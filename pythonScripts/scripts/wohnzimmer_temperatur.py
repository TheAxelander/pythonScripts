from pythonScripts.helpers import helper_netatmo, helper_redis, helper_telegram

REDIS_RUNNING = "dotnet-scripts:wohnzimmer-temperatur-running"
REDIS_COOLDOWN = "dotnet-scripts:wohnzimmer-temperatur-cooldown"


def check_temperature():
    redis = helper_redis.get_redis_database()

    cooldown = int(redis.get(REDIS_COOLDOWN))
    if cooldown > 0:
        cooldown -= 1
        redis.set(name=REDIS_COOLDOWN, value=cooldown)
        print(f'Cooldown, {cooldown} iterations remaining.')
        return

    running = redis.get(REDIS_RUNNING) == 'true'
    basis_station = helper_netatmo.get_station_data('Netatmo Basis')
    temperature = float(basis_station['Temperature'])
    print(f'Basis: {basis_station["Temperature"]}')

    if temperature >= 23.5 and not running:
        helper_telegram.send_message('Temperatur im Wohnzimmer ist über 23,5°C')
        redis.set(name=REDIS_RUNNING, value='true')
        return

    if temperature <= 23.5 and running:
        helper_telegram.send_message('Temperatur im Wohnzimmer ist wieder unter 23,5°C')
        redis.set(name=REDIS_RUNNING, value='false')
        redis.set(name=REDIS_COOLDOWN, value=5)
        return
