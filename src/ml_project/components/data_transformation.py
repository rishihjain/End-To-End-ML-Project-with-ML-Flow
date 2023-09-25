import os
from ml_project import logging
from sklearn.model_selection import train_test_split
import pandas as pd
from ml_project.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config

    # here i am adding train_test_split bcz the data i slaready cleaned up

    # NOTE : But if needed we can add different data transformation teachniques such as scalar and PCA


    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        #Spliting the data into training and testing sets(75 , 25 ) split

        train , test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"), index = False)
        train.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logging.info("Splitted Data into training and testing sets")
        logging.info(train.shape)
        logging.info(test.shape)

        print(train.shape)
        print(test.shape) 