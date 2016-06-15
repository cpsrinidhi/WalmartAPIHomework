import urllib
import requests
import sys
# Taking the input string
if len(sys.argv) == 1:
    print "Please pass the search string as a command line argument"
    exit()

search_query = " ".join(sys.argv[1:])
#api key for the account cpsrinidhi@gmail.com
api_key= "4yd5s9tps4yff7uw6ty6k2c9"

data = {'query': search_query, 'apiKey': api_key, 'format': 'json'}

res = requests.get("http://api.walmartlabs.com/v1/search?"+urllib.urlencode(data))
# if HTTP response is not 200 
if res.status_code != 200:
    print "Please try running the app with different search query"
#Converting to JSON format
res_json = res.json()

items = res_json['items']
# no items returned
if len(items) == 0:
    print "No items found for the search term", search_query, "Please try running the app with different search query"
# Getting the first product 
req_item = items[0]

req_product_id = req_item['itemId']


rec_data = { 'apiKey': api_key, 'itemId': req_product_id }
# Get requests from product recommendation API
rec_res = requests.get("http://api.walmartlabs.com/v1/nbp?"+urllib.urlencode(rec_data))

if rec_res.status_code != 200:
    print "Error in recommendation API. Please try running the app with different search query"

rec_json = rec_res.json()

i = 0
# Array for storing the reviews
product_reviews = []

for rec_prod in rec_json:
    if i == 10:
        break

    rec_item_id = rec_prod['itemId']
    rec_item_name = rec_prod['name']
    rev_data = { 'apiKey': api_key, 'format': 'json' }

    rev_res = requests.get("http://api.walmartlabs.com/v1/reviews/"+str(rec_item_id)+"?"+urllib.urlencode(rev_data))

    i+=1

    if rev_res.status_code != 200:
        print "Error with reviews API for product id", rec_item_id
        continue

    rev_json = rev_res.json()

    reviews = rev_json['reviews']

    reviews_sentiment = [int(t['overallRating']['rating']) for t in reviews]
#Calculating the average reviews
    avg_reviews = 0
    if len(reviews_sentiment) != 0:
        avg_reviews = float(sum(reviews_sentiment))/len(reviews_sentiment) 


    product_reviews.append((rec_item_id, rec_item_name, avg_reviews))

#Sorting the average reviews
product_reviews = sorted(product_reviews, key=lambda x: x[2], reverse=True)

print "The recommended products for your query", search_query, "are:"
# Displaying the recommendations
for i in range(len(product_reviews)):
    print i+1, product_reviews[i][1]
