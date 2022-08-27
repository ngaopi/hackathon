# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.\
# If the input is an empty array or is null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
def count_positives_sum_negatives(arr):
    if len(arr)>0:
        sum=0
        count=0
        i=0
        while i<len(arr):
            if arr[i]>0:
                count+=1
            elif arr[i]<0:
                sum=sum+arr[i]
            i=i+1
            a=[count,sum]
    else:
        a=[]
    return a
arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
count_positives_sum_negatives(arr)      