from environs import Env

config = Env()
config.read_env()

PORT: str = config("PORT")
HOST: str = config("HOST")
SQL_URL: str = config("SQL_URL")
REDIS_URL: str = config("REDIS_URL")
EMAIL: str = config("EMAIL")
EMAIL_PASS: str = config("EMAIL_PASS")
VERIFY_ENDPOINT: str = config("VERIFY_ENDPOINT")
SITE_NAME: str = config("SITE_NAME")
