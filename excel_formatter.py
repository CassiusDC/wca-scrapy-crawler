import pandas as pd
import numpy as np

dataframe = pd.read_excel('output_final3.xlsx', index_col=None, usecols="B:AA")
dataframe = dataframe.replace(r'.*Members.*','',regex=True)
dataframe = dataframe.replace(r'\[\"','',regex=True)
dataframe = dataframe.replace(r'\"]','',regex=True)
dataframe = dataframe.replace(r'\[]', '', regex=True)
dataframe = dataframe.replace(r'\[\'','',regex=True)
dataframe = dataframe.replace(r'\']','',regex=True)
dataframe = dataframe.replace(r'\', \'','',regex=True)
dataframe = dataframe.replace(r'\\n','',regex=True)
dataframe = dataframe.replace(r'\\r','',regex=True)
dataframe = dataframe.replace(r'\\t','',regex=True)
dataframe = dataframe.replace(np.nan, '', regex=True)
# dataframe = dataframe[['country']].replace(r' ','')
# dataframe = dataframe[['country']].replace('NewZealand','New Zealand')
dataframe.to_excel('formatted.xlsx')
print(dataframe)