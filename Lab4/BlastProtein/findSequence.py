import pandas as pd
import numpy as np
from Bio import SeqIO

#File input operations
df = pd.read_csv('condensed.csv')
sep = ' '
#Iterate over rows in dataframe
for i, row in df.iterrows():
	fasta05 = SeqIO.parse("05.fa", "fasta")
	fasta11 = SeqIO.parse("11.fa", "fasta")
	fasta19 = SeqIO.parse("19.fa", "fasta")
	outfile = open("multi_%s.fa" % i,'w')
	protein05 = (row['Target_Name_05']).split(sep, 1)[0]
	protein11 = (row['Target_Name_11']).split(sep, 1)[0]
	protein19 = (row['Target_Name_19']).split(sep, 1)[0]
	for record in fasta05:
		if (protein05 == record.id):
			print("i"+"\n")
			outfile.write (">"+record.id+"\n"+str(record.seq)+"\n")
	for record in fasta11:
		if (protein11 == record.id):
			outfile.write (">"+record.id+"\n"+str(record.seq)+"\n")	
	for record in fasta19:
		if (protein19 == record.id):
			outfile.write (">"+record.id+"\n"+str(record.seq)+"\n")
	outfile.close()
