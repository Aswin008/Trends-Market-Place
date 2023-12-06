<img src="https://iili.io/JIxT2gn.md.jpg" alt="JIxT2gn.md.jpg" border="0">

# Small Investments in Machine Learning can lead to Big Returns for Small Businesses
******
### Project videos:
* <p style="font-size:17px"><a href="https://azure.microsoft.com/en-us/pricing/">Step-by-Step Guide on How to Use this Repository</a></p>
* <p style="font-size:17px"><a href="https://azure.microsoft.com/en-us/pricing/">Presentation</a></p>
******


## Barrier to Access ML Tools for Small Businesses
******
Data is all around us. It is generated every time we interact with the greater world, such as making a purchase at your favorite store or coffee shop, going for a walk with your phone in your pocket, or browsing the internet.  In recent years, businesses have realized the importance of data and that implementing data analytics tools can yield returns by offering novel insights.  With the meteoric rise of OpenAI's ChatGPT, Concepts like "Machine Learning" and "Artificial Intelligence" have reached most corners our society. 

Small business owners are now contemplating how they might be able to add machine learning (ML) into their box of tools.  Fortunately, with tools within the Azure ecosystem, individuals can build and implement ML models without having to write a single line of code.  Azure removes the barriers most small business owners experience when they explore ML implementation. 

Lacking solutions for these challenges, the barrier for small business to access ML tools may be too great:
* What is even possible with machine learning?
* Limited or no experience with coding or high-level analytics
* Large investment in the resources, such as hardware/software and hiring/contracting individuals with these skills can be very expensive


## Azure as an ML Solution for Small Businesses
******
The __Automated ML__ module within Azure ML Studio can create configurations of various Azure services to create a start-to-finish ML Pipeline to meet the needs of many small businesses.

Key features offed within __Automated ML__ to make accessible to all are:

* A menu of automated ML tasks to individuals to create machine learning pipelines.
* A reasonably priced pay-as-you-go subscription plan
* Cloud computing resources that can scale as the business grows
* A pledge to offer responsible machine learning solutions

When taken together, these features allow small businesses to take advantage of machine learning tools and techniques by removing the burdensome upfront investment of time, money, and resources.


### Three ML Tasks that Small Business 

1. __Dynamic Forecasting:__ Quickly create adaptive forecasting models to reduce costs (unsold or expired inventory) and/or lost revenue (missed sales from depleted inventory)

2. __Spam Detection:__ Automate a workflow to detect which user/loyalty accounts belonging to real humans and delete accounts belonging to bots
    
3. __Customer Characterization:__ Create individualized marketing initiatives by using a customer's behavior on store's website to predict the likelihood they will make a purchase 


<br>

## Technical Overview
******
<img src="https://iili.io/JIx3hbe.md.jpg" alt="JIx3hbe.md.jpg" border="0">

<p style="text-align: center;">Image above represents a common ML pipeline and may include services and features not explored within this demonstration.</p>
<br> <br>
This demonstration establishes a pipeline for streaming clickstream data to a Microsoft Event Hub and visualizing it in a Power BI Dashboard. Using Azure services, notably Cosmos DB, we ingest and process data efficiently. A script generates simulated clickstream data that can be ingested into a pre-configured Event Hub, that accepts data as Avro files. This demonstrates Azure's capability to integrate Power BI's analytics tools within a streaming analytics pipeline.

### Constructing the Dataset

This pipeline utilizes simulated data.  Based the experience our team members, we were able to write a script that continuously generates clickstream data.  These are the features of the dataset.

|Feature | Data Type | Example |
| :-----------: | :-----------: | :-----------: |
|Time of Event | datetime | "10/31/2024 14:33:57" |
|Action | categorical | "click", "hover", "scroll"|
|Last Website (prior to arriving) | URL string | "www.google.com"|
|Device Type| "string" | "tablet"|
|Time on Webpage (s)| datetime | 25s |
|Geographic Location | string | "Minneapolis, MN"|
|Page Viewing | URL string | "www.fakewebsite.com/products/"|
|Promotion Offered | binary | True |
|Purchase Made (outcome)| binary | False |
|User Engagement Score (outcome) | binary | False|



### Azure ML Studio, Automated ML (ML Pipeline Builder)
Before streaming data is able to processed and ingested, we used historical data to build our predictive model in Automated (ML within Azure ML Studio).  In this demonstration, clickstream data follows a structured pattern, and is relatively clean and can therefore be used with little to no pre-processing of the data.
#### Features
* User defined hyperparameters with easy to understand definitions
* ML tasks available with Automated ML include
    * Common Taks: classification, regression, time-series forecasting
    * Text: text classification, multilabel text classification, named entity recognition
    * Images: image classification, object detection, and image segmentation
* Identifies key features within the model and provides visualizations and a summary to give users context on their importance   


