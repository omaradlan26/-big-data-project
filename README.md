📌 Big Data Project – NYC Taxi Data Cleaning
👨‍💻 Member 1 – Data Cleaning (PySpark)

This part of the project focuses on loading and cleaning NYC Taxi trip data using Apache Spark.

📊 Dataset

The project uses NYC Yellow Taxi trip data in Parquet format:

yellow_tripdata_2025-01.parquet
yellow_tripdata_2025-02.parquet
yellow_tripdata_2025-03.parquet

⚠️ Large dataset files are excluded from the repository using .gitignore.

⚙️ Technologies Used
Python 🐍
PySpark ⚡
Apache Spark
🧹 Data Cleaning Steps

Implemented in cleaning.py:

Load multiple Parquet files using Spark
Display dataset schema using printSchema()
Show sample records using show()
Handle missing values (nulls)
Remove duplicate records
Filter invalid trips (e.g., trip_distance > 0)
📈 Output Summary
Dataset schema printed successfully
First 5 rows displayed
Dataset size reduced after cleaning

Example:

Rows before cleaning: ~11,198,026
Rows after cleaning: ~8,578,838
🚀 How to Run
python cleaning.py

Make sure the following are installed:

Java
Apache Spark
PySpark
📌 Notes
This section includes only Member 1 (Data Cleaning) work.
No feature engineering or machine learning is included here.
Large dataset files are not uploaded to GitHub.
🏁 Status

✔ Data Loading
✔ Data Cleaning
✔ Data Filtering
✔ Output Validation
