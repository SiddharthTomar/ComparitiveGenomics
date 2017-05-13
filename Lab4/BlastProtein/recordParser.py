from Bio.Blast import NCBIXML	

#Define file names which are to be parsed
filename = ["05.xml","11.xml","19.xml"]

#Driving loop
for i in filename:
	bout = open(i)
	b_records = NCBIXML.parse(bout) #Main parsing function	
	outfile = open("record_%s.record" % i,'w') #Each parsed sequence is stored in a new file
	for b_record in b_records:
		for alig in b_record.alignments:
			for hsp in alig.hsps:
				print ("15"+"\t"+alig.hit_def+"\t"+i+"\t"+b_record.query+"\t"+str(hsp.score)+"\n")
				outfile.write ("15"+"\t"+alig.hit_def+"\t"+i+"\t"+b_record.query+"\t"+str(hsp.score)+"\n")
	outfile.close()
