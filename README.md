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
netatmo-clientId=myId
netatmo-clientSecret=mySecret
influx-server=http://my.influx.dev:8086
influx-org=my-org
```