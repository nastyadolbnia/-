import pandas as pd
import numpy as np

df = pd.read_excel('C:\\Users\\dolbnya\\Desktop\\test\\weekly_1.xlsx', header = 0)
df.columns = df.columns.astype(str).str.strip()


# Создаем пустые списки для заказов каждого грузовика
truck1_orders = []
truck2_orders = []

# Создаем счетчики для количества поездок каждого грузовика в каждую смену
truck1_morning_trips = 0
truck1_afternoon_trips = 0
truck2_evening_trips = 0

# Распределяем заказы по грузовикам
for index, order in df.iterrows():
    if pd.notna(order['delivery_shift']):
        if order['delivery_shift'] == 'M' and sum(order['volume'] for order in truck1_orders) + order['volume'] <= 1400 and truck1_morning_trips < 2:
            truck1_orders.append(order)
            truck1_morning_trips += 1
        elif order['delivery_shift'] == 'N' and sum(order['volume'] for order in truck1_orders) + order['volume'] <= 1400 and truck1_afternoon_trips < 2:
            truck1_orders.append(order)
            truck1_afternoon_trips += 1
        elif order['delivery_shift'] == 'E' and sum(order['volume'] for order in truck2_orders) + order['volume'] <= 1400 and truck2_evening_trips < 1:
            truck2_orders.append(order)
            truck2_evening_trips += 1
# Если грузовики не полностью заполнены, добавляем оставшиеся заказы
remaining_orders = df[~df.index.isin([order.name for order in truck1_orders + truck2_orders])]
for index, order in remaining_orders.iterrows():
    if sum(order['volume'] for order in truck1_orders) + order['volume'] <= 1400:
        truck1_orders.append(order)
    elif sum(order['volume'] for order in truck2_orders) + order['volume'] <= 1400:
        truck2_orders.append(order)

# Выводим заказы для каждого грузовика
print("Заказы для грузовика 1:", truck1_orders)
print("Заказы для грузовика 2:", truck2_orders)

# Преобразуем списки обратно в DataFrame
df_truck1_orders = pd.DataFrame(truck1_orders)
df_truck2_orders = pd.DataFrame(truck2_orders)

# Сохраняем DataFrame в файлы Excel
#df_truck1_orders.to_excel('truck1_orders.xlsx', index=False)
#df_truck2_orders.to_excel('truck2_orders.xlsx', index=False)