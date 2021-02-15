# Anomaly_detection_pycaret
## Introduction
   This is manufacturing anomaly on industrial_hourly_reject_dataset.
## Dataset: industrial_hourly_reject_dataset
## Dependencies:
   This machine learning model is trained on Pycaret.
   
## Installation   
## REST API SETUP
### Download Anaconda 5.3.0 or above
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
### Install Anaconda
bash ~/Downloads/Anaconda3-2020.02-Linux-x86_64.sh

### Create conda environment
conda create -n pycaret python=3.6 anaconda

### Activate the environment
conda activate pycaret

### Install pycaret
pip install pycaret

### Clone the repo
git clone https://github.com/Dharani1008/Anomaly_detection_pycaret

### run the api server
python flask_v8.py

### Test the api server

cURL command example:
`curl -F "file={json_data}  http://{ipaddress}:5012/api/v0`

or

Run python check8.py

## How to create models in pycaret
1. Load the dataset using pandas library
2. Import pycaret anomaly detection module
3. Initialize data with pycaret setup()
4. Create anyone pycaret model with create_model()
5. Use assign_model() for producing label for anomalies.
6. Use the predict_model() for predicting on unseen data.
7. Save the model use save_model() in .pkl format.
8. Use load_model() for loading model for future usage.

