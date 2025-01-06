from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import *
from pyspark.sql import functions as f
from  datetime import datetime
from  pipeline_config import Schemas, Paths


def collect_to_parquet(spark: SparkSession):
    schema = Schemas.get_json_schema()

    forecast_df = (spark.readStream
                   .format("json")
                   .schema(schema)
                   .load(Paths.RAW_JSON))

    forecast_with_timestamp_df = add_created_at_column(forecast_df)

    query = (forecast_with_timestamp_df.coalesce(1)
             .writeStream
             .outputMode("append")
             .option("path", Paths.PARQUET)
             .option('format', 'parquet')
             .trigger(availableNow=True)
             .option("checkpointLocation", Paths.JSON_CHECKPOINT)
             .start())

    query.awaitTermination()

def add_created_at_column(df: DataFrame) -> DataFrame:

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return df.withColumn(Schemas.CREATED_AT, f.lit(created_at).cast("timestamp"))






