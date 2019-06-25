#!/env/bin/python3
import requests

from settings import OWM_KEY

if __name__ == "__main__":

    r = requests.get(
        "http://api.openweathermap.org/data/2.5/weather",
        params={"q": "Labège,fr", "units": "metric", "appid": OWM_KEY},
    )
    data = r.json()
    temp = round(data.get("main").get("temp"))

    r = requests.get("http://www.meteofrance.com/mf3-rpc-portlet/rest/pluie/312540")
    data = r.json()

    rain_data = [datacadran.get("niveauPluie") for datacadran in data.get("dataCadran")]
    it_will_rain = [i for i in rain_data if i > 1] != []
    rain_histogram = [{1: "▁", 2: "▃", 3: "▄", 4: "▅", 5: "█"}.get(rd, "?") for rd in rain_data]

    umbrella = "☔" if it_will_rain else "🌂"
    print("{}°C {}{}".format(temp, umbrella, "".join(rain_histogram)))
