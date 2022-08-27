# 14. Power of Four
# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.
 
# Example 1:
# Input: n = 16
# Output: true

# Example 2:
# Input: n = 5
# Output: false

# Example 3:
# Input: n = 1
# Output: true



def my(num):
    if num==0:
        return False
    while num!=1:
        if num%4!=0:
            return False
        num=num//4
    return True
print(my(28))
print(my(16))
print(my(1))






        
