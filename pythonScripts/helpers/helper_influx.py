from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
from pythonScripts.helpers.helper_env import get_env_file_content


def get_influx_client():
    url = get_env_file_content()['influx-server']
    org = get_env_file_content()['influx-org']
    token = get_env_file_content()['influx-token']

    return InfluxDBClient(url=url, token=token, org=org, timeout=120000)


def write_measurement(bucket, points):
    client = get_influx_client()
    write_api = client.write_api(write_options=SYNCHRONOUS)

    for point in points:
        print(f'Write to Influx: [{bucket}] {point}')
        write_api.write(bucket=bucket, org=get_env_file_content()['influx-org'], record=point)

    client.close()


def flush_measurement(bucket, measurement):
    client = get_influx_client()
    delete_api = client.delete_api()

    delete_api.delete(
        start=datetime(year=1900, month=1, day=1),
        stop=datetime.now(),
        predicate=f'_measurement="{measurement}"',
        bucket=bucket,
        org=get_env_file_content()['influx-org'])
