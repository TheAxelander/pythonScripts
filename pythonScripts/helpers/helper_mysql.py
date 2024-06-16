from sqlalchemy import create_engine
from pythonScripts.helpers.helper_redis import get_redis_database
from pythonScripts.helpers.helper_env import get_env_file_content


def get_mysql_engine(database):
    redis = get_redis_database()
    data = redis.hgetall('dotnet-scripts:mariadb')
    url = get_env_file_content()['mariadb-server']

    return create_engine(f'mysql+pymysql://{data["user"]}:{data["password"]}@{url}/{database}')
