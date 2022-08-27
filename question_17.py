# 17. Capital indexes
# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
def capital_indexes(list):
    i=0
    b=[]
    while i<len(list):
        if list[i].isupper():
            # b.append(list[i])
            b.append(i)
        i=i+1
    return b
print(capital_indexes("HeLlO"))





        
                
                
            
    