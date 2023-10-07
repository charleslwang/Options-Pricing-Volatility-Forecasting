import pandas as pd
from arch import arch_model
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error, mean_absolute_error

# implement GARCH model to predict near-future volatility

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

# implement validation techniques

mse_scores = []
mae_scores = []

n_splits = 5 # folds for cross-validation

tscv = TimeSeriesSplit(n_splits=n_splits)

for train_index, test_index in tscv.split(returns):
    train_data = returns.iloc[train_index]
    test_data = returns.iloc[test_index]

    # fit the GARCH model for each fold
    model = arch_model(train_data, vol='Garch', p=1, q=1)
    results = model.fit()

    # forecast volatility for the test period
    forecast = results.forecast(start=test_data.index[0], horizon=len(test_data))
    forecasted_volatility = forecast.variance.values[-1, :]

    # calculating Mean Squared Error
    mse = mean_squared_error(test_data, forecasted_volatility)
    mse_scores.append(mse)

    # calculating mean absolute error
    mae = mean_absolute_error(test_data, forecasted_volatility)
    mae_scores.append(mae)

average_mse = sum(mse_scores) / len(mse_scores)
average_mae = sum(mae_scores) / len(mae_scores)
