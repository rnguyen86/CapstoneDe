import pandas as pd

department_data = [{'department_no': '1001',
                    'department_name': 'sales',
                    'department_manager': 'Rich Win'},
                   {'department_no': '1002',
                    'department_name': 'marketing',
                    'department_manager': 'Joe Doe'},
                   {'department_no': '1003',
                    'department_name': 'IT',
                    'department_manager': 'Mike Jordan'},
                   {'department_no': '1004',
                    'department_name': 'business development',
                    'department_manager': 'Nyjah Huston'},
                   {'department_no': '1005',
                    'department_name': 'analytics',
                    'department_manager': 'James Beard'}
                   ]

department_df = pd.DataFrame(department_data)
department_table = department_df.to_csv('../csv_folders/departments.csv', index=False)