from Bio.Blast import NCBIXML
result=open("19.xml","r")
records= NCBIXML.parse(result)
item=next(records)
for alignment in item.alignments:
          for hsp in alignment.hsps:
                 if hsp.expect <0.1:
                         print('****Alignment****')
                         print('sequence:', alignment.title) 
                         print('length:', alignment.length)
                         print('score:', hsp.score)
                         print('gaps:', hsp.gaps)
                         print('e value:', hsp.expect)
                         print(hsp.query[0:90] + '...')
                         print(hsp.match[0:90] + '...')
                         print(hsp.sbjct[0:90] + '...')