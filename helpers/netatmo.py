import lnetatmo


def get_basis_station():
    print('Get Basis Station data')

    authorization = lnetatmo.ClientAuth(clientId="65f5885d85b257b06d028a38",
                                        clientSecret="rmc5CLXNCIEN3zniKKElkuqx8XSuKOLPHaQO")
    weather_data = lnetatmo.WeatherStationData(authorization)

    basis = weather_data.lastData()['Netatmo Basis']
    outdoor = weather_data.lastData()['Outdoor Module']
    alex_buero = weather_data.lastData()['Innenmodul Alex Büro']
    rain = weather_data.lastData()['Regenmesser']

    print(f'Basis: {basis["Temperature"]}')
    print(f'Alex Büro: {alex_buero["Temperature"]}')
    print(f'Garten: {outdoor["Temperature"]}')
    print(f'Regen (24h): {rain["sum_rain_24"]}')


if __name__ == '__main__':
    get_basis_station()
