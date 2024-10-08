import argparse
from pythonScripts.scripts import aussen_innen_temperatur, dwd_reader, netatmo_influxdb, sbfspot_influxdb, wohnzimmer_temperatur


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('script', type=str, help="Script which should be executed")

    parser.add_argument('-d', '--days', type=int, default=None, help="How many days (optional)")

    args = parser.parse_args()
    match args.script:
        case "aussen_innen":
            aussen_innen_temperatur.check_temperature()
        case "dwd":
            station_data = dwd_reader.get_station_data(dwd_reader.DWD_SOURCE, start_year=2022)
            dwd_reader.write_to_influx(station_data, 'solar')
        case "netatmo_influx":
            netatmo_influxdb.write_station_data()
        case "sbfspot_influx":
            days = args.days
            if days is None:
                sbfspot_influxdb.copy_day_data()
                sbfspot_influxdb.copy_month_data()
            else:
                sbfspot_influxdb.copy_day_data(days)
                sbfspot_influxdb.copy_month_data(days)
        case "wohnzimmer_temp":
            wohnzimmer_temperatur.check_temperature()
        case _:
            pass


if __name__ == '__main__':
    main()
