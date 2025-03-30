import pandas as pd
import matplotlib.pyplot as plt
df = dataset  # Power BI auto-provides this from the Fields you dragged
df['Order Date'] = pd.to_datetime(df['Order Date'])  # Ensure date format
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
monthly_sales.plot(kind='line', title='Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show() #- Power BI renders it automatically