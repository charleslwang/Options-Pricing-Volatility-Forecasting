import pandas as pd
from arch import arch_model

cleaned_data_file = "data/clean_data.csv"

cleaned_data = pd.read_csv(cleaned_data_file)

cleaned_data['Date'] = pd.to_datetime(cleaned_data['Date'])

cleaned_data.set_index('Date', inplace=True)

returns = cleaned_data['Close'].pct_change().dropna()

model = arch_model(returns, vol='Garch', p=1, q=1)

results = model.fit()

n_days = 10
forecast = results.forecast(start=returns.index[-1], horizon=n_days)

forecasted_volatility = forecast.variance.values[-1, :]

print("Forecasted Volatility for the Next", n_days, "Days:")
for i in range(n_days):
    print(f"Day {i+1}: {forecasted_volatility[i]:.6f}")
