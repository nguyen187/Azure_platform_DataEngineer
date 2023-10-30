# RealTime & BatchTime Azure Platform

This is a practical example of a data engineering project . 
Topics are:
1. Real-Time:
<br>
* Generate data (Python) & send to Azure Event Hub 
* Read Stream data by Stream Analytics 
* Storing on Azure Data Lake Storage Gen2 
* Machine Learning Part: Deploy endpoint Machine learning (trained model) by Azure Machine Learning Studio
* Adding Database features to Azure SQL Server 
* Visualize realtime data by Power BI dashboard

2. Batch-Time:
=======

<br />

* Web App (Html, Css, Js, Flask) : Input file csv and show report 
* Storing on Azure Data Lake Storage Gen2 
* Trigger Databricks job when new file arrive in Blob Storage: Azure Function Apps
* Databrick: Ingest data from blob, ETL, Preprocessing and apply Machine learning model (Spark)
* Delta Lake : raw data (Bronze), Select feature & processingn missing values (Silver), Result (Gold)
* Machine Learning Part: Xgboost and ANN
* Adding Database features to Azure SQL Server 
* Visualize data by Power BI report
<br />
<br /><br />
<img src="https://github.com/nguyen187/Azure_platform/blob/main/Architech.png" width="600">

## Starting generate data
1. Start terminal in RealTime/EventHub folder
2. Run pip install -r requirements.txt
3. Run python generate_realtime_eventhub_operation.py (same with python generate_realtime_eventhub_raman.py)

## Starting Web app
1. Start terminal in BatchTime/WebappDemoplatform folder
2. Run pip install -r requirements.txt
3. Run python main.py

You should create a new env.
# Reference:
- Connect Azure Data Lake Storage Gen2 and Azure Databricks : https://learn.microsoft.com/en-us/azure/databricks/getting-started/connect-to-azure-storage

# WEB DEMO
http://demoplatformv1.azurewebsites.net/

# VIDEO DEMO

https://youtu.be/34y3LF-Zk80
