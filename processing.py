
#  & C:/Users/elena/AppData/Local/Programs/Python/Python310/python.exe c:/Users/elena/Documents/liveshare/test.py

from cmath import inf
import csv

#   0 1 2 3 4 
#   P R M I T

SIZE = 2

vals = []
mins = [inf, inf, inf, inf, inf]
maxs = [0 for i in range(SIZE)]

def read_csv():
    with open( 'PotVals.csv' , newline='' ) as csvfile :
        myreader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
        i = 0
        for row in myreader:
            if i < 3:
                i+=1
                continue

            vals.append([int(r) for r in row])
            # print(row[0] +  "   " + row[1])


def min_max():
    for v in vals:
        for i in range(SIZE):
            if v[i] > maxs[i]:
                maxs[i] = v[i]
            elif v[i] < mins[i]:
                mins[i] = v[i]

        
 
def mapVal(num): 
    for i in range(SIZE):
        temp = int((100*num)/(maxs[i] - mins[i]))
        #print(temp)
        return int((100*num)/(maxs[i] - mins[i]))


#####################################################

read_csv()
min_max()
#mapVal()

for row in vals:
    s = ""
    for val in row:
        s += str(mapVal(val)) + ", "
    print(s)


################## LETTER A ######################

