# Hey this is my network security project ## 
## lets goooooooooooooooooooooooooooooooo

# Data Ingestion → Data Validation → Data Transformation → Training → Evaluation → Deployment



# 📥 Data Ingestion Module

The Data Ingestion module is responsible for extracting raw network security data from MongoDB, storing it as feature-store data, and preparing clean train/test datasets for downstream pipeline stages.

This is the first step in the ML pipeline.

🎯 Objectives

This module:

✔ Connects securely to MongoDB
✔ Loads data into a pandas DataFrame
✔ Cleans system-generated _id fields
✔ Stores a local feature-store copy
✔ Splits data into train & test sets
✔ Saves outputs as versioned artifacts

It ensures every pipeline run uses consistent, reproducible data.

🧠 Class: DataIngestion
Inputs

Provided via DataIngestionConfig:

Setting	Purpose
database_name	MongoDB database
collection_name	MongoDB collection
feature_store_file_path	Path to store raw dataset
training_file_path	Path for training dataset
testing_file_path	Path for testing dataset
train_test_split_ratio	% test size

MongoDB connection is read from:

MONGO_DB_URL (env variable)

📤 Outputs

Returns a DataIngestionArtifacts object:

Field	Description
trained_file_path	Path to training CSV
test_file_path	Path to testing CSV

These files are used by Data Validation next.

⚙️ Processing Workflow
┌──────────────────────────────┐
│ Connect to MongoDB           │
└───────────────┬──────────────┘
                ▼
┌──────────────────────────────┐
│ Load Collection into DataFrame│
└───────────────┬──────────────┘
                ▼
┌──────────────────────────────┐
│ Remove _id Column            │
└───────────────┬──────────────┘
                ▼
┌──────────────────────────────┐
│ Save Raw Data (Feature Store)│
└───────────────┬──────────────┘
                ▼
┌──────────────────────────────┐
│ Train–Test Split             │
└───────────────┬──────────────┘
                ▼
┌──────────────────────────────┐
│ Save Train & Test Files      │
└──────────────────────────────┘

🧪 Key Features
1️⃣ Extract Data from MongoDB

The module connects to MongoDB and loads the full dataset into a pandas DataFrame:

✔ reads all records
✔ converts to DataFrame
✔ drops _id column
✔ replaces "na" with NaN

This ensures ML-ready data.

2️⃣ Feature Store Export

The raw dataset is stored locally as:

feature_store_file_path


Purpose:

✔ reproducibility
✔ offline access
✔ audit trail

3️⃣ Train–Test Split

Performed using sklearn.model_selection.train_test_split:

Reproducible via random_state=42

Test size configurable

Train & Test saved separately

📁 Artifacts Created

Example structure:

Artifacts/
 └── <timestamp>/
     ├── data_ingestion/
     │   ├── feature_store.csv
     │   ├── train.csv
     │   └── test.csv

🚨 Error Handling

All failures are wrapped into:

NetworkSecurityException


Ensuring:

✔ clear stack trace
✔ consistent error logging
✔ graceful pipeline failure

🎯 Why Data Ingestion Matters

This step guarantees that:

✔ data is versioned
✔ sources are traceable
✔ splits are consistent
✔ pipeline remains stable

It sets a strong foundation for the ML workflow.



# 🧩 Data Validation Module — Overview

This module validates the ingested training and test datasets before they enter the ML pipeline. The goal is to ensure the data schema is correct and to detect potential data drift between training and testing splits.

✔ Key Responsibilities
1️⃣ Load Schema Configuration

Reads the schema YAML file

Uses it to validate:

Expected columns

Numerical column count

2️⃣ Read Input CSV Files

Utility method:

read_data(path)


Loads CSV files into pandas DataFrames.

3️⃣ Validate Schema
✔ Check column count

Verifies that the dataset contains the exact number of expected columns.

✔ Validate numerical columns

Confirms the number of numeric-type columns matches what the schema defines.

If any mismatch occurs → validation fails.

4️⃣ Detect Data Drift (KS Test)

Uses Kolmogorov–Smirnov test (ks_2samp) to compare:

train distribution  vs  test distribution


for each feature.

If p-value ≥ 0.05 → no drift

If p-value < 0.05 → drift detected

A YAML report is created and stored at:

drift_report_file_path

5️⃣ Save Validated Datasets

If validation succeeds:

Train → valid_train_file_path

Test → valid_test_file_path

Both are saved in CSV format.

6️⃣ Return Validation Artifact

Builds and returns a DataValidationArtifacts object containing:

Field	Meaning
validaion_status	Whether data passed validation
valid_train_file_path	Path to cleaned train data
valid_test_file_path	Path to cleaned test data
invalid_train_file_path	(Reserved for future use)
invalid_test_file_path	(Reserved for future use)
drift_report_file_path	YAML drift report

This artifact is then used by the next pipeline stage.

🚨 Error Handling

Any exception is wrapped and raised as:

NetworkSecurityException


So the pipeline stops safely with meaningful logs.

🎯 Why This Step Matters

Data validation prevents:

✔ training on corrupted data
✔ schema mismatch crashes
✔ silent performance degradation due to drift

It keeps the ML pipeline reliable and reproducible.





