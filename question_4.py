# Problem Code: TYRE
# There are N bikes and M cars on the road.
# Each bike has 2 tyres.
# Each car has 4 tyres.
# Find the total number of tyres on the road.
# Input Format
# The first line will contain T - the number of test cases. Then the test cases follow.
# The first and only line of each test case contains two integers N,M.
# Output Format
# For each test case, output in a single line, the total number of tyres on the road.
# Sample Input 1 
# 2 1
# 3 0
 
# Sample Output 1 
# 8
# 6
# Explanation
# Test Case 1: There are 2 bikes and 1 car. Each bike has 2 tires, so there are 2⋅2=4 bike tyres. Similarly, each car has 4 tires, so there are 1⋅4=4 car tires. Adding the tires of all vehicles, we get 4+4=8 tires in total.
# Test Case 2: There are 3 bikes and 0 cars. Each bike has 2 tires, so there are 3⋅2=6 bike tyres. There are no cars, so there are 0⋅4=0 car tires. Adding the tires of all vehicles, we get 6+0=6 tyres in total.
def my(cars,bikes):
        b=cars*4
        print(b)
        c=bikes*2
        print(c)
        print("cars+bikes=",b+c)
my(1,2)
my(0,3)

    
    