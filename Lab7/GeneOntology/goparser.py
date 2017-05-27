import pandas as pd

#Lambda for apply
def removedot (dot):
	tempstring = str(dot)
	tempstring = tempstring.split('.', 1)[0]
	return str(tempstring)



#Path to HMM search parser 
hmmFileHandle = "list.txt"
#Path to gene ontology record
goFileHandle = "pfam2go"

#We don't need first few lines in GO record
with open(goFileHandle, 'r') as fin:
	data = fin.read().splitlines(True)
with open("temp_go.txt", 'w') as fout:
	fout.writelines(data[6:])

#We need to make the GO record dataframe friendly 
infile = "temp_go.txt"	
outfile = "Processed_go.txt"
delete_list = ["Pfam:"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
	for word in delete_list:
		line = line.replace(word, "")
		line = " > ".join(line.split(" ", 1))
	fout.write(line)
fin.close()
fout.close()
	
#This will create a dataframe from search file
hmm = pd.read_csv(hmmFileHandle, sep='\t',names = ["Predicted_gene", "Pfam", "MISC1", "MISC2", "MISC3", "MISC4", "MISC5"])
hmm['Pfam'] = hmm['Pfam'].apply(removedot)

#How duplicates are treated depends on the user, and same goes for which column to keep
hmm = hmm.drop_duplicates(subset='Pfam', keep='first', inplace=False)
hmm = hmm.drop('MISC1', 1)
hmm = hmm.drop('MISC2', 1)
hmm = hmm.drop('MISC3', 1)
hmm = hmm.drop('MISC4', 1)
hmm = hmm.drop('MISC5', 1)


#This will create a dataframe from GO record
go = pd.read_csv("Processed_go.txt", sep=' > ',names = ["Pfam", "Misc", "GO"])

#Find common records
goRecord = pd.merge(go,hmm,on='Pfam', how = 'inner')

#save common records
goRecord.to_csv("GeneratedGO.csv", index=False, encoding='utf-8')
