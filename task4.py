"""
Есть Pandas DataFrame со столбцами [“customer_id”, “product_id”, “timestamp”], который содержит данные по просмотрам товаров на сайте. Есть проблема – просмотры одного customer_id не разбиты на сессии (появления на сайте). Мы хотим разместить сессии так, чтобы сессией считались все смежные просмотры, между которыми не более 3 минут.

Написать методом который создаст в Pandas DataFrame столбец session_id и проставит в нем уникальный int id для каждой сессии.

У каждого пользователя может быть по несколько сессий. Исходный DataFrame может быть большим – до 100 млн строк.
"""

import pandas as pd
import random

session_interval_sec = 180


def get_rnd_int_from_interval(start=0, end=10):
    return random.randint(start, end)


def mark_rows_by_session_id(df):
    df["session_id"] = 0
    sorted_df = df.sort_values(['customer_id', 'product_id', 'timestamp'], ascending=[True, True, True])

    product = []
    timestamp = 0
    uniq_id = 0

    for i, row in sorted_df.iterrows():
        crt_product, crt_timestamp = [row["customer_id"], row["product_id"]], row["timestamp"]
        if product:
            if crt_product != product:
                uniq_id += 1
                product = crt_product
                timestamp = crt_timestamp
            elif crt_timestamp - session_interval_sec > timestamp:
                uniq_id += 1
            sorted_df.at[i, 'session_id'] = uniq_id
        else:
            product = crt_product
            timestamp = crt_timestamp

    return sorted_df


dataframe = pd.DataFrame({
    'customer_id': [get_rnd_int_from_interval(end=3) for _ in range(30)],
    'product_id': [get_rnd_int_from_interval(end=3) for _ in range(30)],
    'timestamp': [get_rnd_int_from_interval(end=300) for _ in range(30)]
})

print(mark_rows_by_session_id(dataframe))
