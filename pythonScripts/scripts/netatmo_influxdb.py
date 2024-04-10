from pythonScripts.helpers import helper_netatmo, helper_influx
from influxdb_client import Point
from datetime import datetime, timezone


def write_station_data():
    data = helper_netatmo.get_all_station_data()

    influx = helper_influx.get_influx_client()
    points = []

    basis = data['Netatmo Basis']
    outdoor = data['Outdoor Module']
    alex_buero = data['Innenmodul Alex Büro']
    rain = data['Regenmesser']
    time = datetime.now(timezone.utc)

    points.append(Point('basis')
                  .time(time=time, write_precision='s')
                  .field(field='CO2', value=basis['CO2'])
                  .field(field='Humidity', value=basis['Humidity'])
                  .field(field='Noise', value=float(basis['Noise']))
                  .field(field='Pressure', value=float(basis['Pressure']))
                  .field(field='Temperature', value=float(basis['Temperature']))
                  )
    points.append(Point('aussenmodul')
                  .time(time=time, write_precision='s')
                  .field(field='Humidity', value=outdoor['Humidity'])
                  .field(field='Temperature', value=float(outdoor['Temperature']))
                  )
    points.append(Point('innenmodul_alex_buero')
                  .time(time=time, write_precision='s')
                  .field(field='CO2', value=alex_buero['CO2'])
                  .field(field='Humidity', value=alex_buero['Humidity'])
                  .field(field='Temperature', value=float(alex_buero['Temperature']))
                  )
    points.append(Point('regenmesser')
                  .time(time=time, write_precision='s')
                  .field(field='Rain', value=float(rain['Rain']))
                  .field(field='sum_rain_1', value=float(rain['sum_rain_1']))
                  .field(field='sum_rain_24', value=float(rain['sum_rain_24']))

                  )

    helper_influx.write_measurement(bucket='netatmo', points=points)
