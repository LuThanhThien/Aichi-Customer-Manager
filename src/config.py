import os
from dataclasses import dataclass
import pandas as pd
import yaml
from PIL import Image

#PATHS
DATABASE_PATH = r".\database\customers.csv"
SETTING_PATH = r".\database\setting.yml"
X_BUTTON_PATH = r"src\assets\images\x-button.png"

#IMGAES 
X_BUTTON_IMG = Image.open(X_BUTTON_PATH)

#DATA
CUSTOMER_DF = pd.read_csv(DATABASE_PATH)
SEARCH_ENTRIES = ["No."] + CUSTOMER_DF.columns.tolist()   
CUSTOMER_COLUMNS = SEARCH_ENTRIES.copy()
CUSTOMER_COLUMNS_WIDTH = {"No.": 40}
for column in CUSTOMER_COLUMNS[1:]:
    max_len = max(CUSTOMER_DF[column].astype(str).map(len).max(), len(column))
    CUSTOMER_COLUMNS_WIDTH[column] = max_len*3
# this can cause error if database is empty or not containing all kinds of column name
GENDER_OPT = CUSTOMER_DF["Gender"].unique().tolist()
CERT_OPT = CUSTOMER_DF["Certificate Type"].unique().tolist()


# SETTINGS
DATE_FORMAT = r"%Y/%m/%d"
DATE_FORMAT_LIST = [e[-1] for e in DATE_FORMAT.split("/")]
SETTING = yaml.load(open(SETTING_PATH, "r"), Loader=yaml.FullLoader)

#STYLE
FONT = ("Arial", 10)

@dataclass
class DataIngestionConfig:
    """
    This will define the path that data will be saved by data classes
    """
    data_path: str = os.path.join("artifacts")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")


@dataclass
class DataTransformationConfig:
    preprocessor_ob_file_path = os.path.join("artifacts", "preprocessor.pkl")


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")
    model_report_file_path = os.path.join("artifacts", "model_report.pkl")

if __name__ == "__main__":
    # date_list = DATE_FORMAT.split("/")
    # date_list = [e[-1] for e in date_list]
    # print(date_list)
    # print(SETTING)
    pass