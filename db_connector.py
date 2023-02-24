from sqlalchemy import create_engine
import pandas as pd


def table_to_upload(file_path):

    file_to_upload_df = pd.read_csv(file_path)
    return file_to_upload_df


connection = create_engine('mysql+pymysql://admin:Rdsadmin1@capstone-de.cbtdydcbqz9b.us-east-2.rds.amazonaws.com/snowboard_haus',
                           echo=False)

upload_df = table_to_upload('../capstoneDE/csv_folders/payments.csv')

upload_df.to_sql('payments', con=connection, if_exists='append', index=False)



