import os
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
import pandas as pd
import sys
import dill
import pickle
import yaml


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