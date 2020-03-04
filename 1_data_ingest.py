import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import *

# Get Spark Session
spark = SparkSession\
    .builder\
    .appName("PythonSQL")\
    .master("yarn") \
    .getOrCreate()

# Schema
schema = StructType(
  [
    StructField("customerID", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("SeniorCitizen", StringType(), True),
    StructField("Partner", StringType(), True),
    StructField("Dependents", StringType(), True),
    StructField("tenure", DoubleType(), True),
    StructField("PhoneService", StringType(), True),
    StructField("MultipleLines", StringType(), True),
    StructField("InternetService", StringType(), True),
    StructField("OnlineSecurity", StringType(), True),
    StructField("OnlineBackup", StringType(), True),
    StructField("DeviceProtection", StringType(), True),
    StructField("TechSupport", StringType(), True),
    StructField("StreamingTV", StringType(), True),
    StructField("StreamingMovies", StringType(), True),
    StructField("Contract", StringType(), True),
    StructField("PaperlessBilling", StringType(), True),
    StructField("PaymentMethod", StringType(), True),
    StructField("MonthlyCharges", DoubleType(), True),
    StructField("TotalCharges", DoubleType(), True),
    StructField("Churn", StringType(), True)
  ]
)    

# Upload to HDFS
!hdfs dfs -copyFromLocal raw/WA_Fn-UseC_-Telco-Customer-Churn.csv /tmp/WA_Fn-UseC_-Telco-Customer-Churn.csv

# Read it!    
telco_data = spark.read.csv(
  "/tmp/WA_Fn-UseC_-Telco-Customer-Churn.csv",
  header=True,
  schema=schema,
  sep=',',
  nullValue='NA'
)

telco_data.show()

telco_data.printSchema()

# Save it locally. This operation will fail if you don't have 8GB RAM
telco_data.coalesce(1).write.csv(
  path="/tmp/telco-data/",
  mode='overwrite',
  header=True
)

spark.sql("show databases").show()

spark.sql("show tables in default").show()

# Create table in HDFS as Parquet
telco_data\
  .write.format("parquet")\
  .mode("overwrite")\
  .saveAsTable('default.telco_churn', path="/tmp/spark-warehouse")

# Test table
spark.sql("select * from default.telco_churn").show()
