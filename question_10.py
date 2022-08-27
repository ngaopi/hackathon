# 10.Counting Pretty Numbers Problem Code: NUM239
# Vasya likes the number 239. Therefore, he considers a number pretty if its last digit is 2, 3 or 9. Vasya wants to watch the numbers between L and R (both inclusive), so he asked you to determine how many pretty numbers are in this range. Can you help him?
# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains two space-separated integers L and R.
# Output
# For each test case, print a single line containing one integer — the number of pretty numbers between L and R.
# Sample Input 1 

# 1 10
# 11 33

# Sample Output 1 
# 3
# 8

# Explanation
# Example case 1: The pretty numbers between 1 and 10 are 2, 3, and 9.
# Example case 2: The pretty numbers between 11 and 33 are 12, 13, 19, 22, 23, 29, 32, and 33.
def my(n,m):
    c=0
    for i in range(n,m):
        x=i%10
        if x==2 or x==3 or x==9:
            c=c+1
    print(c)
my(n=int(input("enter the number:")),m=int(input("enter the number:")))


    

        
            
    