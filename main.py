from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DatavalidationTrainingPipeline
from src.datascience.pipeline.data_transfromation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline


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
        data_validation = DatavalidationTrainingPipeline()
        data_validation.initiate_data_ingestion()
        logger.info(f">>>>>>{STAGE_NAME} completed<<<<<<")
except Exception as e:
        logger.error(f">>>>>>Error in {STAGE_NAME}: {str(e)}>>>>>>")
        raise e

STAGE_NAME = "Data Transformation stage"
try:
        logger.info(f">>>>>>{STAGE_NAME} started<<<<<<<")
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.initiate_data_transformation()
        logger.info(f">>>>>>{STAGE_NAME} completed<<<<<<")
except Exception as e:
        logger.error(f">>>>>>Error in {STAGE_NAME}: {str(e)}>>>>>>")
        raise e

STAGE_NAME = "Model  Trainer stage"


try:
        logger.info(f">>>>>>{STAGE_NAME} started<<<<<<<")
        modeltrainer = ModelTrainerTrainingPipeline()
        modeltrainer.initiate_model_training()
        logger.info(f">>>>>>{STAGE_NAME} completed<<<<<<")
except Exception as e:
        logger.error(f">>>>>>Error in {STAGE_NAME}: {str(e)}>>>>>>")
        raise e