import pandas as pd
from capstoneDE.web_scrape import webscrape_product_data


product_url_list = ['https://www.evo.com/shop/snowboard/bags/new',
                    'https://www.evo.com/shop/snowboard/bindings/new',
                    'https://www.evo.com/shop/snowboard/tuning-tools',
                    'https://www.evo.com/shop/snowboard/boots/new',
                    'https://www.evo.com/shop/snowboard/facemasks/new',
                    'https://www.evo.com/shop/snowboard/goggles/new',
                    'https://www.evo.com/shop/snowboard/helmets/new',
                    'https://www.evo.com/shop/snowboard/jackets/new',
                    'https://www.evo.com/shop/snowboard/pants/mens/womens/new',
                    'https://www.evo.com/shop/snowboard/snowboards/boys',
                    'https://www.evo.com/shop/snowboard/snowboards/girls',
                    'https://www.evo.com/shop/snowboard/snowboards/kids',
                    'https://www.evo.com/shop/snowboard/snowboards/womens/new']


def create_product_df(data_list):

    df = pd.DataFrame(data=data_list,
                      columns=['product_id','product_type','product_name','product_price','stock_quantity'])
    df['product_price'] = df['product_price'].str.replace('$', '')
    df[['product_type', 'product_name', 'product_price']] = df[['product_type', 'product_name', 'product_price']]. \
        apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    return df


product_df = create_product_df(webscrape_product_data(product_url_list))

product_table = product_df.to_csv('../csv_folders/product_table.csv', index=False)
