import json
import sys
import pickle

from genupc import upc_sampling

iteration = int(sys.argv[1])
INTERVAL_NUM = 100
INTERVAL_SAMPLING_NUM = 10
FIX = 3


result_list = []

for i in range(iteration):
    # Load all ground truth upc into a list
    with open("GT_upc_list", "rb") as f:
        gt = pickle.load(f)

    num_valid_upc = 0

    sampling_upc_list = upc_sampling(fix=FIX, com_upc="885306", seed=i, interval_num=INTERVAL_NUM, interval_sampling_num=INTERVAL_SAMPLING_NUM)

    for upc in sampling_upc_list:
        if(upc in gt):
            num_valid_upc += 1

    i_est = num_valid_upc/(INTERVAL_SAMPLING_NUM/INTERVAL_NUM)
    result_list.append(i_est)

print(sum(result_list)/len(result_list))
