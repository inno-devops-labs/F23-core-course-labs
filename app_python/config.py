class Config:
    SECRET_KEY = "my_secret_key"
    TEMPLATES_FOLDER = "../templates"
    STATIC_FOLDER = "../static"
    TEMPLATES_AUTO_RELOAD = False
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass
