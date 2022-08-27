# 13. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]
# list=[0,1,0,3,12]
# i=0
# b=[]
# c=[]
# while i<len(list):
#     if list[i]==0:
#         b.append(list[i])
#     else:
#         c.append(list[i])
#     i=i+1
# c.extend(b)
# print(c)

def fun(list):
    i=0
    c=0
    while i<len(list):
        j=0
        while j<len(list):
            if list[j]==0:
                if list[i]>list[j]:
                    c=list[j]
                    list[j]=list[i]
                    list[i]=c
            j=j+1
        i=i+1
    return list
print(fun([0,1,0,3,12]))
print(fun([1,9,8,4,0,0,2,7,0,6,0,9]))            