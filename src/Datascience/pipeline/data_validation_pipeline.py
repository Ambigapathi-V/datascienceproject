from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValiadtion
from src.datascience import logger

STAGE_NAME = "Data Validation Stage"

class DatavalidationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(data_validation_config)
        data_validation.validate_all_columns()
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>{STAGE_NAME} started<<<<<<<")
        obj = DatavalidationTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>>{STAGE_NAME} completed<<<<<<")
    except Exception as e:
        logger.error(f">>>>>>Error in {STAGE_NAME}: {str(e)}>>>>>>")
        raise e
