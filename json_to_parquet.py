from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import functions as f
from  datetime import datetime


def collect_to_parquet():
    spark = (SparkSession.builder
             .config("spark.jars.packages", "com.microsoft.azure:spark-mssql-connector_2.12:1.2.0")
             .getOrCreate())

    schema = StructType([
        StructField("city", StringType(), True),
        StructField("date", LongType(), True),
        StructField("temperature_2m", DoubleType(), True)
    ])

    forecast_df = (spark.readStream
                   .format("json")
                   .schema(schema)
                   .load("raw_json/"))

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    forecast_with_timestamp_df = (forecast_df.withColumn("created_at", f.lit(created_at).cast("timestamp")))

    query = (forecast_with_timestamp_df.coalesce(1)
             .writeStream
             .outputMode("append")
             .option("path", "parquet/f.parquet")
             .option('format', 'parquet')
             .trigger(availableNow=True)
             .option("checkpointLocation", "checkpoint/")
             .start())

    query.awaitTermination()






