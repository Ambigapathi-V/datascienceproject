from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DatavalidationTrainingPipeline
STAGE_NAME = "Data Ingestion Stage"


try:
        logger.info(f">>>>>>{STAGE_NAME} started<<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.initiate_data_ingestion()
        logger.info(f">>>>>>{STAGE_NAME} completed<<<<<<")
except Exception as e:
        logger.error(f">>>>>>Error in {STAGE_NAME}: {str(e)}>>>>>>")
        raise e



STAGE_NAME = "Model evaluation stage"
try:
        logger.info(f">>>>>>{STAGE_NAME} started<<<<<<<")
        obj = DatavalidationTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>>{STAGE_NAME} completed<<<<<<")
except Exception as e:
        logger.error(f">>>>>>Error in {STAGE_NAME}: {str(e)}>>>>>>")
        raise e