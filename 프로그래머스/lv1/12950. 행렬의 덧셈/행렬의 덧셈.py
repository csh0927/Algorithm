import numpy as np
def solution(arr1, arr2):
    ar = np.array(arr1) + np.array(arr2)
    return ar.tolist()