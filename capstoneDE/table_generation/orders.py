import pandas as pd
from capstoneDE.generate_ids import generate_ids
from faker import Faker
from datetime import datetime
import random
import csv
import json

f = open('../yelp_quotes.json')
data = json.load(f)
customer_df = pd.read_csv('../csv_folders/customer.csv')



def fake_order_generation(records):
    fake = Faker('en_US')
    orders = []

    for i in range(records):

        orders.append({
            "order_id": generate_ids(),
            "order_date": fake.date_between_dates(date_start=datetime(2022,10,1), date_end=datetime(2022,11,1)),
            "shipped_date": fake.date_between_dates(date_start=datetime(2022,10,2), date_end=datetime(2022,11,30)),
            "status": 'shipped',
            "comments": random.choice(data),
        })

    return orders

f.close()

order_df = pd.DataFrame(fake_order_generation(500))
order_df['comments'] = order_df['comments'].sample(frac=.8).astype(str)
order_df['customer_id'] = customer_df['customer_id'].sample(n=750, replace=True, ignore_index=True)

order_df[['order_date', 'shipped_date']] = order_df[['order_date', 'shipped_date']].astype(str)

orders_table = order_df.to_csv('../csv_folders/orders.csv', index=False)
