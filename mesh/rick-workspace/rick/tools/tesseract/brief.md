# Tessera whole-picture brief (5D)
- earthquake: 245 events, max severity 0.96
- wildfires: 193 events, max severity 0.50
- weather-alert: 10 events, max severity 0.70
- weather-now: 8 events, max severity 0.10
- severeStorms: 7 events, max severity 0.50
## Top salient (severity)
- M 6.7 - central Mid-Atlantic Ridge [https://earthquake.usgs.gov/earthquakes/eventpage/us6000u1z5]
- M 6.1 - 17 km W of Río Grande, Panama [https://earthquake.usgs.gov/earthquakes/eventpage/us6000u1wn]
- M 5.4 - Mid-Indian Ridge [https://earthquake.usgs.gov/earthquakes/eventpage/us6000u1rh]
- M 5.1 - 119 km SSW of Gambiran Satu, Indonesia [https://earthquake.usgs.gov/earthquakes/eventpage/us6000u1ye]
- M 4.9 - 17 km W of Río Grande, Panama [https://earthquake.usgs.gov/earthquakes/eventpage/us6000u1ww]
- M 4.9 - 283 km SSW of Severo-Kuril’sk, Russia [https://earthquake.usgs.gov/earthquakes/eventpage/us6000u1sn]
- Flood Warning issued October 12 at 10:33PM CDT until October 13 at 11:00PM CDT by NWS Mobile AL [https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.83e8512db1b8fc55b3d8b421a208ce7f1598dd5b.001.1]
- Flood Warning issued October 12 at 9:21PM CDT until October 17 at 7:00PM CDT by NWS Lake Charles LA [https://api.weather.gov/alerts/urn:oid:2.49.0.1.840.0.8c39b0a475d4541f891e248563cc28d2eb7d8526.003.1]
## Regions (10° cells, busiest)
- cell 30,-110: 73
- cell 40,-110: 56
- cell 30,-120: 42
- cell 30,-100: 34
- cell 30,-90: 34
## Possibility axis (quake count cone)
- global quake count p50 2026-10-12: 22.0
- global quake count p50 2026-10-13: 22.0
- global quake count p50 2026-10-14: 22.0
## Anomalies: 10 anomalous days in 364-day history (robust z>3.5)
## Mesh bus (latest)
- rick→tessera: celestrak: {"total": 16693, "by_orbit": {"LEO": 15881, "MEO": 183, "HEO": 45, "GEO": 584}}
- rick→tessera: kp: {"latest_kp": 3.33, "max_kp": 7.0, "storm_periods_kp5plus": 3}
- rick→tessera: meteo: 8 events in 589 ms; top: 20.5°C wind 12.8 km/h; 26.2°C wind 8.1 km/h; 13.8°C wind 6.5 km/h
- rick→tessera: usgs: 245 events in 97 ms; top: M 6.7 - central Mid-Atlantic Ridge; M 6.1 - 17 km W of Río Grande, Panama;
## Memory graph: 115 nodes, 1717 edges; top: repo:TESSERA, module:rick/src, repo:gitbook-cordnation, repo:rea-batch, repo:rick