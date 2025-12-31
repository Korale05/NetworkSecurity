import os
from networksecurity.entity.artifact_entity import DataIngestionArtifacts,DataValidationArtifacts
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.utlis.main_utils.utlis import read_yaml_file,write_yaml_file
from scipy.stats import ks_2samp
import pandas as pd
import sys


class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifacts,
                     data_validation_config : DataValidationConfig ):
        try:
            self.data_ingestion_artifacts = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._scheme_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
     
    @staticmethod
    def read_data(file_path):
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    
    def validate_number_of_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            number_of_columns = len(self._scheme_config["columns"])
            logging.info(f"Requried number of columns : {number_of_columns}")
            logging.info(f"Data Frame columns : {len(dataframe.columns)}")
            
            if len(dataframe.columns) == number_of_columns:
                return True
            else : 
                return False

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def validate_numerical_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            number_of_num_columns = len(self._scheme_config['numerical_columns'])
            logging.info(f"Required number of numerical columns : {number_of_num_columns}")
            dataframe_num_columns = len(dataframe.select_dtypes(exclude='object').columns)
            logging.info(f"Data frame numerical columns : {dataframe_num_columns}")
            
            if number_of_num_columns == dataframe_num_columns:
                return True
            else :
                return False
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def detect_dataset_drift(self,base_df,current_df,threshold=0.05)->bool:
        try:
            status = True
            report = {}
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_sample_dist = ks_2samp(d1,d2)

                if is_sample_dist.pvalue >= threshold :  #We can’t say they’re different.”
                    is_found = False 
                else:         #the distributions are different.
                    is_found = True
                    status = False
                report.update({column:{
                    "p_value" : float(is_sample_dist.pvalue),
                    "drift_status" : is_found
                }})
            drift_report_file_path = self.data_validation_config.drift_report_file_path

            #create a directory
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path,content=report)
            return status

        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def initiate_data_validation(self)->DataValidationArtifacts:
        try:
            train_file_path = self.data_ingestion_artifacts.trained_file_path
            test_file_path = self.data_ingestion_artifacts.test_file_path

            # read the data from train and test 
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            error_message=""

            # validate number of columns
            status = self.validate_number_of_columns(dataframe=train_dataframe)

            if not status:
                error_message += f"Train data frame does not contain all columns.\n"
            
            status = self.validate_number_of_columns(dataframe=test_dataframe)

            if not status:
                error_message += f"Test data frame does not contain all columns.\n"
            

            # validate number of numerical columns
            status = self.validate_numerical_columns(dataframe=train_dataframe)
            
            if not status:
                error_message += f"Train data frame does not contain all numerical column"
            
            status = self.validate_numerical_columns(dataframe=test_dataframe)

            if not status:
                error_message += f"Test data frame does not contain all numerical column"
            
            if error_message !="":
                raise NetworkSecurityException(error_message)
            

            # lets check the data drift
            status = self.detect_dataset_drift(base_df=train_dataframe,current_df=test_dataframe)
            dir_path = os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(dir_path,exist_ok=True)

            train_dataframe.to_csv(self.data_validation_config.valid_train_file_path,
                                   index=False,header=True
            )
            test_dataframe.to_csv(self.data_validation_config.valid_test_file_path,
                                  index=False,header=True
            )
            data_validation_artifact = DataValidationArtifacts(
                validaion_status = status,
                valid_train_file_path = self.data_validation_config.valid_train_file_path,
                valid_test_file_path = self.data_validation_config.valid_test_file_path,
                invalid_train_file_path = None,
                invalid_test_file_path = None,
                drift_report_file_path = self.data_validation_config.drift_report_file_path
            )
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)




