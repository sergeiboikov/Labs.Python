import itertools as it
status = None
date = None
new_lines = []
header = ['Status', 'Date', 'Longitude', 'Attitude', 'Count']

with open('C:\GIT\Labs.Python\TransformCsv\CoordStatusMA_Short.csv', mode='r', encoding='cp1252') as f:
    for line in f.readlines():
        if line.startswith('Status='):
            status_line = line.split(',')[0]
            status = status_line.split('=')[1]
        else:
            #Get date
            date = line.split(',')[0]
            #Get list with longitudes
            _l = line.split(',')[1::3]
            #Get list with attitudes
            _a = line.split(',')[2::3]
            #Get list with counts
            _c = line.split(',')[3::3]
            if len(_l) == len(_a) == len(_c):
                #Aggregate elements from lists
                for (l, a, c) in zip(_l, _a, _c):
                    #while lists are not empty
                    if len(l) > 0 and len(a) > 0 and len(c) > 0:
                        print(status, date, status, l, a, c)