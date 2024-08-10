from pythonScripts.helpers import helper_influx, helper_mysql
from influxdb_client import Point
from datetime import datetime, timedelta
import pandas as pd


def copy_day_data(days=3):
    mariadb_engine = helper_mysql.get_mysql_engine('SBFspot')

    start_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=days)
    end_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start_unix_timestamp = int(start_day.timestamp())
    end_unix_timestamp = int(end_day.timestamp())

    sql_query = (f'SELECT * FROM DayData '
                 f'WHERE TimeStamp >= {start_unix_timestamp} AND TimeStamp <= {end_unix_timestamp}')
    data = pd.read_sql_query(sql=sql_query, con=mariadb_engine)

    points = []
    for index, row in data.iterrows():
        print(row)
        points.append(Point('DayData')
                      .time(time=row['TimeStamp'], write_precision='s')
                      .field(field='Power', value=row['Power'])
                      .field(field='TotalYield', value=row['TotalYield'])
                      )

    helper_influx.write_measurement(bucket='solar', points=points)


def copy_month_data(days=3):
    mariadb_engine = helper_mysql.get_mysql_engine('SBFspot')

    start_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=days)
    end_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start_unix_timestamp = int(start_day.timestamp())
    end_unix_timestamp = int(end_day.timestamp())

    sql_query = (f'SELECT * FROM MonthData '
                 f'WHERE TimeStamp >= {start_unix_timestamp} AND TimeStamp <= {end_unix_timestamp}')
    data = pd.read_sql_query(sql=sql_query, con=mariadb_engine)

    points = []
    for index, row in data.iterrows():
        print(row)
        points.append(Point('MonthData')
                      .time(time=row['TimeStamp'], write_precision='s')
                      .field(field='TotalYield', value=row['TotalYield'])
                      .field(field='DayYield', value=row['DayYield'])
                      )

    helper_influx.write_measurement(bucket='solar', points=points)
