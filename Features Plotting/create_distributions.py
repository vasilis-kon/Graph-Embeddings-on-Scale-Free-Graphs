import pandas as pd
import matplotlib.pyplot as plt

g = [9]

for m in g:
    dt= pd.read_csv(f'Dataset_100_{m}.csv')

# features_list = ['S-metric', 'Average clustering', 'Transitivity', 'Local efficiency', 'Subgraph centrality', 'Diameter',
#          'Nodes in periphery', 'Radius',
#          'Nodes in center', 'Nodes removed until break', 'Correlation', 'Average neighbor degree', 'Avg Degree 0',
#          'Avg Degree Rank 0',
#          'Avg Degree 1', 'Avg Degree Rank 1', 'Avg Degree m', 'Avg Degree Rank m',
#          'Avg Degree m+1', 'Avg Degree Rank m+1', 'Maximal cliques', 'Size of largest clique',
#          "Avg Node's maximal cliques",
#          "Avg size of Node's largest maximal clique",'Assortativity']

# Type = ["JESSEN_FULL", "JESSEN_MINIMAL", "ORDERED", "RANDOM", "ROMANTIC", "BARABASI_ALBERT",
#         "POWERLAW_CLUSTER","BARABASI_IGRAPH", "BARABASI_NX_CLIQUE"]

    feature = 'S-metric'
    def_bins = 24
    col_jes_full = dt[[feature]]
    col_jes_min = dt[[feature]]
    col_ord = dt[[feature]]
    col_rom = dt[[feature]]
    col_bar_alb = dt[[feature]]
    col_power = dt[[feature]]
    col_rand = dt[[feature]]
    col_nx = dt[[feature]]
    col_ig = dt[[feature]]
    plt.figure(feature, figsize=(10, 6))
    plt.hist(col_jes_full[0:5000],bins=def_bins, label='jessen_full')
    plt.hist(col_jes_min[5001:10000],bins=def_bins, alpha=0.9, label='jessen_minimal')
    plt.hist(col_ord[10001:15000],bins=def_bins, label='ordered')
    plt.hist(col_rand[15001:20000],bins=def_bins, label='random')
    plt.hist(col_rom[20001:25000],bins=def_bins,alpha=0.8, label='romantic')
    plt.hist(col_bar_alb[25001:30000],bins=def_bins, alpha=0.6,label='barabasi_albert')
    plt.hist(col_power[30001:35000],bins=def_bins, label='powerlaw')
    plt.hist(col_ig[35001:40000],bins=def_bins, alpha=0.6, label='igraph')
    plt.hist(col_nx[40001:45000],bins=def_bins, alpha=0.6,label='nx_clique')
    plt.legend(loc='upper right')
    plt.xlabel(feature)
    plt.ylabel("Feature's Frequency")
    plt.suptitle(f'{feature} distribution for 5000 graphs/generator, n=100 and m={m}')
    plt.show()

