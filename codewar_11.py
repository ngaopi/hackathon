# You are given two sorted arrays that both only contain integers. Your task is to find a way to merge them into a single one, sorted in asc order. Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

# You don't need to worry about validation, since arr1 and arr2 must be arrays with 0 or more Integers. If both arr1 and arr2 are empty, then just return an empty array.

def merge_arrays(arr1,arr2):
    l=[]
    arr1.extend(arr2)
    arr1.sort()
    i=0
    while i<len(arr1):
        if arr1[i] not in l:
            l.append(arr1[i])
        i=i+1
    return l