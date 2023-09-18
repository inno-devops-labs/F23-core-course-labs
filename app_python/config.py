import os

from dotenv import load_dotenv

from app_python.templates.templates import SetUpTemplates


class Config:
    load_dotenv()
    server_host = os.getenv("SERVER_HOST")
    server_port = int(os.getenv("SERVER_PORT"))
    templates = SetUpTemplates("app_python/templates")


config = Config()
