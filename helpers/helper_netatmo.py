import lnetatmo
from helpers.helper_env import get_env_file_content


def get_all_station_data():
    client_id = get_env_file_content()['netatmo-clientId']
    client_secret = get_env_file_content()['netatmo-clientSecret']

    authorization = lnetatmo.ClientAuth(clientId=client_id, clientSecret=client_secret)
    weather_data = lnetatmo.WeatherStationData(authorization)

    return weather_data.lastData()


def get_station_data(name):
    return get_all_station_data()[name]


if __name__ == '__main__':
    get_all_station_data()
