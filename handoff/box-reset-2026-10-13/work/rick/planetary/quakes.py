"""Planetary View step 1: USGS earthquakes (public domain) -> summary JSON. No person-level data."""
import json, sys, urllib.request
URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
def summarize(fc):
    ev = [f for f in fc["features"] if f["properties"].get("mag") is not None]
    ev.sort(key=lambda f: -f["properties"]["mag"])
    return {"count": len(ev), "max_mag": ev[0]["properties"]["mag"] if ev else None,
            "top5": [{"mag": f["properties"]["mag"], "place": f["properties"]["place"],
                      "lon": f["geometry"]["coordinates"][0], "lat": f["geometry"]["coordinates"][1],
                      "time_ms": f["properties"]["time"]} for f in ev[:5]], "source": URL}
if __name__ == "__main__":
    fc = json.load(urllib.request.urlopen(URL, timeout=20))
    json.dump(summarize(fc), sys.stdout, indent=1)
