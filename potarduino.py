import serial
import time
from cmath import inf
import csv

#   0 1 2 3 4 
#   P R M I T

SIZE = 5
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

limit = 50

data = []



#vals = []
mins = [inf for i in range(SIZE)]
maxs = [0 for i in range(SIZE)]


def process_input(string):    
    val = str(string).strip()[2:]
    return val[:-5]


print("calibrating...")
while(len(data) <= limit):
    data.append([int(i) for i in process_input(arduino.readline()).split()])
    

def min_max():
    for v in data:
        for i in range(SIZE):
            if v[i] > maxs[i]:
                maxs[i] = v[i]
            elif v[i] < mins[i]:
                mins[i] = v[i]
      
 
def mapVals(l):
    ret = []
    for i in range(SIZE):
        num = int(100*((l[i]-mins[i])/(maxs[i]-mins[i])))
        if num < 0:
            num = 0
        elif num > 100:
            num = 100
        ret += [num]
    
    return ret
    
#    return [int((100*l[i])/(maxs[i] - mins[i])) for i in range(SIZE)]


#####################################################

min_max()

print()
print(mins)
print(maxs)

'''
with open('afirsttry.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while 1:
        dis = arduino.readline()
        mapped = mapVals([int(i) for i in process_input(dis).split()])
        writer.writerow(mapped)
        print(mapped)

'''
with open('rahel4.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(26):
        #time.sleep(2)
        #print("now sign " + alpha[i] + "!")
        #time.sleep(1)
        ready = input("ready? ")
        arduino.reset_input_buffer()
        dat =arduino.readline()
        print("dat ", dat)
        mapped = mapVals([int(i) for i in process_input(dat).split()])
        writer.writerow(mapped)
        print(mapped)
        # print(dat)

################## LETTER A ######################