#!/usr/bin/env python

# Author Dr. Ziad Salem
#Add hearin to the lines 
#Search for 'ir_raw' in the file, then save the sensors values only into a new file
#I took the time off (secod line) but in that case we have to be careful to separate the backgroung from the rest of the file.
#either we check the time stamp about when the the real bees recording start
#or we blink the top led (diagnosticled) for 1 sec and we check that from the log file

#the file will handle the csv and plotting

import time
import argparse
import subprocess, sys
import csv
#import home/assisi/assisi/IR_sensors_validations_2017/plot5.py
from datetime import datetime

from subprocess import call
from __main__ import *
#from plot6 import *
#y = 57
#timestamp = time.time()
timestamp = int(time.time()) #show integer value of time
t = timestamp
print ("FIRST 1 call to timestamp value =",t)

def csv_processing(m):
#def csv_processing(self):
	#timestamp = time.time() 
	#print ("timestamp_1 =", timestamp)
	#print ("datetime.now() =", datetime.now())
 	my_row = []
	#y = 57

	with open('/home/assisi/assisi/IR_sensors_validations_2017/logs/2017-10-19-12-33-35-casu-006.csv', 'rt') as f1:
		#with open('/home/assisi/assisi/IR_sensors_validations_2017/logs/IR_raw_'+str(timestamp)+'.csv', 'w') as f2:
		print ("SECOND %%% 2 %%% call to timestamp value =",t)
		
		with open('/home/assisi/assisi/IR_sensors_validations_2017/logs/IR_raw_'+str(t)+'.csv', 'w') as f2:
			#print ("timestamp_2 =", timestamp)
			print ("THIRD ### 3 ### call to timestamp value =",t)
			x = ("x=","IR_raw_"+str(t)+".csv")	
			print ("the file name x = ", x)	
			#y=t
			#return y	
			#print ("datetime.now() =", timestamp)
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
	#print ("datetime.now() =", datetime.now())
	#print ("timestamp_3 =", timestamp)
	#x= timestamp
	print ("T value before rerun to the main =",t)
	return t #return the results to the caller	
	
def plotting(n):
	#import csv_processing_plotting_2
	#from csv_processing_plotting_2 import *
	
	print ("nnnnnn =",n)
	#print ("YYYYY_2 =",csv_processing_plotting_2.y)
	call (["python", "/home/assisi/assisi/IR_sensors_validations_2017/plot7.py"])

if __name__ == '__main__':
	#timestamp = time.time()
	#global t
	#t = timestamp	
	print ("T value in main BEFORE the finction call =",t)
	y = 0	
	csv_processing(y)
	#csv_processing(self)
	print ("T value in main AFTER the function call =",t)
	results = csv_processing(y)
	#results = csv_processing(self)
	plotting(results)
	print ("YYYYY_2 =",results)

print "end"

#y = 5
#print ("y=====", timestamp)
#print ("final t value =",t)
#print ("YYYYY_2 =",y)
#print(__name__.y)
        

