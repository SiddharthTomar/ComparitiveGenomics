from Bio.Blast import NCBIXML	
import re

#Define file names which are to be parsed
filename = ["result.xml"]
genelist = []

#Driving loop
for i in filename:
	bout = open(i)
	b_records = NCBIXML.parse(bout) #Main parsing function	
	outfile = open("record_%s.record" % i,'w') #Each parsed sequence is stored in a new file
	for b_record in b_records:
		for alig in b_record.alignments:
			for hsp in alig.hsps:
				text = alig.hit_def
				m = re.findall(r'\bGN=\w+', text)
				m = m[0]
				print (m)
				z = m.split('=')
				genelist.append(z[1])
				outfile.write("%s\n" % z[1])
	outfile.close()
print (genelist)