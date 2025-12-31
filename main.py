from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
import sys
import os
if __name__=='__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        dataingestion_config = DataIngestionConfig(training_pipeline_config)
        dataingestion = DataIngestion(dataingestion_config)
        logging.info("Initiate the data ingestion")
        dataingestion_artifacts = dataingestion.initiate_data_ingestion()
        logging.info("Data initiation completed")
        print(dataingestion_artifacts)
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(dataingestion_artifacts,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_Artifacts = data_validation.initiate_data_validation()
        logging.info(" data Validation Completed")
        print(data_validation_Artifacts)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
