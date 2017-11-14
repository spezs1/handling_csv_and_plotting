#!/usr/bin/env python

#Author Dr. Ziad Salem
#Search for 'ir_raw' in the file, then save the sensors values only into a new file
#I took the time off (secod col.)
#be careful to separate the backgroung from the rest of the file. 
#either you could check the timestamp about when the the real bees recording start
#or we blink the top led (diagnosticled) for 1 sec and we check that from the log file
#the file will handle the csv and plotting

import time
import argparse
import subprocess, sys
import csv

from datetime import datetime

from subprocess import call
from __main__ import *

timestamp = int(time.time()) #show integer value of time
t = timestamp
print ("FIRST 1 call to timestamp value =",t)

def csv_processing(m):
 	my_row = []
	with open('/home/assisi/assisi/IR_sensors_validations_2017/logs/2017-10-19-12-33-35-casu-006.csv', 'rt') as f1:
		print ("SECOND %%% 2 %%% call to timestamp value =",t)		
		with open('/home/assisi/assisi/IR_sensors_validations_2017/logs/IR_raw_'+str(t)+'.csv', 'w') as f2:
			print ("THIRD ### 3 ### call to timestamp value =",t)
			x = ("x=","IR_raw_"+str(t)+".csv")	
			print ("the file name x = ", x)	
			reader = csv.reader(f1)
			w = csv.writer(f2)
			w.writerow(('time','F','FL','BL','B','BR','FR'))
					
			for row in reader:
				if row [0] == "ir_raw":
					
					#print row [1], row[2], row[3], row[4], row[5],row[6], row[7] 
					my_row = []						
					my_row.append(row[1])
					my_row.append(row[2])
   					my_row.append(row[3])
    					my_row.append(row[4])
					my_row.append(row[5])
   					my_row.append(row[6])
    					my_row.append(row[7])					
					w.writerow (my_row )
					
		
	f1.close()
	f2.close()
	print ("T value before rerun to the main =",t)
	return t #return the results to the caller	
	
def plotting(n):
		
	print ("nnnnnn =",n)
	call (["python", "/home/assisi/assisi/IR_sensors_validations_2017/plot7.py"])

if __name__ == '__main__':
	
	print ("T value in main BEFORE the finction call =",t)
	y = 0	
	csv_processing(y)
	print ("T value in main AFTER the function call =",t)
	results = csv_processing(y)
	plotting(results)
	print ("YYYYY_2 =",results)

print "end"


