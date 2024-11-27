import pandas as pd


file_path = 'comptagevelo2010.csv'
data = pd.read_csv(file_path)

data_cleaned = data.drop(columns=['Unnamed: 1'], errors='ignore')

data_cleaned['Date'] = pd.to_datetime(data_cleaned['Date'], format='%d/%m/%Y', errors='coerce')

data_cleaned['Month'] = data_cleaned['Date'].dt.month

monthly_usage = data_cleaned.groupby('Month').sum(numeric_only=True)

most_popular_month = monthly_usage.sum(axis=1).idxmax()
print(f"Найпопулярніший місяць: {most_popular_month} (загальна кількість проїздів: {monthly_usage.sum(axis=1)[most_popular_month]:,.0f})")

print("\nКількість проїздів за місяцями:")
print(monthly_usage.sum(axis=1))
