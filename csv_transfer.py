# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:46:40 2022

@author: rahel
"""

import csv

filenames = ["rahel.csv"]
outputs = ["output.csv"]
values = []


for i in range(len(filenames)):
    
   
    with open(filenames[i], 'r') as csvfile:
        reader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
        
        values = []
        for i in range(26):
            values.append(next(reader)[0])
            print(values)
        
    with open("output.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(values)
        
        # for j in range(26):
    
