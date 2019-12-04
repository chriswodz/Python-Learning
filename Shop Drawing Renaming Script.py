import os
import pandas as pd


input_path = r'C:\Users\Chris.Wodzinski\Desktop\test\\'
output_path = r'C:\Users\Chris.Wodzinski\Desktop\test\output\\'

df = pd.read_csv('test.csv')
    
for i in df.index: 
    os.rename(input_path + '{}.pdf'.format(df['Name'].iloc[i]),
              output_path + 'C03-KEL-01A-13-DRG-ST_{}_{}_{}_rev{}.pdf'.format(df['Name'].iloc[i], df['Iss'].iloc[i], df['Rev'].iloc[i], df['Status'].iloc[i]))
