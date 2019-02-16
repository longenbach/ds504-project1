import random
from random import randint

def upc_generate(num_upc, start, end, seed=3):
    random.seed(seed)
    upc_list = []
    for _ in range(num_upc):
        upc = str(randint(start, end))
        if(len(upc)<12):
            upc = "0"*(12 - len(upc)) + upc
        upc_list.append(upc)
    return upc_list
