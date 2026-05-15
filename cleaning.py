print("STARTING SCRIPT...")

import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Eclipse Adoptium\jdk-17.0.19.10-hotspot"
os.environ["PATH"] += r";C:\Program Files\Eclipse Adoptium\jdk-17.0.19.10-hotspot\bin"

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark session
spark = SparkSession.builder \
    .appName("NYC Taxi Cleaning") \
    .getOrCreate()

# Read all parquet files
df = spark.read.parquet(
    "yellow_tripdata_2025-01.parquet",
    "yellow_tripdata_2025-02.parquet",
    "yellow_tripdata_2025-03.parquet"
)

# Show schema
df.printSchema()

# Show sample rows
df.show(5)

# Rows before cleaning
print("Rows before cleaning:", df.count())

# Remove null values
df = df.dropna()

# Remove duplicates
df = df.dropDuplicates()

# Filter invalid trips
df = df.filter(col("trip_distance") > 0)
df = df.filter(col("fare_amount") > 0)
df = df.filter(col("passenger_count") > 0)

# Remove outliers
df = df.filter(col("trip_distance") < 100)
df = df.filter(col("fare_amount") < 500)

# Rows after cleaning
print("Rows after cleaning:", df.count())

# Save cleaned dataset
df.write.mode("overwrite").parquet("cleaned_taxi_data.parquet")

print("Cleaning completed successfully.")