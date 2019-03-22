from datetime import datetime

import requests
import pytz
from dateutil.parser import parse

from settings import FOOTBALL_DATA_API_KEY


FR_TZ = pytz.timezone("Europe/Paris")
NOW = datetime.now(FR_TZ)


def format_fixture(fixture, score=True):
    if score:
        return "{} {}-{} {}".format(
            fixture.get("homeTeamName"),
            fixture.get("result").get("goalsHomeTeam") or 0,
            fixture.get("result").get("goalsAwayTeam") or 0,
            fixture.get("awayTeamName"),
        )
    return "{} - {}".format(fixture.get("homeTeamName"), fixture.get("awayTeamName"))


def seconds_to_countdown(seconds):
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60
    if seconds > seconds_in_day:
        count = int(seconds / seconds_in_day)
        letter = "J"
    elif seconds > seconds_in_hour:
        count = int(seconds / seconds_in_hour)
        letter = "H"
    else:
        count = int(seconds / seconds_in_minute)
        letter = "M"
    return "{}-{}".format(letter, count)


def main():

    if FOOTBALL_DATA_API_KEY is None:
        raise ValueError("FOOTBALL_DATA_API_KEY is None, stopping here.")

    request = requests.get(
        "http://api.football-data.org/v1/competitions/467/fixtures",
        headers={"X-Auth-Token": FOOTBALL_DATA_API_KEY},
    )
    fixtures = request.json().get("fixtures")
    for fixture in fixtures:
        if fixture.get("status") == "FINISHED":
            pass
        elif fixture.get("status") == "IN_PLAY":
            print(format_fixture(fixture))
            break
        else:
            starting_at = parse(fixture.get("date"))
            print(
                seconds_to_countdown((starting_at - NOW).seconds),
                format_fixture(fixture, score=False),
            )
            break


if __name__ == "__main__":
    main()
