import requests
import smtplib
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

OPEN_WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
# CITY = "Calgary,ca"
CITY ="Mumbai,ind"

weather_params = {
    "q": CITY,
    "appid": API_KEY
}


def send_email():
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=TO_EMAIL,
        msg="Subject: Rain Forecast\n\nIt's going to rain today. Remember to bring an umbrella"
    )


response = requests.get(url=OPEN_WEATHER_ENDPOINT, params=weather_params)
response.raise_for_status()

data = response.json()["list"]
will_rain = False

for i in data:
    condition_code = i["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
    send_email()


