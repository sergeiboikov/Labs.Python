import itertools as it
import sys
import os

status = None
date = None
source_file = r'D:\OneDrive\OneDrive - EPAM\BI Exchange\2021\Databricks\Source files\CoordStatusMA_Short.csv'
column_names = ['Status', 'Date', 'Latitude', 'Longitude', 'Count']

if os.path.exists(source_file):
    new_file = open(os.path.splitext(source_file)[0] + '_prepared.csv', 'w')
    new_file.write(f'{column_names[0]}, {column_names[1]}, {column_names[2]}, {column_names[3]}, {column_names[4]}\n')
    with open(source_file, mode='r', encoding='cp1252') as f:
        for line in f.readlines():
            if len(line.strip()) > 0:
                if line.startswith('Status='):
                    status_line = line.split(',')[0]
                    status = status_line.split('=')[1]
                else:
                    # Get date
                    date = line.split(',')[0]
                    # Get list with Latitudes
                    _la = line.split(',')[1::3]
                    # Get list with Longitudes
                    _lo = line.split(',')[2::3]
                    # Get list with counts
                    _c = line.split(',')[3::3]
                    if len(_la) == len(_lo) == len(_c):
                        # Aggregate elements from lists
                        for (la, lo, c) in zip(_la, _lo, _c):
                            # while lists are not empty
                            if len(la) > 0 and len(lo) > 0 and len(c) > 0:
                                new_file.write(
                                    f'{status.strip()}, {date.strip()}, {la.strip()}, {lo.strip()}, {c.strip()}\n')
    new_file.close()
