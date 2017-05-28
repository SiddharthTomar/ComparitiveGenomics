overlap = set()
counter = 0
genes = []
tempArray = []
with open("record_result.xml.record") as file:
	for line in file:
		line = line.strip() 
		genes.append(line)
		
with open("experiments.txt") as f:
	for line in f:
		line = line.rstrip()
		tempArray = line.split(' ')
		matches = 0
		for z in genes:
			if z in tempArray:
				matches = matches + 1
				print (z)
				overlap.add(z)
		counter =  counter + 1
		print ("Number of matches in line %s : %s" %(counter,matches))
print ("Overlapping genes : ")
print (overlap)
print ("Done")