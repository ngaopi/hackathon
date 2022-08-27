# Implement a function which multiplies two numbers.
# def func(a,b):
#     c=a*b
#     return c
# print(func(2,2))
    


def func(n):
    i=0
    c=0
    while i<len(n):
        if n[i]%2!=0:
            c=c+1
        i=i+1
    return c
print(func([1,2,3,4,5,6,7,9]))
    