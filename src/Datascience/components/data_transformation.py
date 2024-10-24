import os 
from src.datascience import logger
from sklearn.model_selection import train_test_split
from src.datascience.entity.config_entity import DataTransformationConfig
import pandas as pd


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        
        # Split the data into training and test sets
        train ,test = train_test_split(data)
        
        # Create  training and test sets
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"))
        
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"))
        
        # Logging
        logger.info(f"Training and test sets created successfully at {self.config.root_dir}")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)
        