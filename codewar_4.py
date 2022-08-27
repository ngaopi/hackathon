
# Output
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# None of the arrays will be empty, so you don't have to worry about that!
def func(a):
    i=0
    b=[]
    while i<len(a):
        a.append(a[i])
        i=i+2
    return a
func(["keep","remove","keep","remove","keep","remove"])
    