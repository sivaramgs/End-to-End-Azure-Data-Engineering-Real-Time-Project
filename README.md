# Project
To implement an end to end data platform from Data Ingestion, Data Transformation, Data Loading and Reporting. 

# High Level Requirements:
- Collect and ingest data from the source system to lakehouse platform.
- Use Azure databricks to transform the RAW data to the most cleanest form of data (Gold Tables).
- Use Azure Synapse Analytics to load the clean data and use Microsoft Power BI to integrate with Azure synapse analytics to build an interactive dashboard.
- Use Azure Active Directory (AAD) and Azure Key Vault for the monitoring and governance purpose.
- Test the data platform Pipeline End to End.
  
# Project Architecture
### ![Architecture](assets/Project_Architecture.png)


# Azure Resource Group
- Created the required resources under single resource group: Azure Key Vault, Azure data factory, Azure databricks workspace, Azure synapse analytics, Azure Storage Account
### ![Architecture](assets/resourcegroup.png)


# Containers created under Azure Storage Account
- Created three containers in ADLS Gen2 Storage for Bronze, Silver and Gold tables used in Azure Databricks.
### ![storagecontainers](assets/storagecontainers.png)


# Secrets created under Azure Key Vault
- Created Azure Key vault secrets: 1) password to connect on-prem database server, 2) databricks token to be used in Datafactory pipeline. 
### ![keyvault](assets/keyvault.png)


# Azure Data Factory Pipeline configuration with Run results
- Created self-hosted Microsoft Integration Runtime and installed it in on-prem system to connect with Azure Datafactory.
- In Azure Data Factory, created a pipeline with copydata and foreach activities to copy all the table data from on-prem to Azure datalake ALDS Gen2.
    1. Created linked services at the required steps in the pipeline.
    2. Configured an access policy to access azure datalake gen2 in the pipeline.
    3. Configured the source and sink in the pipeline activities and pass the table name dynamically to copy data.
    4. Written databricks pyspark notebook to mount the diffferent azure storage containers : bronze, silver, gold and Passed through the credentials.
    5. Written Bronze_to_Silver transformation code to change the date columns with datetimestamp datatype to date datatype in all tables.
    6. Written Silver_To_Gold code to rename the columns that has two joined words with an "_" underscore in between. eg: ModifiedDate as Modified_Date
    7. Tested the datafactory pipeline end-to-end by loading data from on-prem MSSQL to gold table in Azure Datalake Gen2.
  
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
