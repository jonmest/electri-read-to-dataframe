import os
import pandas as pd
import requests

ELECTRI_API_KEY = os.environ.get('API_KEY')
URL = "https://electri.p.rapidapi.com/api/v1/day-ahead-prices"

querystring = {
    "to": "2022-05-05T22:00Z",
    "from": "2022-04-05T22:00Z",
    "eic": "10Y1001A1001A46L"
}

headers = {
    "X-RapidAPI-Key": ELECTRI_API_KEY,
    "X-RapidAPI-Host": "electri.p.rapidapi.com"
}

if __name__ == "__main__":
    response = requests.request("GET", URL, headers=headers, params=querystring)
    df = pd.DataFrame(response.json()["data"]["series"])
    print(df)
