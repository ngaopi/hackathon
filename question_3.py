# Problem (Problem Code: FBC, fill the buckets)
# Chef has a bucket having a capacity of K liters. It is already filled with X liters of water.Find the maximum amount of extra water in liters that Chef can fill in the bucket without overflowing.
# Input Format
# The first line will contain T - the number of test cases. Then the test cases follow.
# The first and only line of each test case contains two space-separated integers K and X - as mentioned in the problem.
# Output Format
# For each test case, output in a single line, the amount of extra water in liters that Chef can fill in the bucket without overflowing.
# Sample Input 1 
# 5 4
# 15 6
# Sample Output 1 
# 1
# 9
 
# Explanation
# Test Case 1: The capacity of the bucket is 5 liters but it is already filled with 4 liters of water. Adding 1 more liter of water to the bucket fills it to (4+1)=5 liters. If we try to fill more water, it will overflow.
# Test Case 2: The capacity of the bucket is 15 liters but it is already filled with 6 liters of water. Adding 9 more liters of water to the bucket fills it to (6+9)=15 liters. If we try to fill more water, it will overflow.


def my(capacity,filled):
    user=int(input("enter the amount to be filled:"))
    if user>1:
        print("water will overflow")
    else:
        print("water is filled")
my(5,4)
    
    
    
    

    
    