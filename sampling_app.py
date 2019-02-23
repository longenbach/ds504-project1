import time
import json

import crawler as cl
from genupc import upc_sampling

# Add your API Key here
API_KEY1 = ""
API_KEY2 = ""
API_KEY3 = ""

COMPANY_UPC = "885306"

# create a instance of crawler using apikey
wal1    = cl.Walcrawl(API_KEY1)
wal2    = cl.Walcrawl(API_KEY2)
wal3    = cl.Walcrawl(API_KEY3)

results = []

# store all the UPC candidates
# fix: number of digits to be fixed
# random_proportion: sampling percentage of population
upc_list = upc_sampling(fix=3, com_upc=COMPANY_UPC, random_proportion=0.1, seed=1)


for i in range(len(upc_list)):
    # make sure you won't run out queries per day (5000/day)
    # if(i>=5000):
    #     # break
    if(i%5 == 0):
        time.sleep(1.5)
    # search for a product with upc
    # parameter upc should be string with 12 digits
    if(i<5000):
        results.append(wal1.upc_search(upc_list[i]))
    elif(5000<=i<10000):
        results.append(wal2.upc_search(upc_list[i]))
    else: # In case the query list has more than 10,000 elements
        results.append(wal3.upc_search(upc_list[i]))

# save the variable "results" which is a list of dictionaries
timestr = time.strftime("%Y%m%d-%H%M%S")
file_name = "./sampling_results/" + COMPANY_UPC + timestr + "sampling.json"
with open(file_name, "w") as f:
    json.dump(results, f)
