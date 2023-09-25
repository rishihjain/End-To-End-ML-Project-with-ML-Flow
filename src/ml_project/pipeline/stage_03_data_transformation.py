from ml_project.config.configuration import ConfigurationManager
from ml_project.components.data_transformation import DataTransformation
from ml_project import logging
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTraningPipeline:
    def __init__(self):
        pass

    def main(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status = f.read().split(" ")[-1]
            
            if status == "True":
                 config = ConfigurationManager()
                 data_transformation_config = config.get_data_transformation_config()
                 data_transformation = DataTransformation(config=data_transformation_config)
                 data_transformation.train_test_splitting()

            else:
                raise Exception("Your data schema is not valid")

        except Exception as e:
            print(e)

       

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTraningPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e