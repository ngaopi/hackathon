# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#  Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

# def my(num1,num2):
#     a=num1*num2
#     print(a) 
# my(123,456)
def func():
    num1=input("enter the number1:")
    num2=input("enter the number2:")
    multiply=int(num1)*int(num2)
    b=str(multiply)
    # print("multiplication of number is:"+repr(b))
    print("multiplication of number is:"+"'"+b+"'")
func()