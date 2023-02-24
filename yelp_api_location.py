import requests

# Define a business ID
# Define API Key, Search Type, and header
MY_API_KEY = 'WspvpJMsPlCo2m_bYmh2q3ODy3DwvNK7J41c8r32J4Jx7YEDbwMNlY9dHqiHuF6qIsgOoRXR3DlULSrTBnrgmaMYvH8IUnNNrO98IVa058IrWE4ODCusUx-CF0ZyY3Yx'
BUSINESS_PATH = f'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % MY_API_KEY}

# Define the Parameters of the search
PARAMETERS = {'locale':'en_US',
              'term': 'snowboard shop',
              'limit': 50,
              'radius': 40000,
              'location': 'colorado'
              }

response = requests.get(url=BUSINESS_PATH,
                        params=PARAMETERS,
                        headers=HEADERS)

# Convert response to a JSON String

business_data = response.json()

loc_busi = business_data['businesses'][:]

#saving each business ID to a list
loc_ids = []
for links in loc_busi:
    loc_ids.append(links['id'])

print(loc_ids)