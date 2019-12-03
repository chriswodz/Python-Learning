import os
import csv

with open('test.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #Make the reader skip the line 0
    next(csv_reader)
    

    #For all lines 1+, rename the intial file to the issue, revision & status given in text.csv
    for line in csv_reader:
        os.rename(r"C:\Users\chris.wodzinski\Desktop\test\\"+line[0]+".pdf",r"C:\Users\chris.wodzinski\Desktop\test\C03-KEL-01A-13-DRG-ST-"+line[0]+"_iss"+line[1]+"_rev"+line[2]+" RBG STATUS "+line[3]+".pdf")
        
