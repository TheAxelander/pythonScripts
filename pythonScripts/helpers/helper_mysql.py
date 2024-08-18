from sqlalchemy import create_engine
from pythonScripts.helpers.helper_env import get_env_file_content


def get_mysql_engine(database):
    url = get_env_file_content()['mariadb-server']
    user = get_env_file_content()['mariadb-user']
    password = get_env_file_content()['mariadb-password']

    return create_engine(f'mysql+pymysql://{user}:{password}@{url}/{database}')
