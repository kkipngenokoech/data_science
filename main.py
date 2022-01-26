import pandas as pd
abalone_data=pd.read_csv('abalone.data',header=None)#it is important to let py compiler that it has no header since it aassumes the first line is ,by default
#reading data directly from the web
urlprefix='https :// vincentarelbundock .github.io/ Rdatasets /csv/'
data_name='datasets/iris.csv'
iris_data=pd.read_csv(urlprefix+data_name)
print(abalone_data.head(5))