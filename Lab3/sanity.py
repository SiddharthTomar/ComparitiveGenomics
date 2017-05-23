from Bio import SeqIO

#Variables
id = [] #RecordID
sequence = [] #Array to store sequence, should have used dictonary

#File Input
for record in SeqIO.parse("besthits.fa", "fasta"):
	id.append(record.id)
	sequence.append(record.seq.tostring())

#Repeat sequence by appeanding a copy
append_seq = 1

#Sequence shuffle
seq_1 = sequence[0] #define the pairs where sequence will be shuffled
seq_2 = sequence[1] #define the pairs where sequence will be shuffled
A_1, A_2 = seq_1[:len(seq_1)//2], seq_1[len(seq_1)//2:]
B_1, B_2 = seq_2[:len(seq_2)//2], seq_2[len(seq_2)//2:]
sequence[0] = B_1 + A_2
sequence[1] = A_1 + B_2

if (append_seq == 1):
	sequence[0] = sequence[0] + sequence[0]
	sequence[1] = sequence[1] + sequence[1]
	sequence[2] = sequence[2] + sequence[2]
	sequence[3] = sequence[3] + sequence[3]

#File Output
outfile = open('sanityhits.fa', 'w')
for i in range(0,4): 
	outfile.write (">"+id[i]+"\n")
	outfile.write (sequence[i]+"\n")
outfile.close()