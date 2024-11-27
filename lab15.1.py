import pandas as pd

passenger_baggage = {
    1: (3, 50),
    2: (1, 20),
    3: (2, 45),
    4: (4, 55),
    5: (5, 30),
    6: (1, 15),
    7: (2, 40),
    8: (3, 60),
    9: (1, 24),
    10: (2, 25)
}

df = pd.DataFrame.from_dict(
    passenger_baggage,
    orient='index',
    columns=['Кількість речей', 'Вага багажу (кг)']
).reset_index().rename(columns={"index": "Номер пасажира"})

print("Датафрейм:")
print(df)

# Виконання агрегації: підрахунок загальної кількості речей і ваги
agg_data = df.agg({
    'Кількість речей': ['sum', 'mean'],
    'Вага багажу (кг)': ['sum', 'mean']
})

print("\nАгреговані дані:")
print(agg_data)

# Групування даних за кількістю речей (групи з однаковою кількістю)
grouped_data = df.groupby('Кількість речей').agg({
    'Вага багажу (кг)': ['sum', 'mean'],
    'Номер пасажира': 'count'
}).rename(columns={'count': 'Кількість пасажирів'})

print("\nГруповані дані:")
print(grouped_data)
