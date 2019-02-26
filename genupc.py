import random
# from random import randint
import math

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

def upc_sampling(fix=3, com_upc="885306", seed=1, interval_num=100, interval_sampling_num=10): #random_proportion=0.1):
    if(interval_sampling_num>interval_num):
        raise ValueError("Number of sampled intervals cannot be greater than total number of intervals")
    if(int(math.pow(10. fix)) % interval_num !=0):
        raise ValueError("Fixed digits space cannot be divided into even intervals")

    upc_list = []
    # fix_sampling_num = int(math.pow(10, fix)*random_proportion)
    # seed = 1
    # for _ in range(fix_sampling_num):
    #     random.seed(seed)
    #     fix_digit = str(randint(0, math.pow(10, fix) - 1))
    #     for i in range(exh_range):
    #         upc = com_upc + "0"*(fix - len(fix_digit)) + fix_digit
    random.seed(seed)
    # fix_digit_list = random.sample(range(int(math.pow(10, fix))), fix_sampling_num)
    interval_sampling_index = random.sample(range(interval_num), interval_sampling_num)
    fix_digit_list = []
    for n in interval_sampling_index:
        fix_digit_list += list(range(n*int(math.pow(10, fix)/interval_num), (n+1)*int(math.pow(10, fix)/interval_num)))
    fix_list = ["0"*(fix - len(str(x))) + str(x) for x in fix_digit_list]
    exh_range = int(math.pow(10, 5 - fix))
    for p in fix_list:
        fix_upc = com_upc + p
        for i in range(exh_range):
            upc = fix_upc + "0"*(5 - fix - len(str(i))) + str(i)
            upc = upc + produce_last_digit(upc)
            upc_list.append(upc)
    return upc_list
