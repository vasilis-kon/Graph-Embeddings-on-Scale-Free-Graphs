import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def alpha_calculation(G, deg_values):
    N = nx.number_of_nodes(G)
    SUM = 0
    kmin = min(deg_values)
    for k in deg_values:
        SUM += np.log(k / (kmin - 0.5))
    a = 1 + N * (SUM ** -1)
    # b = (a-1)/np.sqrt(N)
    return (a)


Type = ["RANDOM","BARABASI_IGRAPH", "BARABASI_NX_CLIQUE"]
g = [5] #value of m
nodes = [6, 7, 8, 10] #number of nodes in the graph
counter = 1
N = 10000 #number of graphs for each generator
for m in g:
    for n in nodes:
        counter = 1
        for tp in Type:
            array_d = []
            ar = []
            for i in range(N):
                G = nx.read_edgelist(f'C:\\Users\\billy\\Diplomatiki\\Degree-Distribution\\Graphs_{n}\\{i}_{tp}.edges',
                                     delimiter=',', nodetype=int)

                g = G.degree()
                degree_values = [v for k, v in g]
                array_d.extend(degree_values)

                a = alpha_calculation(G, degree_values)
                ar.append(a)

            print(f'm={m} {tp} average alpha:{np.mean(ar)}')

            plt.figure(m, figsize=(12, 8))
            plt.subplot(2, 2, counter)
            # allages sta logbins an theloume na exoume idies times ston x
            # logbins = np.logspace(np.log10(min(array_d)), np.log10(max(array_d)), 11)
            plt.hist(array_d, bins=10)
            plt.xscale('log')
            plt.yscale('log')
            plt.xlabel('Degree value')
            plt.ylabel(f'Frequency x{N}')
            plt.title(tp)
            plt.suptitle(f'Degree distribution for {N} graphs, n={n} and m={m}')
            counter += 1
        plt.show()



