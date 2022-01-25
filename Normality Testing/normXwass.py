import pandas as pd
import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt
from scipy.stats import wasserstein_distance
from scipy.stats import shapiro
from sklearn import preprocessing

#calculate the mean and variance of the non-normal distribution
m = input('Please type the m value...\n')
dt = pd.read_csv(f"Dataset_100_{m}.csv")
feature = 'Assortativity'
data = dt[[feature]]
data_t = data.T

generators = [["JESSEN_FULL", "JESSEN_MINIMAL", "ORDERED", "RANDOM", "ROMANTIC", "BARABASI_ALBERT",
               "POWERLAW_CLUSTER", "BARABASI_IGRAPH", "BARABASI_NX_CLIQUE"]]
#generators' indication matrix. each line represents the first and last data point of the generator from the dataset
gnr_ind = [0, 5000], [5000, 10000], [10000, 15000], [15000, 20000], [20000, 25000], [25000, 30000], [30000, 35000],\
          [35000, 40000], [40000, 45000]

for i in range(1):
    values = []
    print('Generator is', generators[0][i])
    for gn in range(gnr_ind[i][0], gnr_ind[i][1]):
        val = data_t[gn][0]
        values.append(val)

    print('Sample size is',len(values))
    means = np.mean(values)
    print('The mean of our data is..',means)
    std = np.std(values)
    print('The standard deviation of our data is..',std)
    #create a normal distribution with the same mean and variance and 5000 data points
    gaussian = normal(loc=means, scale=std, size=5000)

    # print both sets to visualise the difference between the distributions
    plt.figure(generators[0][i],figsize=(10, 5))
    plt.subplot(121)
    plt.hist(values)
    plt.title(f'Distribution for {feature}')
    plt.subplot(122)
    plt.hist(gaussian)
    plt.title('Normal Distribution with same mean & std')
    plt.show()
    #
    # # calculate the wasserstein distance
    # distance = wasserstein_distance(values, gaussian)
    # print('The Wasserstein distance is...', distance)
    # # ----- SHAPIRO NORMALITY TEST --------
    # stat, p = shapiro(data[gnr_ind[i][0]:gnr_ind[i][1]])
    # print('Shapiro: Statistics=%.3f, p=%.3f' % (stat, p))
    # # interpret
    # alpha = 0.05
    # if p > alpha:
    #     print('Sample looks Gaussian (fail to reject H0)')
    # else:
    #     print('Sample does not look Gaussian (reject H0)')
    # print('------------------------------------------------------')