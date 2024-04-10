import lnetatmo


def get_all_station_data():
    authorization = lnetatmo.ClientAuth()
    weather_data = lnetatmo.WeatherStationData(authorization)

    return weather_data.lastData()


def get_station_data(name):
    return get_all_station_data()[name]
