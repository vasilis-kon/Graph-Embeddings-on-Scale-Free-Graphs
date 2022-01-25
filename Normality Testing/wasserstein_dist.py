import pandas as pd
import numpy as np
from numpy import random
from numpy.random import normal
import matplotlib.pyplot as plt
from scipy.stats import wasserstein_distance

#calculate the mean and variance of the non-normal distribution
dt = pd.read_csv(f"Dataset_100_2.csv")
feature = 'Assortativity'
data = dt[[feature]]
data_t = data.T
values = []

for i in range(5000):
    val = data_t[i][0]
    values.append(val)

print(len(values))
means = np.mean(values)
print('The mean of our data is..',means)
std = np.std(values)
print('The standard deviation of our data is..',std)
#create a normal distribution with the same mean and variance and 5000 data points
gaussian = normal(loc=means, scale=std, size=5000)

# print both sets to visualise the difference between the distributions
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.hist(values)
plt.title(f'Distribution for {feature}')
plt.subplot(122)
plt.hist(gaussian)
plt.title('Normal Distribution with same mean & std')
plt.show()

#calculate the wasserstein distance
distance = wasserstein_distance(values, gaussian)
print('The Wasserstein distance is...', distance)