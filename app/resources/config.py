from environs import Env

config = Env()
config.read_env()

PORT: str = config("PORT")
HOST: str = config("HOST")
SQL_URL: str = config("SQL_URL")
REDIS_URL: str = config("REDIS_URL")
RENEW_PASSWORD_LINK: str = config("RENEW_PASSWORD_LINK")
EMAIL: str = config("EMAIL")
EMAIL_PASS: str = config("EMAIL_PASS")
SITE_NAME: str = config("SITE_NAME")
REDIRECT_LINK: str = config("REDIRECT_LINK")
ORIGINS: str = config("ORIGINS")
