
# Cloudera Data Science Workbench Lab
This is an exercise based on a Cloudera Machine Learning lab. CML is the CDSW version on the cloud as a service.

## Requirements
CDSW installed with your [CDH|HDP|CDP] Cluster

## Introduction

###  Telco churn with refactor code
This is the port of the Refractor prototype which is part of the [Interpretability report from Cloudera Fast Forward Labs](https://clients.fastforwardlabs.com/ff06/report).

## Process

### Step 0 - Setup
Start a Python 3 Session with at least 8GB of memory and __run the utils/setup.py code__.  This will create the minimum setup to use existing, pretrained models.

### Step - 1 Ingest Data
- Open `1_data_ingest.py` in a workbench: python3, 1 CPU, 2 GB.
- Run the file.

### Step 2 - Explore Data
- Open a jupyter notebook at open the `2_data_exploration.ipynb` file

### Step 3 - Train Models
A model has been pre-trained and placed in the models directory.  If you want to retrain the model run the 3_train_models.py code to train a new model.
The model artifact will be saved in the models directory named after the datestamp, dataset and algorithm (ie. 20200304T151133_telco_linear). The default settings will create a linear regression model against the IBM telco dataset. 

### Step 4 - Serve Models
Go to the **Models** section and create a new Explainer model with the following:

* **Name**: Explainer
* **Description**: Explain customer churn prediction
* **File**: 4_model_serve_explainer.py
* **Function**: explain
* **Input**: `{"StreamingTV":"No","MonthlyCharges":70.35,"PhoneService":"No","PaperlessBilling":"No","Partner":"No","OnlineBackup":"No","gender":"Female","Contract":"Month-to-month","TotalCharges":1397.475,"StreamingMovies":"No","DeviceProtection":"No","PaymentMethod":"Bank transfer (automatic)","tenure":29,"Dependents":"No","OnlineSecurity":"No","MultipleLines":"No","InternetService":"DSL","SeniorCitizen":"No","TechSupport":"No"}`
* **Kernel**: Python 3

If you created your own model (see above)
* Click on "Set Environment Variables" and add:
  * **Name**: CHURN_MODEL_NAME
  * **Value**: 20200304T151133_telco_linear  **your model name from above**
  Click "Add" and "Deploy Model"

In the deployed Explainer model -> Settings note (copy) the "Access Key" (ie. mukd9sit7tacnfq2phhn3whc4unq1f38)

### Step 5 - Deploy Application
From the Project level click on "Open Workbench" (note you don't actually have to Launch a session) in order to edit a file.
Select the flask/single_view.html file and paste the Access Key in at line 19.
Save and go back to the Project.

Go to the **Applications** section and select "New Application" with the following:
* **Name**: Visual Churn Analysis
* **Subdomain**: telco-churn
* **Script**: 5_application.py
* **Kernel**: Python 3
* **Engine Profile**: 1vCPU / 2 GiB Memory

If you created your own model (see above)
* Add Environment Variables:
  * **Name**: CHURN_MODEL_NAME
  * **Value**: 20200304T151133_telco_linear  **your model name from above**
  Click "Add" and "Deploy Model"

After the Application deploys, click on the blue-arrow next to the name.  The initial view is a table of rows selected at  random from the dataset.  This shows a global view of which features are most important for the predictor model.

Clicking on any single row will show a "local" interpretabilty of a particular instance.  Here you
can see how adjusting any one of the features will change the instance's churn prediction.


** Don't forget** to stop your Models and Experiments once you are done to save resources for your colleagues.


## Additional options
By default this code trains a linear regression model against the IBM dataset.
There are other datasets and other model types as well.  Set the Project environment variables to try other datasets and models:
Name              Value
CHURN_DATASET     telco (default) | ibm | breastcancer | iris
CHURN_MODEL_TYPE  linear (default) | gb | nonlinear | voting


**NOTE** that not all of these options have been fully tested so your mileage may vary.

## Dataset
### [IBM Churn data](https://www.ibm.com/communities/analytics/watson-analytics-blog/predictive-insights-in-the-telco-customer-churn-data-set/)
### Subscription cable. 7043 rows, 21 features:
    Index(['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
           'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
           'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
           'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
           'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'],
          dtype='object')
