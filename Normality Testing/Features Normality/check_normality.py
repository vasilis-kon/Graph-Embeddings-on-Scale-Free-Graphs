import numpy as np
from numpy import random
from numpy.random import seed
from numpy.random import normal
import matplotlib.pyplot as plt
from scipy.stats import shapiro

#Request sampling method from the user to check normality
print('Type... ')
print('A, if you want Normal Distribution sampling')
print('B, if you want Non Normal Distribution sampling')
model = input()

#make this example reproducible
seed(1)
samples = 100
means = []

if model == 'A':
    for i in range(5000):
    #generate sample of 200 values that follow a normal distribution
        data = normal(loc=0, scale=1, size=100)

        #find mean of sample
        mean = np.mean(data)
        means.append(mean)

elif model == 'B':
    for i in range(5000):
        #poisson distribution
        # data = random.poisson(lam=3, size=100)
        #powerlaw distribution
        data = np.random.power(5, 100)
        #find mean of sample
        mean = np.mean(data)
        means.append(mean)

count, bins, ignored = plt.hist(means, 30)
plt.show()

#perform Shapiro-Wilk test
normality_ckeck = shapiro(means)
print(normality_ckeck)
if normality_ckeck.pvalue > 0.05:
    print('Distribution looks Gaussian')
else:
    print('Distribution does not look Gaussian')

