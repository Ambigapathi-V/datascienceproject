from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        try:   
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status = f.read().split(" ")[-1]
            
            if status == "True":
                logger.info(f">>>>>>{STAGE_NAME} started<<<<<<<")
                
                # Load the dataset
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                logger.info(f"Skipping {STAGE_NAME} as data validation failed.")
                raise Exception("Your data scheme is not valid " )
            
            
        except Exception as e:
             logger.error(f"Error occurred while running {STAGE_NAME} pipeline: {e}")
             raise e