import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sports_data = pd.read_csv("sports_data.csv", header=0, sep=',')

#PLOTTING THE GRAPH
sports_data.plot(x='Average_Pulse', y='Calorie_Burnage', kind='line'),
plt.ylim(ymin=240,ymax=400)#show us what value we want on the x and y axis to start from and thats 0 or whichever least number weve got
plt.xlim(xmin=80,xmax=150)
plt.show()

#FINDING THE SLOPE AND THE Y INTERCEPT
x=sports_data['Average_Pulse']
y=sports_data['Calorie_Burnage']
slope_intercept=np.polyfit(x,y,1)#one specifies the degree of functon-all coeefcients are in power of one
print(slope_intercept)
def my_function(x):
    return x*2+80#according to the above calculations
y_1=my_function(30)
print(y_1)