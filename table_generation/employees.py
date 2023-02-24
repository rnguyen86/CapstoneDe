import random
from capstoneDE.generate_ids import generate_ids
import pandas as pd
from faker import Faker


sales_jobs = ['account representative', 'account executive', 'sales consultant', 'salesperson']
marketing_jobs = ['marketing assistant', 'brand ambassador', 'content specialist', 'SEO specialist', 'social media manager']
it_jobs = ['solutions architect', 'web developer', 'data engineer', 'network engineer', 'service desk engineer']
analyst_jobs = ['data analyst', 'business intelligence analyst', 'R&D', 'consultant']
bd_jobs = ['accountant', 'project manager', 'human resources', 'business analyst']

def fake_employee_generation(records):
    fake = Faker('en_US')

    employees = []

    for i in range(records):
        first_name = fake.first_name()
        last_name = fake.last_name()

        employees.append({
            "employee_id": generate_ids(),
            "first_name": first_name,
            "last_name": last_name,
            "email": str.lower(f"{first_name}.{last_name}@fake_domain.com"),
            "department_no": random.randint(1001, 1005)
        })

    return employees


def decide_job(row):

    if row['department_no'] == 1001:
        return random.choice(sales_jobs)
    elif row['department_no'] == 1002:
        return random.choice(marketing_jobs)
    elif row['department_no'] == 1003:
        return random.choice(it_jobs)
    elif row['department_no'] == 1004:
        return random.choice(bd_jobs)
    elif row['department_no'] == 1005:
        return random.choice(analyst_jobs)


employees_df = pd.DataFrame(fake_employee_generation(200))
employees_df['job_title'] = employees_df.apply(lambda row: decide_job(row), axis=1)

employees_csv = employees_df.to_csv('../csv_folders/employees.csv', index=False)

print(employees_df)