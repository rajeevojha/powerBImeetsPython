import pandas as pd
import matplotlib.pyplot as plt
df = dataset
df['Order Date'] = pd.to_datetime(df['Order Date'])
customer_sales = df.groupby(['Customer Name', df['Order Date'].dt.to_period('M')])['Sales'].sum().unstack()
customer_sales.plot(kind='line', title='Customer Sales Trends')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend(title='Customer', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()