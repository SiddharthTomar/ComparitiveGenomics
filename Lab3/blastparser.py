from Bio.Blast import NCBIXML	

#Define file names which are to be parsed
filename = ["05_bn","11_bn","15_bn","19_bn","34_bn"]

#Driving loop
for i in filename:
	bout = open(i)
	b_records = NCBIXML.parse(bout) #Main parsing function	
	outfile = open("out_%s.fasta" % i,'w') #Each parsed sequence is stored in a new file
	for b_record in b_records:
		for alig in b_record.alignments:
			for hsp in alig.hsps:
				hitseq = hsp.sbjct.replace('-','') #Removing the gaps from the sequence
				print (">"+i+"\n"+hitseq)
				outfile.write (">"+i+"\n"+hitseq)
				outfile.close()
				