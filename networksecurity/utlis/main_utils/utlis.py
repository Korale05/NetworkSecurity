import os
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
import pandas as pd
import sys
import dill
import pickle
import yaml
import numpy as np
import pickle
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import r2_score
import mlflow

def read_yaml_file(file_path : str)->dict:
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def write_yaml_file(file_path : str,content : object, replace : bool = False)->None:
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
                
        with open(file_path,"w") as file:
            yaml.dump(content,file)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    

def save_numpy_array_data(file_path : str,array : np.array):
    """
    Save numpy array data to file
    file_path : str location of file to save
    array : np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            np.save(file_obj,array)
        logging.info(f"Save the numpy file as {file_path}")
    except Exception as e:
        raise NetworkSecurityException(e,sys)

def save_object(file_path : str,obj : object)->None:
    try:
        logging.info("Enterd the save_object method of Main utils class")
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
        logging.info("Exited the save object method of Mainutils class")
    except Exception as e:
        raise NetworkSecurityException(e,sys)


def load_object(file_path : str)->object:
    try:
        if not os.path.exists(file_path):
            raise NetworkSecurityException(f"File not found {file_path}")
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    

def load_numpy_array_data(file_path : str)->np.array:
    """
    load numpy array data from file
    file_path : str location of file to load
    return : np.array data loaded
    """
    try:
        if not os.path.exists(file_path):
            raise NetworkSecurityException(f"File not found {file_path}")
        with open(file_path,'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    

def evaluate_models(x_train,y_train,x_test,y_test,models : dict,params):
    try:
        report = {}
        mlflow.set_experiment("Network Security")

        for name,model in models.items():
            print(f"Training : {name}")
            param = params.get(name)
            rs = RandomizedSearchCV(estimator=model,param_distributions=param,cv=3)
            rs.fit(x_train,y_train)

            model.set_params(**rs.best_params_)
            model.fit(x_train,y_train)
            
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)
            
            # MLflow Run
            with mlflow.start_run(run_name=name):
                
                # log all best params
                for k , v in rs.best_params_.items():
                    mlflow.log_param(k,v)
                
                # log metrics
                mlflow.log_metric("train_r2",train_model_score)
                mlflow.log_metric("test_r2",test_model_score)

                  # log model
                mlflow.sklearn.log_model(model,"Model")

            # store result
            report[name] = test_model_score
        return report

    except Exception as e:
        raise NetworkSecurityException(e,sys)
