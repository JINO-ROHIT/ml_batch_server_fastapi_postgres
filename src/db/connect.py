import psycopg2
from loguru import logger
from configs.configurations import DBConfigurations

# conn = psycopg2.connect(
#     database = DBConfigurations.database,
#     user = DBConfigurations.user,
#     password = DBConfigurations.password,
#     host = DBConfigurations.host
# )

conn = psycopg2.connect(
    database="sample_db",
    user="jino",
    password="jino",
    host="postgres"
)

logger.info("DB Connection established")