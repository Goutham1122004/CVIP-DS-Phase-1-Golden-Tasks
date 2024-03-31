import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

data = pd.read_csv("portfolio_data.csv")
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

plt.figure(figsize=(12, 8))
for column in data.columns:
    plt.plot(data.index, data[column], label=column)
plt.title('Stock Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

plt.figure(figsize=(12, 8))
for i, column in enumerate(data.columns):
    decomposition = seasonal_decompose(data[column], model='additive', period=1)
    plt.subplot(len(data.columns), 1, i+1)
    plt.plot(decomposition.trend, label='Trend')
    plt.plot(decomposition.seasonal, label='Seasonal')
    plt.plot(decomposition.resid, label='Residual')
    plt.title(f'Decomposition of {column}')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
plt.tight_layout()
plt.show()
