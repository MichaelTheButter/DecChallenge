from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import functions as f
from  config import MsSqlCredentials
from pipeline_config import Schemas, Paths


url = f"jdbc:sqlserver://;databaseName=weather_db;user={MsSqlCredentials.USERNAME};password={MsSqlCredentials.PASSWORD};"
server_name = "jdbc:sqlserver://DELLMM\\MIKE_MSSQL"
database_name="weather_db"
table_name = "forecast"
connectionProperties = {
    "Trusted_Connection": "yes",
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

def save_batch_to_database(df, epoch_id):
    transformed_df = (df.withColumn(Schemas.DATE, (f.col(Schemas.DATE) / 1000).cast("long"))
            .withColumn(Schemas.FORECAST_DATE, f.from_unixtime(f.col(Schemas.DATE)).cast("timestamp"))
            .withColumnRenamed(Schemas.TEMPERATURE_2M, Schemas.TEMPERATURE)
            .drop(Schemas.DATE)
            .dropDuplicates([Schemas.CITY, Schemas.FORECAST_DATE]))

    (transformed_df.write
     .mode("append")
     .jdbc(url=url, table=table_name, properties=connectionProperties))


def run_db_loader(spark: SparkSession):
    schema = Schemas.get_parquet_schema()

    forecast_df = (spark.readStream
                   .schema(schema)
                   .parquet(path=Paths.PARQUET))

    db_query = (forecast_df.writeStream
     .option("checkpointLocation", Paths.PARQUET_CHECKPOINT)
     .trigger(availableNow=True)
     .foreachBatch(save_batch_to_database)
     .start())

    db_query.awaitTermination()