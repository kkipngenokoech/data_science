import pandas as pd
abalone_data=pd.read_csv("abalone.data",header=None,sep=",")#incase theres an header,pass index of the header to header
#print(abalone_data)
#print(abalone_data.head())#shows the first five rows of your data
sports_data=pd.read_csv("sports_data.csv",header=0,sep=",")
print(sports_data)
count_rows=sports_data.shape[0]
count_columns=sports_data.shape[1]
print(count_rows,count_columns)

#DATA CLEANING
"""
empty data is normally relaced by the NaNs in pd
when we find inconistent data we can
1.delete the entire row with inconsistent values
sports_data.dropna(axis=0,inplace=True)=axis=0means remove all rows with NaNs value
"""
#getting metadata on the imported data-genral meta data
print(sports_data.info())
#converting data from one data tpe tp another
sports_data["Max_Pulse"]=sports_data["Max_Pulse"].astype(float)
print(sports_data.info())
#summary/analyzing data column wise
print(sports_data.describe())
"""
count-total number of obrsevations
std-standard deviation
"""