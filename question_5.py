# 5. Chef and Chocolates
# Chef wants to gift C chocolates to Botswal on his birthday. However, he has only X chocolates with him. The cost of 1 chocolate is Y rupees.
# Find the minimum money in rupees Chef needs to spend so that he can gift C chocolates to Botswal.
# Input Format
# First-line will contain T, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, three integers C, X, and Y.
# Output Format
# For each test case, output in a single line answer, the minimum money in rupees Chef needs to spend.
# Sample Input 1 
# 7 5 5
# 10 1 1
# Sample Output 1 
# 10
# 9

# Explanation
# Test Case 1: Chef has to gift a total of 7 chocolates out of which he has 5 chocolates. Thus, Chef needs to buy 2 more chocolates, which costs him 10 rupees.
# Test Case 2: Chef has to gift a total of 10 chocolates out of which he has 1 chocolate. Thus, Chef needs to buy 9 more chocolates, which costs him 9 rupees.
user1=int(input("total of chocolates the chef has to gift:"))
user2=int(input("total of chocolates the chef had:"))
if user1>user2:
    a=user1-user2
    print("total cost of chocolate the chef needs to buy =",a)
    user3=int(input("total cost of one chocolate:"))
    b=a*user3
    print("cost of the chocolate =",b)

