import networkx as nx
import csv
import numpy as np
import scipy.stats as sc


def nodes_pairs(n):
    k = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            k.append((i, j))
    return k

Type = ["BARABASI_IGRAPH", "BARABASI_NX_CLIQUE","NETWORKIT"]



# g = [2, 3, 4, 5, 6, 7, 8, 9]
g = [5]
with open('D:\\billy\\Diplomatiki\\Paper\\Paper_dataset_temp.csv', 'w', newline='') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['S-metric', 'Average clustering', 'Transitivity', 'Local efficiency', 'Correlation', 'Average neighbor degree',
                      'Assortativity', 'Generator', 'm', 'seed'])

    for m in g:
        for tp in Type:
            array_s = []
            array_avc = []
            array_glc = []
            array_loc = []
            array_cor = []
            array_and = []
            array_assort_fast = []

            for i in range(700,800):
                G = nx.read_edgelist(f'D:\\billy\\Diplomatiki\\Paper\\Graphs5000\\{i}_{tp}.edges',
                                     delimiter=',', nodetype=int)

                # # S-metric
                s_metric_edges = [G.degree(edge[0]) * G.degree(edge[1]) for edge in G.edges()]
                s_m = sum(s_metric_edges)
                array_s.append(s_m)
                #
                # # Average clustering value
                avc = nx.average_clustering(G)
                array_avc.append(avc)
                #
                # # Average global clustering or transitivity value
                glc = nx.transitivity(G)
                array_glc.append(glc)
                #
                # # Local efficiency value
                loc = nx.local_efficiency(G)
                array_loc.append(loc)
                #
                # Correlation between the edge existence and degree product
                pairs = nodes_pairs(nx.number_of_nodes(G))
                A = []
                B = []
                for p in pairs:
                    if G.has_edge(p[0], p[1]):
                        A.append(1)
                    else:
                        A.append(0)
                    b1 = nx.degree(G, p[0])
                    b2 = nx.degree(G, p[1])
                    B.append(b1 * b2)
                correlation, p_value = sc.pearsonr(A, B)
                array_cor.append(correlation)
                #
                # Average neighbor degree
                nd = nx.average_neighbor_degree(G)
                nd_vals = nd.values()
                avg_nd = np.mean(list(nd_vals))
                array_and.append(avg_nd)
                #Assortativity
                assort_fast = nx.degree_pearson_correlation_coefficient(G)
                array_assort_fast.append(assort_fast)

                row = [s_m, avc, glc, loc, correlation, avg_nd, assort_fast, tp, m, i]
                csv_out.writerow(row)

            # with open('D:\\billy\\Diplomatiki\\Paper\\Paper_dataset_means.csv', 'a', newline='') as out2:
            #     csv_out = csv.writer(out2)
            #     row = [np.mean(array_s), np.mean(array_avc), np.mean(array_glc), np.mean(array_loc),np.mean(array_cor),
            #             np.mean(array_and), np.mean(array_assort_fast), tp, m, i]
            #     csv_out.writerow(row)
