# import random
# from random import randint
from check_last_digit import produce_last_digit

def upc_generate(start, end, com_upc="885306"):
    # random.seed(seed)
    upc_list = []
    # first_p = randint(0, 4)
    # maf = "40410"

    # # Fix the first 6 digits
    # # First 6-digit for a manufacturer
    # com_upc = "885306"
    for i in range(start, end):
        # last_ps = str(randint(start, end))
        last_5 = str(i)
        if(len(last_5)<=5):
            # upc = first_p + maf + "0"*(6 - len(last_ps))
            upc = com_upc + "0"*(5 - len(last_5)) + last_5
            upc = upc + produce_last_digit(upc)
            upc_list.append(upc)
    # for _ in range(num_upc):
    #     upc = str(randint(start, end))
    #     if(len(upc)<12):
    #         upc = "0"*(12 - len(upc)) + upc
    #     upc_list.append(upc)
    return upc_list
