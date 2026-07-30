# Databricks notebook source
# MAGIC %fs ls 's3://hranalyticssss/'

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *

# COMMAND ----------

df = spark.read.format('csv').load('s3://hranalyticssss/Clean_data/',
                                   header=True,inferSchema=True)
                                

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### _Creating Metricess_

# COMMAND ----------

head_count = df.count()
avg_salary = df.agg(avg("Salary")).first()[0]
tot_salary = df.agg(sum("Salary")).first()[0]
female_count=df.where(df['Gender']=='F').count()
male_count=df.where(df['Gender']=='M ').count()
a=df.where(df['EmploymentStatus']=='Active').count()
t=df.filter((df['EmploymentStatus']=='Voluntarily Terminated') | (df['EmploymentStatus']=='Terminated for Cause')).count()

# COMMAND ----------

dm = spark.createDataFrame(
    [(head_count, avg_salary, tot_salary, female_count, male_count,a,t)],
    ["Head Count", "Average Salary", "Total Salary","Female Count","Male Count","Active","Terminated"]
)
dm.display()

# COMMAND ----------

dm.write.format('csv')\
    .mode('append')\
    .options(header='True',delimiter =',')\
    .save('s3://hranalyticssss/Metricess/')