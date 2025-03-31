import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df = dataset
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Days'] = (df['Order Date'] - df['Order Date'].min()).dt.days
X = df[['Days']]
y = df['Sales']
model = LinearRegression().fit(X, y)
forecast = model.predict(X)
plt.scatter(df['Order Date'], y, color='blue', label='Actual')
plt.plot(df['Order Date'], forecast, color='red', label='Forecast')
plt.legend()
plt.title('Sales Forecast')
plt.show()