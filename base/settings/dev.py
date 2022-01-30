# Settings for Development stage
from . base import *
from decouple import config
import redis


class DatabaseOperations():
    
    def redis_connection():
        client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
        return client