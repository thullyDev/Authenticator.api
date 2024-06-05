from environs import Env

config = Env()
config.read_env()

PORT: str = config("PORT")
HOST: str = config("HOST")
REDIS_URL: str = config("REDIS_URL")