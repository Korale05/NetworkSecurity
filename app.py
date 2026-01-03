import sys
import os
import certifi
import pandas as pd
import numpy as np

ca = certifi.where()

from dotenv import load_dotenv

#load the environment
load_dotenv()


mongo_db_url = os.getenv("MONGO_DB_URL")
print(mongo_db_url)


import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.constant.training_pipeline import (DATA_INGESTION_COLLECTION_NAME,
                                                        DATA_INGESTION_DATABASE_NAME  )
from networksecurity.utlis.main_utils.utlis import load_object
from networksecurity.utlis.ml_utils.model.estimator import NetworkModel
#Monogo db collection 
client = pymongo.MongoClient(mongo_db_url,tlsCAFile = ca)
database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]


# Flask app

from flask import Flask,request,render_template,jsonify



app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message" : "This is the ml model home page"})


@app.route("/train",methods=['GET'])
def train():
    try:
        logging.info("Training pipeline is initilised")
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        logging.info("Training pipeline is completed")
        return jsonify({"status" : "success",
                       "message" : "Training completed successfully"})
    except Exception as e:
        raise NetworkSecurityException(e,sys)


@app.route("/predict",methods=['GET','POST'])
def predict_route():
    if request.method == "GET":
        return render_template('table.html')
    else:
        try:
            file = request.files["file"]
            df = pd.read_csv(file)
            preprocessor = load_object('final_model/preprocessing.pkl')
            final_model = load_object('final_model/model.pkl')
            network_model = NetworkModel(preprocessor=preprocessor,model=final_model)
            y_pred = network_model.predict(df)
            print(y_pred)
            df['predicted_column'] = y_pred
            table_html = df.to_html(classes='table table-striped')
            df.to_csv("prediction_output/output.csv")
            return render_template("table.html",data = table_html)

        except Exception as e:
            raise NetworkSecurityException(e,sys)

    
if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)




