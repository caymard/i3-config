#!/env/bin/python3
import requests
import redis

if __name__ == "__main__":
    red = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
    rain_cursor = int(red.get("rain_cursor"))
    rain_city = red.lindex("rain_index", rain_cursor)
    rain_code = red.hget("rain_" + rain_city, "code")
    rain_label = red.hget("rain_" + rain_city, "label")

    r = requests.get(
        "http://www.meteofrance.com/mf3-rpc-portlet/rest/pluie/" + rain_code
    )
    data = r.json()

    rain_histogram = [rain_label]
    for dc in data.get("dataCadran"):
        np = dc.get("niveauPluie")
        rain_histogram.append({1: " ", 2: "▁", 3: "▃", 4: "▅", 5: "█"}.get(np, "X"))

    red.set("rain_cursor", (rain_cursor + 1) % red.llen("rain_index"))

    print("".join(rain_histogram))
