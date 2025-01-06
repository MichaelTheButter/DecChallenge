from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pipeline_config import Schemas

spark = SparkSession.builder.appName("test").getOrCreate()

df = (spark.read
      .parquet("parquet/final.parquet")
      .withColumn(Schemas.DATE, (f.col(Schemas.DATE) / 1000).cast("long"))
      .withColumn(Schemas.FORECAST_DATE, f.from_unixtime(f.col(Schemas.DATE)).cast("timestamp")))
df.show()
