import os
from loguru import logger

from dotenv import load_dotenv
load_dotenv()

class APIConfigurations:
    title = os.getenv("API_TITLE", "batch_serve")
    description = os.getenv("API_DESCRIPTION", "Batch serve using fastapi and postgres")
    version = os.getenv("API_VERSION", "0.1")

class ModelConfigurations:
    model_filepath = os.getenv("MODEL_FILEPATH")
    label_filepath = os.getenv("LABEL_FILEPATH")

class DBConfigurations:
    database = os.getenv("DATABASE")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")


logger.info(f"{APIConfigurations.__name__}: \n{APIConfigurations.__dict__}")
logger.info(f"{ModelConfigurations.__name__}: \n{ModelConfigurations.__dict__}")