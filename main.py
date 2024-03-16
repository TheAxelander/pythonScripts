# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from helpers import helper_netatmo


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    data = helper_netatmo.get_all_station_data()

    basis = data['Netatmo Basis']
    outdoor = data['Outdoor Module']
    alex_buero = data['Innenmodul Alex Büro']
    rain = data['Regenmesser']

    print(f'Basis: {basis["Temperature"]}')
    print(f'Alex Büro: {alex_buero["Temperature"]}')
    print(f'Garten: {outdoor["Temperature"]}')
    print(f'Regen (24h): {rain["sum_rain_24"]}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
