import json
import sys
import pickle
import time
from os import listdir

from genupc import upc_sampling

def sampling(iteration_time=10, interval_num=100, interval_sampling_num=10, fix_digit_num=3):
    if(fix_digit_num>5):
        raise ValueError("Fixed digits number cannot be greater than 5")

    param_dic = {"number of iteration": iteration_time, "total number of intervals": interval_num, \
                "number of sampled intervals":interval_sampling_num, "number of fixed digits": fix_digit_num}
    start = time.time()

    ITERATION = iteration_time
    INTERVAL_NUM = interval_num
    INTERVAL_SAMPLING_NUM = interval_sampling_num
    FIX = fix_digit_num

    result_list = []

    for i in range(ITERATION):
        # Load all ground truth upc into a list
        with open("GT_upc_list", "rb") as f:
            gt = pickle.load(f)

        num_valid_upc = 0
        try:
            sampling_upc_list = upc_sampling(fix=FIX, com_upc="885306", seed=i, interval_num=INTERVAL_NUM, interval_sampling_num=INTERVAL_SAMPLING_NUM)
        except ValueError as error:
            print("Error Message: ", repr(error))

        for upc in sampling_upc_list:
            if(upc in gt):
                num_valid_upc += 1

        i_est = num_valid_upc/(INTERVAL_SAMPLING_NUM/INTERVAL_NUM)
        result_list.append(i_est)

    estimator = sum(result_list)/len(result_list)
    param_dic["estimator"] = estimator

    end = time.time()
    param_dic["running time"] = end - start


    return param_dic

if __name__ == "__main__":
    FILENAME = "test_param_result.json"
    file_list = listdir()
    if(FILENAME in file_list):
        with open(FILENAME, "r") as l:
            data = json.load(l)
    else:
        data = []
    try:
        test = sampling(10, 100, 10, 3)
        data.append(test)
        with open(FILENAME, "w") as w:
            json.dump(data, w)
    except ValueError as error:
        print("Error Message: ", repr(error))
