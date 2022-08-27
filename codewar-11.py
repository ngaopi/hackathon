# Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]
def maps(a):
    i=0
    b=[]
    while i<len(a):
        d=a[i]+a[i]
        b.append(d)
    i=i+1
    return b
maps([1,2,3,4,5])
