import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)

from networksecurity.entity.artifact_entity import (
    DataIngestionArtifacts,
    DataValidationArtifacts,
    DataTransformationArtifacts,
    ModelTrainerArtifacts,
)


class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
    
    def start_data_ingestion(self):
        try:

            self.data_ingestion_config = DataIngestionConfig(self.training_pipeline_config)
            logging.info("Initiate the  data ingestion")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info(f"data ingestion completed and artifacts : {data_ingestion_artifacts}")
            return data_ingestion_artifacts
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def start_data_validation(self,data_ingestion_artifacts : DataIngestionArtifacts):
        try:

            data_validation_config = DataValidationConfig(self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifacts,data_validation_config)
            logging.info("Initiate the  data validation")
            data_validation_artifacts = data_validation.initiate_data_validation()
            logging.info(f"Data validation completed and artifacts {data_ingestion_artifacts}")
            return data_validation_artifacts

        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def start_data_transformation(self,data_validation_artifacts : DataValidationArtifacts):
        try:
            data_transformation_config = DataTransformationConfig(self.training_pipeline_config)
            data_transformation = DataTransformation(data_transformation_config=data_transformation_config,data_validation_artifact=data_validation_artifacts)
            logging.info("Initiate the data transformation")
            data_transformation_artifacts = data_transformation.initiate_data_transformation()
            logging.info(f"Data transformation Completed and artifacts {data_transformation_artifacts}")
            return data_transformation_artifacts
      
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def start_model_trainer(self,data_transformation_artifacts : DataTransformationArtifacts):
        try:
            self.model_trainer_config = ModelTrainerConfig(
                training_pipelin_config=self.training_pipeline_config
            )
            model_trainer = ModelTrainer(
                model_trainer_config=self.model_trainer_config,
                data_transformation_artifacts=data_transformation_artifacts
            )
            model_trainer_artifacts = model_trainer.initiate_model_trainer()
            
            return model_trainer_artifacts

        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_validation_artifacts = self.start_data_validation(data_ingestion_artifacts)
            data_transformation_artifacts = self.start_data_transformation(data_validation_artifacts)
            model_trainer_artifacts = self.start_model_trainer(data_transformation_artifacts)
            return model_trainer_artifacts

        except Exception as e:
            raise NetworkSecurityException(e,sys)

        
