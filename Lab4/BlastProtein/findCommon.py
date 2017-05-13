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
df05 = df05.head(300)
df11 = df11.head(300)
df19 = df19.head(300)



#s1 = pd.merge(df05, df11, df19, on=['Refrence_Name'], how='inner')
s1 = pd.merge(pd.merge(df11,df19,on='Refrence_Name', how = 'inner'),df05,on='Refrence_Name', how = 'inner')
s1.to_csv('full.csv')
#We need to remove the duplicates
s1 = s1.drop_duplicates(subset='Refrence_Name', keep='first', inplace=False)
s1 = s1.drop_duplicates(subset='Target_Name_05', keep='first', inplace=False)
s1 = s1.drop_duplicates(subset='Target_Name_11', keep='first', inplace=False)
s1 = s1.drop_duplicates(subset='Target_Name_19', keep='first', inplace=False)
del s1['Refrence_x']
del s1['Target_11']
del s1['Bit_Score_x']
del s1['Refrence_y']
del s1['Target_19']
del s1['Bit_Score_y']
del s1['Refrence']
del s1['Target_05']
del s1['Bit_Score']
s1 = s1.head(10)
s1.to_csv('condensed.csv')
