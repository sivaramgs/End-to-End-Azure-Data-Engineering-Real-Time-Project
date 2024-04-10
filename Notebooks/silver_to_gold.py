# Databricks notebook source
# MAGIC %md
# MAGIC Doing transformation in all tables

# COMMAND ----------

tablenames = []
for i in dbutils.fs.ls("/mnt/silver/SalesLT"):
    tablenames.append(i.name.split("/")[0])

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace

# COMMAND ----------

for name in tablenames:
    path = "/mnt/silver/SalesLT/" + name
    df = spark.read.format("delta").load(path)
    column_names = df.columns
    for old_col_name in column_names:
        new_col_name = "".join(["_"+char if char.isupper() and not old_col_name[i-1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_") 
        df = df.withColumnRenamed(old_col_name, new_col_name)
    output_path = "/mnt/gold/SalesLT/" + name+"/"
    df.write.format("delta").mode("overwrite").save(output_path)
