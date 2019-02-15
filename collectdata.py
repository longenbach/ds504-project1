import time

import crawler as cl

# Add your API Key here
API_KEY = ""

# create a instance of crawler using apikey
wal = cl.Walcrawl(API_KEY)

results = []

# store all the UPC candidates
upc_list = []

'''
Construct a UPC generator based on different purpose
Add the generated UPC to the upc_list
'''


for i in range(len(upc_list)):
    if(i>=4500):
        break
    if(i%5 == 0):
        time.sleep(1.5)
    # search for a product with upc
    # parameter upc should be string with 12 digits
    results.append(wal.upc_search(upc_list[i]))

# If you run the code locally, change the code below
# save the variable "results" which is a list of dictionaries
print(results)
