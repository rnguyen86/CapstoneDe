import pandas as pd
from faker import Faker
from capstoneDE.generate_ids import generate_ids

# columns I need:
# “firstname”, “lastname”, “street address”, “city”, “state”, “zip”, “phone”, and “email_address”


def fake_data_generation(records):
    fake = Faker('en_US')

    customers = []

    for i in range(records):
        first_name = fake.first_name()
        last_name = fake.last_name()

        customers.append({
            "customer_id": generate_ids(),
            "first_name": first_name,
            "last_name": last_name,
            "phone": fake.phone_number(),
            "email": str.lower(f"{first_name}.{last_name}@fake_domain.com"),
            "address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state_abbr(),
            "zip": fake.postcode(),
            "country": fake.country_code()
        })

    return customers


customer_df = pd.DataFrame(fake_data_generation(500))
customer_table = customer_df.to_csv('../csv_folders/customer.csv',index=False)


