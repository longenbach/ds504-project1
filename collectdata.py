import time
import json

import crawler as cl
from genupc import upc_generate

# Add your API Key here
API_KEY = ""
# # Choose the number of candidate upc you want to query, max = 5000/day
# UPC_NUM = 4500
# Choose the range of UPC's last 6 digits
START = 1
END = 1000000
# Fix the first 6 digits which is the manufacturer
COMPANY_UPC = "885306"


# create a instance of crawler using apikey
wal = cl.Walcrawl(API_KEY)

results = []

# store all the UPC candidates
# upc_list = []
upc_list = upc_generate(START, END, COMPANY_UPC)


for i in range(len(upc_list)):
    # make sure you won't run out queries per day (5000/day)
    if(i>=4500):
        break
    if(i%5 == 0):
        time.sleep(1.5)
    # search for a product with upc
    # parameter upc should be string with 12 digits
    results.append(wal.upc_search(upc_list[i]))

# If you run the code locally, change the code below
# save the variable "results" which is a list of dictionaries
# print(results)
timestr = time.strftime("%Y%m%d-%H%M%S")
file_name = timestr + "results.json"
with open(file_name, "w") as f:
    json.dump(results, f)
