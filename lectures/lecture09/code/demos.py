from __future__ import print_function
import csv
import numpy as np
from itertools import islice
# start a with statement, this opens the 
with open('demo.txt', 'r') as f:
    # let's read the text data
    read_data = f.read()
    print(read_data)
# once the indent is removed, the file is closed and dumped from memory!  

# start a with statement, this opens the 
with open('demo.txt', 'r') as f:
    # let's read the text data
    read_all_data = f.readlines()
    print(read_data)
# once the indent is removed, the file is closed and dumped from memory!  

with open('demo.txt', 'r') as f:
    for line in f:
        print(line)
        

with open('demo.txt', 'r') as d, open('final.txt', 'w') as f:
    # read all of demo.txt into memory
    my_txt = d.read()
    # replace 'replace_me_1'
    my_txt = my_txt.replace('replace_me_1', 'love')
    # replace 'replace_me_2'
    my_txt = my_txt.replace('replace_me_2', 'blah')
    # write my file to final.txt
    f.write(my_txt)
 
from itertools import islice   
with open('demo.txt', 'r') as d:
    for line in islice(d, 4, 10):
        print(line)
        
with open('demo.txt', 'r') as d:
    my_numbers = []
    for line in islice(d,0,10):
        # split the line by spaces
        temp = line.split(' ')
        # the nubmer is always the fourth item in the temp list
        my_numbers.append(float(temp[3]))

with open('demo.csv', 'r') as my_csv:
    my_data = []
    my_csv_data = csv.reader(my_csv, delimiter=',')
    for row in my_csv_data:
        my_data.append(row)
        
import numpy as np
x = np.random.random(10); y = np.random.random(10)
# convert to strings
x=x.astype('string'); y=y.astype('string')
with open('xy.csv', 'w') as my_csv:
    my_csv_write = csv.writer(my_csv, delimiter=',')
    # write the header
    my_csv_write.writerow(['x','y'])
    # write the csv row by row
    for row in zip(x,y):
        my_csv_write.writerow(row)
        
with open('demo.csv', 'r') as my_csv:
    my_data = []
    my_csv_data = csv.DictReader(my_csv, delimiter=',')
    for row in my_csv_data:
        print(row['radius(mm)'])

import numpy as np
w = np.random.random(10); z = np.random.random(10)
# convert to strings
w=w.astype('string'); z=z.astype('string')
with open('wz_dict.csv', 'w') as my_csv:
    # specify the header
    fieldnames = ['w', 'z']
    my_csv_write = csv.DictWriter(my_csv, delimiter=',',
        fieldnames=fieldnames)
    # write the header
    my_csv_write.writeheader()
    # write the csv row by row as dictionary
    for row in zip(x,y):
        my_csv_write.writerow({'w': row[0], 'z': row[1]})
        