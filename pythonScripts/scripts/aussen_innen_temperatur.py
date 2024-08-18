from pythonScripts.helpers import helper_netatmo, helper_redis, helper_telegram

REDIS_RUNNING = "python-scripts:aussen-innen-temperatur-running"
REDIS_COOLDOWN = "python-scripts:aussen-innen-temperatur-cooldown"


def check_temperature():
    redis = helper_redis.get_redis_database()

    cooldown = int(redis.get(REDIS_COOLDOWN))
    if cooldown > 0:
        cooldown -= 1
        redis.set(name=REDIS_COOLDOWN, value=cooldown)
        print(f'Cooldown, {cooldown} iterations remaining.')
        return

    running = redis.get(REDIS_RUNNING) == 'true'

    data = helper_netatmo.get_all_station_data()
    basis = data['Netatmo Basis']
    outdoor = data['Outdoor Module']
    office = data['Innenmodul Alex Büro']
    temperature_basis = float(basis['Temperature'])
    temperature_outdoor = float(outdoor['Temperature'])
    temperature_office = float(office['Temperature'])

    print(f'Wohnzimmertemperatur: {temperature_basis}')
    print(f'Bürotemperatur: {temperature_office}')
    print(f'Außentemperatur: {temperature_outdoor}')

    if (temperature_outdoor > temperature_basis or temperature_outdoor > temperature_office) and not running:
        helper_telegram.send_message('Außertemperatur ist höher als Innentemperatur. Schließe die Fenster.')
        redis.set(name=REDIS_RUNNING, value='true')
        return

    if (temperature_outdoor <= temperature_basis or temperature_outdoor <= temperature_office) and running:
        helper_telegram.send_message('Öffne die Fenster. Die Außertemperatur ist niedriger als die Innentemperatur.')
        redis.set(name=REDIS_RUNNING, value='false')
        redis.set(name=REDIS_COOLDOWN, value=5)
        return
