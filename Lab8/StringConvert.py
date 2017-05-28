from joblib import Parallel, delayed
import gzip 
import pandas as pd
import pylab as plt
import networkx as nx
import io
import mmap


#Taxonomic IDs to be searched
#taxa = ["4932","272561","243231","208964","289376"]
taxa = ["394"]



for z in taxa:
	#File I/O - open gzip file
	fileIO = gzip.open("protein.links.v10.txt.gz",'r')
	
	unique_protein = []
	
	#counters / Just to remove the first line
	c = 0

	#tuples
	listing = []
	print ("Entering the driver loop")
	#Iterating over the pointer 
	for line in fileIO:
		line = line.decode("latin1")
		temp = line.split(' ')
		tempTaxa = temp[0].split('.')[0]
		if (tempTaxa  == z):
			if temp[0] not in unique_protein:
				unique_protein.append(temp[0])
			if temp[1] not in unique_protein:
				unique_protein.append(temp[1])
			p1 = temp[0]
			p2 = temp[1]
			listing.append((p1,p2))
		c = c + 1
		if (c > 1):	
			if (int(tempTaxa) > int(z)):
				break
			
	#Creating a graph
	tup = tuple(listing)
	g = nx.Graph()
	edgeList = tup		
	g.add_edges_from(edgeList)
		
	#Calculating degree distribution
	print("Calculating degree distribution")
	degrees= g.degree() # dictionary node:degree
	values= sorted(set(degrees.values()))
	hist= [list(degrees.values()).count(x) for x in values]
	plt.figure() # you need to first do 'import pylabas plt'
	plt.grid(True)
	plt.loglog(values,hist,'ro-')
	plt.legend(['Degree'])
	plt.xlabel('Degree')
	plt.ylabel('Number of nodes')
	plt.title('Degree distribution for taxa %s' %z)
	plt.savefig('distribution_%s.pdf' %z)
	plt.close()
			
			
	print ("Calculating connectivity now")
	totalEdges = g.number_of_edges()
	totalNodes = len(g)
	averageConnectivity = totalEdges/totalNodes
	print ("Average connectivity : %s for taxa %s" % (averageConnectivity,z))
	fileIO.close()
	print ("Exiting the driver loop")

