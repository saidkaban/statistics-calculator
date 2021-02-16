import numpy as np

def mean(np_array):
    return [np.mean(np_array, axis=0).tolist(), np.mean(np_array, axis=1).tolist(), np.mean(np_array.reshape(-1)).tolist()]

def variance(np_array):
    return [np.var(np_array, axis=0).tolist(), np.var(np_array, axis=1).tolist(), np.var(np_array.reshape(-1)).tolist()]

def standard_dev(np_array):
    return [np.std(np_array, axis=0).tolist(), np.std(np_array, axis=1).tolist(), np.std(np_array.reshape(-1)).tolist()]

def max_func(np_array):
    return [np.amax(np_array, axis=0).tolist(), np.amax(np_array, axis=1).tolist(), max(np_array.reshape(-1)).tolist()]

def min_func(np_array):
    return [np.amin(np_array, axis=0).tolist(), np.amin(np_array, axis=1).tolist(), min(np_array.reshape(-1)).tolist()]

def sum_func(np_array):
    return [np.sum(np_array, axis=0).tolist(), np.sum(np_array, axis=1).tolist(), np.sum(np_array.reshape(-1)).tolist()]

def calculate(some_list):
    if len(some_list) != 9:
        raise ValueError("List must contain nine numbers.")
    list_np = np.array(some_list).reshape(3, 3)
    calc_list = ["mean", "variance", "standard deviation", "max", "min", "sum"]
    func_list = [mean, variance, standard_dev, max_func, min_func, sum_func]
    calculations = {}

    for i in range(6):
        calculations["{}".format(calc_list[i])] = func_list[i](list_np)
    return calculations

calculate([2,6,2,8,4,0,1,5,7])
