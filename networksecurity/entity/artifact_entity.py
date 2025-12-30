from dataclasses import dataclass
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import pandas as pd
import numpy as np


@dataclass
class DataIngestionArtifacts:
    trained_file_path : str
    test_file_path : str
