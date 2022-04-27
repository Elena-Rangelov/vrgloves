import csv

filenames = ["jeb1.csv", "jeb2.csv", "jeb3.csv", "jeb4.csv", "jeb5.csv", "melissa.csv", "melissa1.csv", "melissa2.csv", "melissa3.csv", "melissa4.csv", "rahel.csv", "rahel1.csv", "rahel2.csv", "rahel3.csv", "rahel4.csv", "zak.csv", "zak2.csv", "zak3.csv", "zak4.csv", "zak5.csv", "afirsttry.csv", "bfirsttry.csv", "cfirsttry.csv", "dfirsttry.csv", "efirsttry.csv"]
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
        writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(values)
            
