import pandas as pd
from capstoneDE.generate_ids import generate_ids

payment_id_list = []
orders_df = pd.read_csv('../csv_folders/orders.csv')


for i in range(750):
    payment_id = generate_ids()
    payment_id_list.append(payment_id)

#paymentDate, price_paid will come from SQL
payments_df = pd.DataFrame(data=payment_id_list, columns=['payment_id'])
payments_df['customer_id'] = orders_df['customer_id']


payments_table = payments_df.to_csv('../csv_folders/payments.csv', index=False)
print(payments_df)