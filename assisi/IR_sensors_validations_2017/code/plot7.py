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

from __main__ import *

from csv_processing_plotting_2 import csv_processing

if __name__ == '__main__': 	

	y = csv_processing(0)
	print "///////////////////////"
	print ("returned y =",y)

	df = pd.read_csv('/home/assisi/assisi/IR_sensors_validations_2017/logs/IR_raw_'+str(y)+'.csv', index_col=0)

	df.plot(x=df.index, y=df.columns)
	plt.xlabel('time',fontsize=14)
	plt.ylabel('IR values',fontsize=14)
	plt.title('IR proximity sensors readings vs. time')
	plt.grid ('on') #show grid

	
	plt.legend(bbox_to_anchor=(1.0,1.0)) #legend outside the plot
	figname = '/home/assisi/assisi/IR_sensors_validations_2017/logs/plot_1.pdf'
	plt.savefig(figname)    # save the plot into file
	plt.show() # show the plot



