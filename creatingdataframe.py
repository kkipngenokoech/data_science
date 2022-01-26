import pandas as pd
import numpy as np
raw_data={"column_1":[1,2,3,4,5],"column_2":[6,7,8,9,10]}#this entry od data-with column names,and list of data it hold
#DataFrame()-helps us ceate a dataframe(dataframe is a stuctural rep of data
data_frame=pd.DataFrame(data=raw_data)#here is where the creation of the dataframe actualy occurs
print(data_frame)
count_columns=data_frame.shape[1]#count number of columns
count_rows=data_frame.shape[0]
print(count_columns,count_rows)

#finding the highest value of data in an array
Average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print(Average_pulse_max)
#finding the minimum value of data in an array
Average_pulse_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print(Average_pulse_min)

#finding the average value of data in anrray
calorie_burnage=[240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
average_colorie_burnage=np.mean(calorie_burnage)
print(average_colorie_burnage)