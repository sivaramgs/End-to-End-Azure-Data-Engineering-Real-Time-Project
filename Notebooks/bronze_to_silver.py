# Databricks notebook source
tablenames = []
for i in dbutils.fs.ls("/mnt/bronze/SalesLT"):
    tablenames.append(i.name.split("/")[0])

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

# COMMAND ----------

# Applying the changes to the required columns in all the tables of Bronze layer
# Storing the transformed dateframe with modified date columns format in Silver layer in delta file format
for i in tablenames:
    path = "/mnt/bronze/SalesLT/" + i +"/"+ i +".parquet"
    df = spark.read.format("parquet").load(path)
    columns = df.columns

    for col in columns:
        if "Date" in col or "date" in col:
            df = df.withColumn(col, date_format(from_utc_timestamp(df[col].cast(TimestampType()),"UTC"),"yyyy-MM-dd"))
    output_path = "/mnt/silver/SalesLT/" + i
    df.write.format("delta").mode("overwrite").save(output_path)

# COMMAND ----------

display(df)
