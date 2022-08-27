# Write a function to split a string and convert it into an array of words.
# Examples (Input -> Output):
# * "Robin Singh" ==> ["Robin", "Singh"]
# * "I love arrays they are my favorite" ==> ["I", "love", "you"]
def func(a):
    if len(a)<1:
        return['']
    else:
        i=0
        b=[]
        s=''
        while i<len(a):
            if a[i]==" ":
                b.append(s)
                s=''
            else:
                s=a+a[i]
            i=i+1
    if s:
        b.append(s)
    return b



