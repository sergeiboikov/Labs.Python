#coding:cp1251
import os
from glob import glob

p = r'F:\GIT\Labs.Python\OS\Checks\*\*.txt'
conv = {
        'AHD_265': 'AHD_255', 
        'AHD_256': 'AHD_266', 
        'AHD_257': 'AHD_267'
        }

for file in glob(p):
    with open (file, 'r') as f:
        file_name = (os.path.basename(f.name))
        old_data = f.read()
        for k, v in conv.items():
            number_of_occurences = old_data.count(k)
            if number_of_occurences > 0:
                new_data = old_data.replace(k, v)
                print(f'{file_name} : {k} --> {v} ({number_of_occurences})')
                with open (file, 'w') as f:
                    f.write(new_data)