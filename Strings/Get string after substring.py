my_string = "hello python world , i'm a beginner "
print (my_string.split("world , ",1)[1])

# Find first part and return slice before it.
str = 'feature/CKBICHDSKK-8595\nYour branch'
ch = "\n"
pos_ch = str.find(ch)
if pos_ch == -1: 
    print("")
print(str[0:pos_ch])