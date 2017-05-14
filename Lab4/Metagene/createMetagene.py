import pandas as pd
import numpy as np
from Bio import SeqIO


#counter
counter = 0
#number of files
maxFile = 10
#metagene variables
meta1 = ""
meta1_id = ""
meta2 = ""
meta2_id = ""
meta3 = ""
meta3_id = ""
#File output pointer
outfile = open("meta.fa",'w')
#File input/concatination operations
for i in range (0,maxFile):	
	records = list(SeqIO.parse("%s.fa" % i, "fasta"))
	meta1_id = meta1_id+"|"+records[0].id
	meta1 = meta1+str(records[0].seq)
	meta2_id = meta2_id+"|"+records[1].id
	meta2 = meta2+str(records[1].seq)
	meta3_id = meta3_id+"|"+records[2].id
	meta3 = meta3+str(records[2].seq)

outfile.write (">"+meta1_id+"\n"+meta1+"\n"+">"+meta2_id+"\n"+meta2+"\n"+">"+meta3_id+"\n"+meta3)
outfile.close()	