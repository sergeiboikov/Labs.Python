line = '13-Mar,42.242,-73.527,1,42.38,-73.384,1,42.426,-73.343,1,22.426,-73.348,1'
print (line)
date = line.split(',')[0]
_l = line.split(',')[1::3]
_a = line.split(',')[2::3]
_c = line.split(',')[3::3]
print (date)
print (_l)
print (_a)
print (_c)
print (len(_l))
print (len(_a))
print (len(_c))