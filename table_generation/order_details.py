import pandas as pd
import numpy as np

orders_df = pd.read_csv('../csv_folders/orders.csv')
products_df = pd.read_csv('../csv_folders/product_table.csv')

# order_id, product_id, quantity_ordered, price_paid

order_details_df = pd.DataFrame(columns=['order_id', 'product_id', 'quantity_ordered', 'price_paid'])

order_details_df['order_id'] = orders_df['order_id']

order_details_df['product_id'] = products_df['product_id'].sample(n=750, replace=True, ignore_index=True)

order_details_df['quantity_ordered'] = np.random.randint(1, 10, size=len(order_details_df))

order_details_table = order_details_df.to_csv('../csv_folders/order_details.csv', index=False)