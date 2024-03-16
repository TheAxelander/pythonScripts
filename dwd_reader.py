from helpers import helper_influx
from datetime import datetime
from decimal import Decimal
from typing import Tuple, Optional
import requests
from influxdb_client import Point


# Station 10513 02667 Köln/Bonn
DWD_SOURCE = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/subdaily/standard_format/kl_10513_00_akt.txt"


class DwdRecord:
    def __init__(self, date: datetime, sun_hours: Decimal):
        self.date = date
        self.sun_hours = sun_hours


def is_null_or_whitespace(s):
    # Check if the string is None or only contains whitespace
    return s is None or s.strip() == ''


def try_create(line_input: str) -> Tuple[bool, Optional[DwdRecord]]:
    year = line_input[7:11]
    month = line_input[11:13]
    day = line_input[13:15]

    date = datetime(year=int(year), month=int(month), day=int(day))

    sun_hours1 = line_input[195:197]
    sun_hours2 = line_input[197:198]
    if is_null_or_whitespace(sun_hours1):
        sun_hours1 = '0'
    if sun_hours1 == '-9':  # Error code from Station
        return False, None

    sun_hours = f'{sun_hours1.strip()}.{sun_hours2}'

    return True, DwdRecord(date=date, sun_hours=Decimal(sun_hours))


def get_station_data(url, start_year):
    stations_data = []
    response = requests.get(url)
    for line in response.iter_lines(decode_unicode=True):
        if is_null_or_whitespace(line):
            return stations_data

        year = line[7:11]
        if int(year) < start_year:
            continue  # Skip the old stuff

        success, new_dwd_record = try_create(line)
        if success:
            print(f'{new_dwd_record.date.strftime("%Y-%m-%d")}: {new_dwd_record.sun_hours}')
        else:
            print(f'Station Error Code')
        stations_data.append(new_dwd_record)

    return stations_data


def write_to_influx(data: list[DwdRecord], bucket):
    points = []
    measurement = 'dwd'

    for item in data:
        points.append(Point(measurement)
                      .time(time=item.date, write_precision='s')
                      .field(field='sunhours', value=item.sun_hours))

    helper_influx.flush_measurement(bucket=bucket, measurement=measurement)
    helper_influx.write_measurement(bucket=bucket, points=points)


if __name__ == '__main__':
    station_data = get_station_data(DWD_SOURCE, start_year=2022)
    write_to_influx(station_data, 'solar')
