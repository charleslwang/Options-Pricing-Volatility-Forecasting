import os
import requests
import pandas as pd

api_key = '2W2V6KD5XK9OXX0M'

endpoint = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "IBM",
    "outputsize": "compact",
    "apikey": api_key,
}

response = requests.get(endpoint, params=params)

if response.status_code == 200:
    data = response.json()

    daily_prices = data.get("Time Series (Daily)")

    df = pd.DataFrame.from_dict(daily_prices, orient="index")

    df.reset_index(inplace=True)
    df.columns = ["Date", "Open", "High", "Low", "Close", "Volume", "Dividend", "Split"]

    output_file = os.path.join("data", "raw_data.csv")

    df.to_csv(output_file, index=False)

    print("Data saved to raw_data.csv")
else:
    print("API failed.", response.status_code)
