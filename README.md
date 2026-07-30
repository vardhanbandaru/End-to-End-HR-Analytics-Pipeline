# End-to-End-HR-Analytics-Pipeline

## Project Overview

This project demonstrates an end-to-end HR Analytics pipeline that ingests employee data from a CSV file, performs data cleaning and transformation, generates business metrics, and visualizes actionable insights through an interactive dashboard.

The objective of this project is to simulate a real-world data engineering workflow where raw HR data is transformed into meaningful business information for decision-making.

---

## Business Problem

Human Resource departments generate large amounts of employee data that require cleaning, transformation, and analysis before meaningful insights can be obtained.

This project automates the complete data pipeline from data ingestion to dashboard reporting, enabling HR teams to monitor workforce metrics such as employee count, salary distribution, department-wise performance, recruitment sources, and employee demographics.

---

## Project Workflow

1. HR data is collected as a CSV file.
2. The raw data is uploaded to cloud object storage(AWS S3).
3. Data is processed and cleaned using distributed data processing(Apache Spark).
4. Business metrics are generated from the transformed data.
5. Cleaned data and metrics are stored in the data lake.
6. Metadata is registered in the data catalog(AWS Glue Catalog).
7. SQL queries are executed using a serverless query engine(AWS Athena).
8. Power BI connects through ODBC to visualize HR insights.

---

## Features

- Data Ingestion
- Data Cleaning
- Data Transformation
- KPI Generation
- Employee Analytics
- Department Analysis
- Gender Distribution Analysis
- Salary Analysis
- Recruitment Source Analysis
- Interactive Dashboard
- End-to-End Data Pipeline

---

## Dashboard Insights

The dashboard provides insights into:

- Total Employees
- Active Employees
- Terminated Employees
- Average Salary
- Employee Satisfaction
- Department-wise Employee Distribution
- Gender Distribution
- Recruitment Source Analysis
- Performance Score Analysis
- State-wise Employee Distribution

---

## Technologies Used

### Programming

- Python
- PySpark
- SQL

### Cloud Services

- Amazon S3
- AWS Glue Data Catalog
- Amazon Athena

### Data Platform

- Databricks
- Apache Spark
- Apache Iceberg

### Business Intelligence

- Microsoft Power BI
- ODBC Driver

---

## Project Architecture

Local CSV

↓

Amazon S3 (Raw Layer)

↓

Databricks (Data Cleaning & Transformation)

↓

Apache Iceberg Tables

↓

AWS Glue Catalog

↓

Amazon Athena

↓

Power BI (ODBC Connection)

↓

HR Analytics Dashboard

---
