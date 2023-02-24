import requests
import json
from yelp_api_key import YELP_KEY
from yelp_api_location import loc_ids

MY_API_KEY = YELP_KEY
HEADERS = {'Authorization': 'bearer %s' % MY_API_KEY}
PARAMETERS = {'locale': 'en_US'
              }
#calling each business IDs and extracting 3 reviews
comments = []
for id in loc_ids:
    response = requests.get(url='https://api.yelp.com/v3/businesses/'+ id +'/reviews',
                             params=PARAMETERS,
                             headers=HEADERS)
    business_data = response.json()
    data = business_data['reviews']
    for x in data:
        quotes = (x['text'])
        comments.append(quotes)


#saving the reviews to a json file
f = open ('yelp_quotes.json', 'w')
f.write (json.dumps (reviews, indent=3))
f.close ()


