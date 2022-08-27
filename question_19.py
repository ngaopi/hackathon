# 19. Adding and removing dots
# Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".
# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".
def my(list):
    i=0
    b=[]
    while i<len(list):
        c=".".join(list[i])
        b.append(c)
        i=i+1
    return b
print(my(["test"]))
