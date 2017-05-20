import pandas as pd

#number of genes
keep = 300

#I/O lists
i = ["05.geneorder","11.geneorder","19.geneorder"]
Genome1 = []
Genome2 = []
Genome3 = []

#I/O Operations
with open(i[0],"r") as f:
	Genome1 = f.readlines()
	Genome1 = [x.strip() for x in Genome1] 
f.close()
	
with open(i[1],"r") as f:
	Genome2 = f.readlines()
	Genome2 = [x.strip() for x in Genome2] 
f.close()	

with open(i[2],"r") as f:
	Genome3 = f.readlines()
	Genome3 = [x.strip() for x in Genome3] 
f.close()	



#I like dataframes more than dictionaries! This converts each list into 
#1D table and uses that table to do a merge operation to find common
#elements. Before doing the merge operation, all the genes which have
#duplicates are removed 
df1 = pd.DataFrame({'Refrence': Genome1})
df1 = df1.drop_duplicates(subset='Refrence', keep=False, inplace=False)

df2 = pd.DataFrame({'Refrence': Genome2})
df2 = df2.drop_duplicates(subset='Refrence', keep=False, inplace=False)

df3 = pd.DataFrame({'Refrence': Genome3})
df3 = df3.drop_duplicates(subset='Refrence', keep=False, inplace=False)

#Relative position. Instead of working directly on each gene, this script
#works on the order of the gene found.
df1['index1'] = df1.index
df2['index2'] = df2.index
df3['index3'] = df3.index

#Merge operation itself - This operation uses Genome 2 as a refrence for
#finding common entries
s1 = pd.merge(pd.merge(df2,df3,on='Refrence', how = 'inner'),df1,on='Refrence', how = 'inner')

#For record keeping
s1.to_csv('orderedList.csv')

#Keeping the given number of genes
s1 = s1.head(keep)

#Doing "In-place" ordering for grimm by adding another ordering index
#Refrence here is the indexes from previous operations
dfList = s1['index2'].tolist()
tdf1 = pd.DataFrame({'Refrence': dfList})

dfList = s1['index1'].tolist()
tdf2 = pd.DataFrame({'Refrence': dfList})

dfList = s1['index3'].tolist()
tdf3 = pd.DataFrame({'Refrence': dfList})


tdf1['index'] = tdf1.index
tdf1['Index'] = tdf1.index + 1
tdf1 = tdf1.sort_values('Refrence')

tdf2['index'] = tdf2.index
tdf2['Index'] = tdf2.index + 1
tdf2 = tdf2.sort_values('Refrence')

tdf3['index'] = tdf3.index
tdf3['Index'] = tdf3.index + 1
tdf3 = tdf3.sort_values('Refrence')


#I/O operations
outfile = open("GRIMMIN",'w')

outfile.write (">Genome1"+":"+"\n")
dfList = tdf1['Index'].tolist()
for item in dfList:
	outfile.write("%s\n" % item)

outfile.write (">Genome2"+":"+"\n")
dfList = tdf2['Index'].tolist()
for item in dfList:
	outfile.write("%s\n" % item)

outfile.write (">Genome3"+":"+"\n")
dfList = tdf3['Index'].tolist()
for item in dfList:
	outfile.write("%s\n" % item)


outfile.close