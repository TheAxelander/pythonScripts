# Python Scripts

## Installation

Download [latest release](https://github.com/TheAxelander/pythonScripts/releases/latest) and install it via `pipx`

``` bash
apt install python3 python3-pipx
pipx install ./pythonScripts-x.x.x-py3-none-any.whl
```

Optionally create a venv for development

``` bash
git clone https://github.com/TheAxelander/pythonScripts.git
cd pythonScripts
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Requires an `.env` file in `~/.config./python-scripts/` folder

```
redis-server=my.redis.dev
redis-username=myuser
redis-password=mypassword
influx-server=http://my.influx.dev:8086
influx-org=my-org
mariadb-server=my.mariadb.dev
```

Netatmo requires a credential file `~/.netatmo.credentials`

> Due to Netatmo continuous changes, the credential file is the recommended method for production use as the refresh token will be frequently refreshed and this file MUST be writable by the library to keep a usable refresh token.

``` json
{
    "CLIENT_ID" : "myId",
    "CLIENT_SECRET" : "mySecret",
    "REFRESH_TOKEN" : "myRefresh|Token"
}
```