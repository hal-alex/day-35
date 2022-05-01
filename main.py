import requests

api_key = "81e7df4979af95e9bf4a2d51e4f0576b"

parameters = {
    "lat": 51.5072,
    "lon": 0.1276,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 900:
        will_rain = True


if will_rain:
    print("Bring an umbrella.")

# print(data["hourly"][0]["weather"][0]["id"])



