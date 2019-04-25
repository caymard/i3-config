#!/env/bin/python3
import requests

if __name__ == "__main__":

    r = requests.get(
        "http://www.meteofrance.com/mf3-rpc-portlet/rest/pluie/312540"
    )
    data = r.json()

    rain_data = [
        datacadran.get("niveauPluie") for datacadran in data.get("dataCadran")
    ]
    it_will_rain = [i for i in rain_data if i > 1] != []
    rain_histogram = [
        {
            1: "▁",
            2: "▃",
            3: "▄",
            4: "▅",
            5: "█"
        }.get(rd, "X") for rd in rain_data
    ]

    umbrella = "☔" if it_will_rain else "🌂"
    print(umbrella + "".join(rain_histogram))