### Azure Event Hubs (data ingestion)
After The Azure event hub is the entry point to the Azure Data Pipeline.  When data is created with your business' ecosystem, Event Hubs are able to collect or ingest this data for future use.  Regardless of use-case or business needs, there is a event hub configuration to fulfill your data demands.
#### Features
* Can be utilized in a strictly cloud-based solution or a hybrid-cloud solution
* Continuously ingest data
* Multiple data destinations:
    * Store raw data as-is in a data lake (i.e. Azure Blob Storage)
    * Connect directly to Stream Analytics

### Azure Event Stream Analytics (ETL & Analysis)
Optimized to process high volumes of data in real-time, Event Streaming Analytics is a fully managed service for streaming data.  For this demonstration, Event Stream Analytics serves as our final destination of our data in this pipeline.

#### Features
* Combine data from multiple streaming sources
* Transform data within Event Stream Analytics data with SQL-based queries
* Stream data from Event Stream Analytics to create real-time dashboards in Power BI Pipe 

<br>

## Team Members
******
|Name | LinkedIn | Github |
| :-----------: | :-----------: | :-----------: |
| Aswin Ganesh Kumar Sreekala | <a href="https://www.linkedin.com/in/aswings/">aswings</a> | <a href="https://github.com/Aswin008/">Aswin008</a> |
| Otto Gaulke | <a href="https://www.linkedin.com/in/ottogaulke//">ottogaulke</a> | <a href="https://github.com/ottogaulke">ottogaulke</a> |
| Jincheng Ji | <a href="https://www.linkedin.com/in/jjcray1218/">jjcray1218</a> | <a href="https://github.com/icg1218">icg1218</a> |
| Madison Meinke | <a href="https://www.linkedin.com/in/madison-meinke-2974611b9/">madison-meinke-2974611b9</a> | <a href="https://github.com/mad-meinke08/">mad-meinke08</a> |
| Natalia Mendoza-Orr | <a href="https://www.linkedin.com/in/nmendoza-orr//">nmendoza-orr</a> | <a href="https://github.com/njmorr/">njmorr</a> |
| Zhuofan Zhai | <a href="https://www.linkedin.com/in/zhuofan-zhai-4b1757228/">zhuofan-zhai-4b1757228</a> | <a href="https://github.com/Erik1010101010/">Erik1010101010</a> |

* The State of Data in Motion (2022 Report)
    * <a href="https://static1.squarespace.com/static/5e9491b0c2923c644bacc529/t/62d5ded3727bb8247f3e015c/1658183403823/Confluent-20220512-RPT-Data_in_Motion-ENG+%281%29.pdf">Confluent.io</a>
* 6 Ways Your Small Business Can Benefit From Machine Learning Solutions
    * <a href="https://builtin.com/machine-learning/small-business-benefit-machine-learning">builtin.com</a>
* 11 Tech Experts On How Small Businesses Can Effectively Leverage Machine Learning
    * <a href="https://www.forbes.com/sites/forbestechcouncil/2022/09/09/11-tech-experts-on-how-small-businesses-can-effectively-leverage-machine-learning/?sh=22f7ecc44ff3">Forbes.com</a>
* 6 Creative Ways to Use Machine Learning for Small Business
    * <a href="https://www.fiverr.com/resources/guides/programming-tech/machine-learning-for-smb">Fiverr.com</a>
* Microsoft Azure revenue growth worldwide from financial year 2020 to 2023, by quarter
    * <a href="https://www.statista.com/statistics/1242206/microsoft-azure-revenue-yoy-quarterly">statista.com</a>   
* Azure vs. AWS Pricing: A Quick Comparison
    * <a href="https://bluexp.netapp.com/blog/azure-vs-aws-pricing-comparing-apples-to-apples-azure-aws-cvo-blg">bluexp.netapp.com</a>
* What is Azure Stream Analytics?
    * <a href="https://www.element61.be/en/competence/microsoft-azure-stream-analytics">element61.be</a>
* Microsoft Azure and its most used services
    * <a href="https://blog.clairvoyantsoft.com/microsoft-azure-and-its-most-used-services-15580f2105d5">clairvoyantsoft.com</a>
* Microsoft Azure: The only consistent, comprehensive hybrid cloud
    * <a href="https://azure.microsoft.com/en-us/blog/microsoft-azure-the-only-consistent-comprehensive-hybrid-cloud/">microsoft.com</a>
* Overview of Amazon Web Services
    * <a href="https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html">amazon.com</a>
* Run Jupyter notebooks in your workspace
    * <a href="https://learn.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks?view=azureml-api-2">microsoft.com</a>



#### MS Azure Product Documentation
* <a href="https://azure.microsoft.com/en-us/products/machine-learning/automatedml/">Automated ML</a>
* <a href="https://azure.microsoft.com/en-us/products/event-hubs">Event Hubs</a>
* <a href="https://azure.microsoft.com/en-us/products/stream-analytics">Stream Analytics</a>
* <a href="https://azure.microsoft.com/en-us/pricing/">Azure Pricing</a>


*******
Disclaimer: This project repository is created in partial fulfillment of the requirements
for the Big Data Analytics course offered by the Master of Science in Business Analytics
program at the Carlson School of Management, University of Minnesota.