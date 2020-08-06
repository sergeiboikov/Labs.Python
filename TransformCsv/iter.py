

status = None
date = None

with open('C:\GIT\Labs.Python\TransformCsv\CoordStatusMA_Short.csv', mode='r', encoding='cp1252') as f:
    for line in f.readlines():
        if line.startswith('Status='):
            status_line = line.split(',')[0]
            status = status_line.split('=')[1]
        else:
            date = line.split(',')[0]
            _l = line.split(',')[1::3]
            _a = line.split(',')[2::3]
            _c = line.split(',')[3::3]
            if len(_l) == len(_a) == len(_c):
                for (l, a, c) in zip(_l, _a, _c):
                    if len(l) > 0 and len(a) > 0 and len(c) > 0:
                        print(status, date, status, l, a, c)
