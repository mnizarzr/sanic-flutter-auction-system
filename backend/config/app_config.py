import os


class AppConfig:
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = os.getenv("REDIS_PORT", 6379)
    REDIS_DB = os.getenv("REDIS_DB", 0)
    REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/?db={REDIS_DB}'

    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_USER = os.getenv("MONGO_USER", "root")
    MONGO_PWD = os.getenv("MONGO_PWD", "root")
    MONGO_PORT = os.getenv("MONGO_PORT", 27017)
    MONGO_DB = os.getenv("MONGO_DB", "test")

    MONGO_URL = f'mongodb://{MONGO_USER}:{MONGO_PWD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?retryWrites=true&w=majority'
    MOTOR_URI = MONGO_URL
