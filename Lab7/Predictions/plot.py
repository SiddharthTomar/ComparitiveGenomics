import pandas as pd
import numpy as np
import matplotlib.pyplot
import pylab

#input array -  Defines input files
input = ["05","11","15","19","34",]

#Question array : Answers the questions
q1 = []
q4 = []
q5 = []


#coordinate arrays, Q2 and Q3
datapoint_x = []
datapoint_y = []


for i in input:
	df = pd.read_csv("%s.txt" % i, delimiter=r"\s+")
	temp = df['TM'].tolist()
	temp = np.array(temp)
	x = np.count_nonzero(temp)
	datapoint_x.append(x)
	df = df[df.TM != 0]
	datapoint_y.append(df["TM"].mean())



for i in input:
	df = pd.read_csv("%s.txt" % i, delimiter=r"\s+")
	size = len(df)
	temp = df['TM'].tolist()
	temp = np.array(temp)
	x = np.count_nonzero(temp)
	df1 = df[df.TM != 0]
	size_tm = len(df1)
	df = df[df.SP == 'Y']
	size_sp_1 = len(df)
	df = df[df.TM != 0]
	size_sp = len(df)
	q1.append(size-size_tm)
	q4.append(size_sp_1)
	q5.append(size_sp)
	
	
print (datapoint_x)
print (datapoint_y)


print ("The fraction of proteins with 0 TM segments in sequence of input file : \n")
print (q1)

print ("The fraction of proteins with > 0 TM segments in sequence of input file : \n")
print (datapoint_x)

print ("The average number of TM segments for those with >0 segments in sequence of input file : \n")
print (datapoint_y)

print ("The fraction of proteins with > 0 signal peptide in sequence of input file : \n")
print (q4)

print ("The fraction of those (with > 0 signal peptide) with > 0 TM segments in sequence of input file : \n")
print (q5)

matplotlib.pyplot.scatter(datapoint_x,datapoint_y)

matplotlib.pyplot.ylabel('Average number of TM elements')
matplotlib.pyplot.xlabel('Number of TM proteins')

pylab.plot(datapoint_x,datapoint_y,'o')
z = np.polyfit(datapoint_x, datapoint_y, 1)
p = np.poly1d(z)
pylab.plot(datapoint_x,p(datapoint_x),"r--")
matplotlib.pyplot.show()
