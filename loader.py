from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import functions as f
from  config import MsSqlCredentials


spark = SparkSession.builder.config("spark.jars.packages", "com.microsoft.azure:spark-mssql-connector_2.12:1.2.0").getOrCreate()
schema = StructType([
    StructField("city", StringType(), True),
    StructField("date", LongType(), True),
    StructField("temperature_2m", DoubleType(), True),
    StructField("created_at", TimestampType(), True)
])


df_2 = spark.read.schema(schema).json(path="raw_json/")
df_3 =(df_2.withColumn("date", (f.col("date")/1000).cast("long"))
       .withColumn("forecast_date", f.from_unixtime(f.col("date")).cast("timestamp"))
       .withColumnRenamed("temperature_2m", "temperature")
       .drop("date")
       .dropDuplicates(["city", "forecast_date"]))
df_3.show()
url = f"jdbc:sqlserver://;databaseName=weather_db;user={MsSqlCredentials.USERNAME};password={MsSqlCredentials.PASSWORD};"

server_name = "jdbc:sqlserver://DELLMM\\MIKE_MSSQL"
database_name="weather_db"

table_name = "forecast"

connectionProperties = {
    "Trusted_Connection": "yes",
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

df_3.write.mode("append").jdbc(url=url, table=table_name, properties=connectionProperties)