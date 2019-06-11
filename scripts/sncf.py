from datetime import datetime
import sys

import requests

from settings import SNCF_API_KEY


API_URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas/{}/departures"
INNOPOLE_ID = "stop_area:OCE:SA:87612002"
RESULTS_MAX = 2


def valid_departure(departure, date):
    return date.split("T")[0] == departure.split("T")[0]


def main():
    today = datetime.now().strftime("%Y%m%dT%H%M%S")
    payload = {"q": today}

    r = requests.get(
        API_URL.format(INNOPOLE_ID),
        data=payload,
        auth=requests.auth.HTTPBasicAuth(SNCF_API_KEY, ""),
    )

    data = r.json()

    pretty_dates = []
    for departure in data.get("departures"):
        direction = departure.get("display_informations").get("direction")
        departure_date_time = departure.get("stop_date_time").get("departure_date_time")
        departure_datetime = datetime.strptime(departure_date_time, "%Y%m%dT%H%M%S")
        base_departure_date_time = departure.get("stop_date_time").get("base_departure_date_time")
        base_departure_datetime = datetime.strptime(base_departure_date_time, "%Y%m%dT%H%M%S")

        if not valid_departure(departure_date_time, today):
            continue
        if not "Toulouse" in departure.get("display_informations").get("direction"):
            continue
        pretty_date = departure_datetime.strftime("%H:%M")
        pretty_late = "(+{})".format((departure_datetime - base_departure_datetime).seconds)
        pretty_dates.append(pretty_date + pretty_late)
        sys.stderr.write("{} : {}\n".format(direction, pretty_date))
        if len(pretty_dates) >= RESULTS_MAX:
            break

    sys.stdout.write(" ".join(pretty_dates) + "\n")


if __name__ == "__main__":
    main()
