from dataclasses import dataclass
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import pandas as pd
import numpy as np

"""
In this file we store the output of the each file we strore means at the end of the file
what the output it gives 
"""

@dataclass
class DataIngestionArtifacts:
    trained_file_path : str
    test_file_path : str

@dataclass
class DataValidationArtifacts:
    validaion_status : bool
    valid_train_file_path : str
    valid_test_file_path : str
    invalid_train_file_path : str
    invalid_test_file_path : str
    drift_report_file_path : str

@dataclass
class DataTransformationArtifacts:
    transformed_object_file_path : str
    transformed_train_file_path : str
    transformed_test_file_path : str

@dataclass
class ClassificationMetricArtifacts:
    f1_score : float
    precision_score : float
    recall_score : float

@dataclass
class ModelTrainerArtifacts:
    trained_model_file_path : str
    train_metric_artifacts : ClassificationMetricArtifacts
    test_metric_artifacts : ClassificationMetricArtifacts
