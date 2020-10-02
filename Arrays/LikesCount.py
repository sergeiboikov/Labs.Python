def likes1(names):
    result = ""
    n = len(names)
    if (n == 0):
        result = "no one likes this"
    elif (n == 1):
        result = "{} likes this".format(names[0])
    elif (n == 2):
        result = "{} and {} like this".format(*names[:2])
    elif (n == 3):
        result = "{}, {} and {} like this".format(*names[:3])
    else:
        result = "{}, {} and {others} others like this".format(*names[:2], others=n-2)
    return result

#2 variant
def likes2(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

print (likes1(["John", "Kim"]))
print (likes2(["John", "Kim", "Alex"]))

n = {
    0: 'no one likes this',
    1: '{} likes this', 
    2: '{} and {} like this', 
    3: '{}, {} and {} like this', 
    4: '{}, {} and {others} others like this'
    }
print(n[1])