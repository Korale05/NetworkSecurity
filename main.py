from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer
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


        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformation(data_validation_Artifacts,data_transformation_config)
        logging.info("Initiate the data transformation")
        data_transformation_Artifacts = data_transformation.initiate_data_transformation()
        logging.info("data transformation completed")
        print(data_transformation_Artifacts)

        logging.info("Model training started")
        model_trainer_config = ModelTrainerConfig(training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifacts=data_transformation_Artifacts)
        model_trainer_artifacts = model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")
        
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
