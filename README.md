# RealTime & BatchTime Azure Platform

This is a practical example of a data engineering project. 
Topics are:
1. Infrastructure as Code (IaC) with terraform:

Benefit:
* Automate infrastructure management
* Understanding  infrastructure changes before being applied
Objective:
* Deploy a resource group, a virtual machine, a simple storage, and a data warehouse.
Advanced Criteria:
* State management: Proper management and storage of the state, possible remote backends.
* Modularity: Scripts are modularized using modules, promoting reusability.
* Destruction: Safe destruction of resources without leaving orphaned resources in the cloud
environment.


2. Real-Time:

Architecture with Stream Analytic:

<img src="https://github.com/nguyen187/Azure_platform/blob/main/RealTime/RealTimeWithStreamAnalytic/Architecture_StreamAnalytic.png" width="600">

* Generate data (Python) & send to Azure Event Hub 
* Read Stream data by Stream Analytics 
* Storing on Azure Data Lake Storage Gen2 
* Machine Learning Part: Deploy endpoint Machine learning (trained model) by Azure Machine Learning Studio
* Adding Database features to Azure SQL Server 
* Visualize real-time data by the Power BI dashboard

Architecture with DataBricks:

<img src="https://github.com/nguyen187/Azure_platform/blob/main/RealTime/RealTimeWithDatabricks/Architecture_Databrick.png" width="600">
* Generate data (Python) & send to Azure Event Hub.
* Databricks: using spark to read stream data from the event hub, save data with parquet format in Azure Data Lake Storage Gen2, using push API to send data to Power BI dashboard.

3. Batch-Time:

<img src="https://github.com/nguyen187/Azure_platform/blob/main/Architech.png" width="600">

* Web App (Html, Css, Js, Flask) : Input file csv and show report 
* Storing on Azure Data Lake Storage Gen2 
* Trigger Databricks job when new file arrive in Blob Storage: Azure Function Apps
* Databrick: Ingest data from blob, ETL, Preprocessing and apply Machine learning model (Spark)
* Delta Lake : raw data (Bronze), Select feature & processingn missing values (Silver), Result (Gold)
* Machine Learning Part: Xgboost and ANN
* Adding Database features to Azure SQL Server 
* Visualize data by Power BI report

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
