# 8.Car or Bus
# Chef wants to reach home as soon as possible. He has two options:
# Travel with his BIKE which takes X minutes.
# Travel with his CAR which takes Y minutes.
# Which of the two options is faster or do they both take the same time?
# Input Format
# First-line will contain T, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, two integers X, Y representing the time taken to travel with BIKE and CAR respectively.
# Output Format
# For each test case, print CAR if traveling with a car is faster, BIKE if traveling with a Bike is faster, SAME if they both take the same time.
# You may print each character of CAR, BIKE, and SAME in uppercase or lowercase (for example, CAR, Car, cAr will be considered identical).
# Sample Input 1 
# 1 5
# 4 2
# 6 6
# Sample Output 1 
# BIKE
# CAR
# SAME

# Explanation
# Test case-1: Travelling with BIKE takes 1 minute while traveling with CAR takes 5 minutes. So traveling with BIKE is faster.
# Test case-2: Travelling with BIKE takes 4 minutes while traveling with CAR takes 2 minutes. So traveling with CAR is faster.
# Test case-3: Travelling with both BIKE and CAR takes the SAME time i.e. 6 minutes.
def time(car,bike):
    if car<bike:
        print("car travels faster")
    elif car>bike:
        print("bike is faster")
    else:
        print("both are same")
time(1,5)
time(4,2)
time(6,6)
    