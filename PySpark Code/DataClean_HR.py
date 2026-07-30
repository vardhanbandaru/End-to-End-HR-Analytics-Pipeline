# Databricks notebook source
# MAGIC %fs ls 's3://hranalyticssss/'

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC ### Reading File

# COMMAND ----------

df = spark.read.format('csv').load('s3://hranalyticssss/HRData.csv',
                                   header =True,inferSchema=True)

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Handling Duplicates

# COMMAND ----------

k= df.distinct()
k.count()

# COMMAND ----------

df = df.dropDuplicates()

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Handling Nulls

# COMMAND ----------

df.select([
    count(when(col(c).isNull(),c)).alias(c)
    for c in df.columns
]).display()

# COMMAND ----------

df = df.dropna('any')
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### _Adding Columns_

# COMMAND ----------

df = df.withColumn('EmployeeSatisfaction',when(df['EmployeeSatisfaction']==5,'Excellent').when(df['EmployeeSatisfaction']==4,'Good').when(df['EmployeeSatisfaction']==3,'Average').when(df['EmployeeSatisfaction']==2,'Low').when(df['EmployeeSatisfaction']==1,'Very Low'))

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.withColumn('HireYear',year(df['HiringDate']))

# COMMAND ----------

df.display()

# COMMAND ----------

df.write.format('csv')\
    .options(header ='True',delimiter =',')\
    .mode('append')\
    .save('s3://hranalyticssss/Clean_data/')


# COMMAND ----------

# MAGIC %md
# MAGIC # **Creating Metrices**

# COMMAND ----------

df.groupBy('EmploymentStatus').sum().display()

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

# COMMAND ----------

