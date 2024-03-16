from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
from helpers.helper_redis import get_redis_database
from helpers.helper_env import get_env_file_content


def get_influx_client() -> InfluxDBClient:
    redis = get_redis_database()
    data = redis.hgetall('dotnet-scripts:influxdb')
    url = get_env_file_content()['influx-server']

    return InfluxDBClient(url=url, token='K4IPCsCPTlcDNxFnzy0PJeMvCigoC3QjJsiCc2oLDCAJltByHeRxk98FfQggVZwaphRZcc8Jnx67OJhu8msldg==', org='homelab-dev', timeout=120000)
    # return InfluxDBClient(url=url, token=data['token'], org=data['organization'], timeout=120000)


def write_measurement(bucket, points):
    client = get_influx_client()
    write_api = client.write_api(write_options=SYNCHRONOUS)

    for point in points:
        result = write_api.write(bucket=bucket, org=get_env_file_content()['influx-org'], record=point)

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