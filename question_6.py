# 6.Janmansh and Assignment
# Janmansh has to submit 3 assignments for Chingari before 10 pm and he starts to do the assignments at X pm. Each assignment takes him 1 hour to complete. Can you tell whether he'll be able to complete all assignments on time or not?
# Input Format
# The first line will contain T - the number of test cases. Then the test cases follow.
# The first and only line of each test case contains one integer X - the time when Janmansh starts doing the assignments.
# Output Format
# For each test case, output Yes if he can complete the assignments on time. Otherwise, output No.
# You may print each character of Yes and No in uppercase or lowercase (for example, yes, yEs, YES will be considered identical).
# Sample Input 1 
# 7
# 9
# Sample Output 1 
# Yes
# No

# Explanation
# Test case-1: He can start at 7 pm and finish by 10 pm. Therefore he can complete the assignments.
# Test case-2: He can not complete all the 3 assignments if he starts at 9 pm
def assignment(x):
    number_of_assign=3
    assignment_time=1
    if 10==x+(number_of_assign*assignment_time):
        print("yes")
    else:
        print("no")
assignment(7)
assignment(9)