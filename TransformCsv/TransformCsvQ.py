import itertools as it
status = None
date = None
new_lines = []
header = ['Status', 'Date', 'Latitude', 'Longitude', 'Count']

with open('C:\GIT\Labs.Python\TransformCsv\CoordStatusMA_Short.csv', mode='r', encoding='cp1252') as f:
    for line in f.readlines():
        if line.startswith('Status='):
            status_line = line.split(',')[0]
            status = status_line.split('=')[1]
        else:
            #Get date
            date = line.split(',')[0]
            #Get list with Latitudes
            _la = line.split(',')[1::3]
            #Get list with Longitudes
            _lo = line.split(',')[2::3]
            #Get list with counts
            _c = line.split(',')[3::3]
            if len(_la) == len(_lo) == len(_c):
                #Aggregate elements from lists
                for (la, lo, c) in zip(_la, _lo, _c):
                    #while lists are not empty
                    if len(la) > 0 and len(lo) > 0 and len(c) > 0:
                        print(status, date, status, la, lo, c)