# Python Scripts

## Installation

``` bash
apt install python3 python3-pip
git clone https://github.com/TheAxelander/pythonScripts.git
cd pythonScripts
pip install -r requirements.txt
```

Optionally create a venv for development

``` bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Requires an `.env` file in project root folder

```
redis-server=my.redis.dev
redis-username=myuser
redis-password=mypassword
influx-server=http://my.influx.dev:8086
influx-org=my-org
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