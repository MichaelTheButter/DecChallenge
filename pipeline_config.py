from pyspark.sql import SparkSession
from pyspark.sql.types import *




def get_spark_session() -> SparkSession:
    spark: SparkSession = (SparkSession.builder
             .config("spark.jars.packages", "com.microsoft.azure:spark-mssql-connector_2.12:1.2.0")
             .getOrCreate())
    return spark

class Schemas:
    CITY = "city"
    DATE = "date"
    TEMPERATURE_2M = "temperature_2m"
    CREATED_AT = "created_at"
    TEMPERATURE = "temperature"
    FORECAST_DATE = "forecast_date"

    @staticmethod
    def get_json_schema() -> StructType:
        schema = StructType([
            StructField(Schemas.CITY, StringType(), True),
            StructField(Schemas.DATE, LongType(), True),
            StructField(Schemas.TEMPERATURE_2M, DoubleType(), True)
        ])
        return schema

    @staticmethod
    def get_parquet_schema() -> StructType:
        schema = StructType([
            StructField(Schemas.CITY, StringType(), True),
            StructField(Schemas.DATE, LongType(), True),
            StructField(Schemas.TEMPERATURE_2M, DoubleType(), True),
            StructField(Schemas.CREATED_AT, TimestampType(), True)
        ])
        return schema

class Paths:
    RAW_JSON = "raw_json/"
    PARQUET = "parquet/final.parquet"
    JSON_CHECKPOINT = "checkpoints/json"
    PARQUET_CHECKPOINT = "checkpoints/parquet"

