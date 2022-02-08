from scipy.stats import shapiro
import pandas as pd

# g = [2, 3, 4, 5, 6, 7, 8, 9]
g = [2]

# features_list = ['S-metric', 'Average clustering', 'Transitivity', 'Local efficiency', 'Subgraph centrality', 'Diameter',
#              'Nodes in periphery', 'Radius',
#              'Nodes in center', 'Nodes removed until break', 'Correlation', 'Average neighbor degree', 'Avg Degree 0',
#              'Avg Degree Rank 0',
#              'Avg Degree 1', 'Avg Degree Rank 1', 'Avg Degree m', 'Avg Degree Rank m',
#              'Avg Degree m+1', 'Avg Degree Rank m+1', 'Maximal cliques', 'Size of largest clique',
#              "Avg Node's maximal cliques",
#              "Avg size of Node's largest maximal clique",'Assortativity']

features_list = ['Assortativity']
generators = [["JESSEN_FULL", "JESSEN_MINIMAL", "ORDERED", "RANDOM", "ROMANTIC", "BARABASI_ALBERT",
               "POWERLAW_CLUSTER", "BARABASI_IGRAPH", "BARABASI_NX_CLIQUE"]]

#generators' indication matrix. each line represents the first and last data point of the generator from the dataset
gnr_ind = [0, 5000], [5000, 10000], [10000, 15000], [15000, 20000], [20000, 25000], [25000, 30000], [30000, 35000],\
          [35000, 40000], [40000, 45000]

for m in g:
    print('---------------------------')
    print('m is', m)
    dt = pd.read_csv(f"Dataset_100_{m}.csv")
    for feature in features_list:
        print('Feature is...',feature)
        data = dt[[feature]]
        for i in range(9):
            print('Generator is', generators[0][i])

            # ----- SHAPIRO NORMALITY TEST --------
            stat, p = shapiro(data[gnr_ind[i][0]:gnr_ind[i][1]])
            # print('Statistics=%.3f, p=%.3f' % (stat, p))
            # interpret
            alpha = 0.05
            if p > alpha:
                print('Sample looks Gaussian (fail to reject H0)')
            else:
                print('Sample does not look Gaussian (reject H0)')