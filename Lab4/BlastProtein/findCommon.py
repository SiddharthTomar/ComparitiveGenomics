import pandas as pd

df05 = pd.DataFrame.from_csv('record_05.xml.record', sep='\t', index_col=None, header = None)
df11 = pd.DataFrame.from_csv('record_11.xml.record', sep='\t', index_col=None, header = None)
df19 = pd.DataFrame.from_csv('record_19.xml.record', sep='\t', index_col=None, header = None)
df05.columns = ["Refrence", "Refrence_Name", "Target_05", "Target_Name_05", "Bit_Score"]
df11.columns = ["Refrence", "Refrence_Name", "Target_11", "Target_Name_11", "Bit_Score"]
df19.columns = ["Refrence", "Refrence_Name", "Target_19", "Target_Name_19", "Bit_Score"]
df05 = df05.sort('Bit_Score', ascending=False)
df11 = df11.sort('Bit_Score', ascending=False)
df19 = df19.sort('Bit_Score', ascending=False)
df05 = df05.head(100)
df11 = df11.head(100)
df19 = df19.head(100)



#s1 = pd.merge(df05, df11, df19, on=['Refrence_Name'], how='inner')
s1 = pd.merge(pd.merge(df11,df19,on='Refrence_Name', how = 'inner'),df05,on='Refrence_Name', how = 'inner')
s1.to_csv('full.csv')
del s1['Refrence_x']
del s1['Target_11']
del s1['Bit_Score_x']
del s1['Refrence_y']
del s1['Target_19']
del s1['Bit_Score_y']
del s1['Refrence']
del s1['Target_05']
del s1['Bit_Score']
s1.to_csv('condensed.csv')