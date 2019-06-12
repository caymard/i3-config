import requests

STATUS = {"off": {"message": "🔴"}, "starting": {"message": "🔺"}, "running": {"message": "🔵"}}

try:
    r = requests.get("http://clement.citymeo.lan/api/management/v2/", timeout=1)
except requests.exceptions.ConnectionError:
    status = "off"
else:
    if r.status_code == 502:
        status = "starting"
    elif r.status_code == 403:
        status = "running"
    else:
        status = "off"
finally:
    print(STATUS[status]["message"])
