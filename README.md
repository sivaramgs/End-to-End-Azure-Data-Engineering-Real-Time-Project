# Project
To create an end to end data platform from Data Ingestion, Data Transformation, Data Loading and Reporting. 

# High Level Requirements:
- Collect and ingest data from the source system to lakehouse platform.
- Use Azure databricks to transform the RAW data to the most cleanest form of data (Gold Tables).
- Use Azure Synapse Analytics to load the clean data and use Microsoft Power BI to integrate with Azure synapse analytics to build an interactive dashboard.
- Use Azure Active Directory (AAD) and Azure Key Vault for the monitoring and governance purpose.
- Test the data platform Pipeline End to End.
  
# Project Architecture
### ![Architecture](assets/Project_Architecture.png)


# Azure Resources created under Resource Group
### ![Architecture](assets/resourcegroup.png)


# Containers created under Azure Storage Account
### ![storagecontainers](assets/storagecontainers.png)


# Secrets created under Azure Key Vault
### ![keyvault](assets/keyvault.png)


# Azure Data Factory Pipeline configuration with Run results
### ![Datafactory_pipeline](assets/Datafactory_pipeline.png)


# Azure Databricks configuration 
### ![Databricks](assets/azuredatabricks.png)


# Azure Synapse Analytics Pipeline configuration with Run results
### ![Synapse_Analytics](assets/synapse_pipeline.png)


# PowerBi Interactive Dashboard with Synapse Analytics Integration
### ![PowerBi](assets/powerbi.png)


# Tech Stack:
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- Azure Synapse Analytics
- Azure Key vault
- Azure Active Directory (AAD) and
- Microsoft Power BI
