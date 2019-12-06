import os
import pandas as pd


input_path = r'C:\Users\Chris.Wodzinski\Desktop\test\\'
output_path = r'C:\Users\Chris.Wodzinski\Desktop\test\output\\'

df = pd.read_csv('test.csv')
  


#DEFINE LEVEL 
L = 16 



  
for i in df.index: 
    os.rename(input_path + '{}.pdf'.format(df['Name'].iloc[i]),
              output_path + 'C03-KEL-01A-'+str(L)+'-DRG-ST-{}_iss{}_rev{} RBG STATUS {}.pdf'.format(df['Name'].iloc[i], df['Iss'].iloc[i], df['Rev'].iloc[i], df['Status'].iloc[i]))
