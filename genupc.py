import random
from random import randint

def upc_generate(num_upc, start, end, seed=3):
    random.seed(seed)
    upc_list = []
    # first_p = randint(0, 4)
    # maf = "40410"

    # Fix the first 6 digits
    # Try
    com_upc = "885306"
    for _ in range(num_upc):
        last_ps = str(randint(start, end))
        if(len(last_ps)<6):
            # upc = first_p + maf + "0"*(6 - len(last_ps))
            upc = com_upc + "0"*(6 - len(last_ps)) + last_ps
            upc_list.append(upc)
    # for _ in range(num_upc):
    #     upc = str(randint(start, end))
    #     if(len(upc)<12):
    #         upc = "0"*(12 - len(upc)) + upc
    #     upc_list.append(upc)
    return upc_list
