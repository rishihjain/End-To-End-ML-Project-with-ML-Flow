from src.ml_project import logging
from ml_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ml_project.pipeline.stage_02_data_validation import DataValidationTraningPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise e

STAGE_NAME = "Data Validation Stage"

try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTraningPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise e