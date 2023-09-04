import os


class Config:
    host = os.getenv("SERVER_HOST")
    port = int(os.getenv("SERVER_PORT"))


config = Config()
