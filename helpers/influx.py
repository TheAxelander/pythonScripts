from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

# InfluxDB 2.0 credentials and details
INFLUXDB_URL = 'your_influxdb_url'
INFLUXDB_TOKEN = 'your_influxdb_token'
INFLUXDB_ORG = 'your_influxdb_org'
INFLUXDB_BUCKET = 'your_influxdb_bucket'


def get_influx_client() -> InfluxDBClient:
    return InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)


def write_measurement(bucket, points):
    print('Write Measurement to Influx')

    client = get_influx_client()
    write_api = client.write_api(write_options=SYNCHRONOUS)

    for point in points:
        write_api.write(bucket=bucket, org=INFLUXDB_ORG, record=point)

    client.close()


def flush_measurement(bucket, measurement):
    client = get_influx_client()
    delete_api = client.delete_api()

    delete_api.delete(
        start=datetime(year=1900, month=1, day=1),
        stop=datetime.now(),
        predicate=f'_measurement="{measurement}"',
        bucket=bucket,
        org=INFLUXDB_ORG)
