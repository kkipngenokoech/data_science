import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sports_data = pd.read_csv("sports_data.csv", header=0, sep=',')
max_pulse = sports_data["Max_Pulse"]
# calculating the 10th percentile
ten_percentile = np.percentile(max_pulse,
                               10)  # how manytraining sessions have a pulse of 10 percentage of training sessions
print(ten_percentile)

# calculating the standard deviation
standard_deviation = np.std(sports_data)
print(standard_deviation)
print(np.std(max_pulse))

# coeefficient of variation
# how large the standard deviation is
c_variation = np.std(sports_data) / np.mean(sports_data)
print(c_variation)

# calculating data variance
variance = np.var(sports_data)
print("\t\tvariance\n", variance)
# positive linear corelation
sports_data.plot(x="Average_Pulse", y="Calorie_Burnage", kind="scatter")
plt.show()
#this compares entire dataset and give you the correlation
correlation_matrix = round(sports_data.corr(), 2)
print(correlation_matrix)
correlation_data=sports_data.corr()
heatmap_correlation=sns.heatmap(correlation_data,vmin=-1,vmax=1,center=0,cmap=sns.diverging_palette(50,500,n=500),square=True)
plt.show()