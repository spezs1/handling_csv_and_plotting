#!/usr/bin/env python
# Author Ziad
# script for plotting the csv file

import csv
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy import *
import pandas as pd
import os, time, datetime 
#from csv_processing_plotting import y
#from csv_processing_plotting import y
#import csv_processing_plotting.y
from __main__ import *

from csv_processing_plotting_2 import csv_processing

#import csv_processing_plotting_2.y
#print csv_processing_plotting_2.y


#f1= "/home/assisi/assisi/IR_sensors_validations_2017/csv_processing_plotting.py"
#f2= "/home/assisi/assisi/IR_sensors_validations_2017/plot6.py"
#print ("f1 XXXXXX = ",os.path.getatime(f1))
#print ("f2 XXXXXX = ",os.path.getatime(f2))


if __name__ == '__main__':
 	
# plot x=time vs. y= all six sensors  
#try to change the time to standard
# try to print the very sensor value alone in one grap
#show all the graphs in one graph
	#print timestamp()
	
	#print ("t in csv file", csv_processing_plotting.t)
	#print ("timestamp in csv file", csv_processing_plotting.timestamp)
	#print ("x in csv file", csv_processing_plotting.y)
	y = csv_processing(0)
	#y = csv_processing(self)
	print "///////////////////////"
	print ("returned y =",y)

	#df = pd.read_csv('/home/assisi/assisi/IR_sensors_validations_2017/logs/IR_raw_2.csv', index_col=0)
	df = pd.read_csv('/home/assisi/assisi/IR_sensors_validations_2017/logs/IR_raw_'+str(y)+'.csv', index_col=0)

	df.plot(x=df.index, y=df.columns)
	plt.xlabel('time',fontsize=14)
	plt.ylabel('IR values',fontsize=14)
	plt.title('IR proximity sensors readings vs. time')
	plt.grid ('on') #show grid

	#ax = plt.subplot(111)
	#plt.legend()
	plt.legend(bbox_to_anchor=(1.0,1.0)) #legend outside the plot
	#plt.legend() #legend outside the plot
	figname = '/home/assisi/assisi/IR_sensors_validations_2017/logs/plot_1.pdf'
	plt.savefig(figname)    # save the plot into file
	plt.show() # show the plot



