import redis
from helpers import helper_env

USERNAME = 'redis-username'
PASSWORD = 'redis-password'
SERVER = 'redis-server'


def get_redis_database():
    env_content = helper_env.get_env_file_content()

    server = env_content.get(SERVER)
    username = env_content.get(USERNAME)
    password = env_content.get(PASSWORD)

    return redis.Redis(
        host=server,
        port=6379,
        username=username,
        password=password,
        db=0,
        decode_responses=True)
