import pandas as pd
import numpy as np

dataframe = pd.read_csv('quotes_items.csv')
print(dataframe)
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
#dataframe[['country']] = dataframe[['country']].apply(lambda x: x.str.split().str[0])

#dataframe[['country']] = dataframe[['country']].replace(r' ','')
# dataframe = dataframe[['country']].replace('NewZealand','New Zealand')
dataframe.to_csv('formatted_quotes_spider.csv')
print(dataframe)