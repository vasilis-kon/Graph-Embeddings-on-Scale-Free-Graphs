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

# Type = ["JESSEN_FULL", "JESSEN_MINIMAL", "ORDERED", "RANDOM", "ROMANTIC", "BARABASI_ALBERT",
#         "POWERLAW_CLUSTER","BARABASI_IGRAPH", "BARABASI_NX_CLIQUE"]

# g = [2, 3, 4, 5, 6, 7, 8, 9]
g = [9]
with open('Dataset_100_9.csv', 'w', newline='') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(
        ['S-metric', 'Average clustering', 'Transitivity', 'Local efficiency', 'Subgraph centrality', 'Diameter',
         'Nodes in periphery', 'Radius',
         'Nodes in center', 'Nodes removed until break', 'Correlation', 'Average neighbor degree', 'Avg Degree 0',
         'Avg Degree Rank 0',
         'Avg Degree 1', 'Avg Degree Rank 1', 'Avg Degree m', 'Avg Degree Rank m',
         'Avg Degree m+1', 'Avg Degree Rank m+1', 'Maximal cliques', 'Size of largest clique',
         "Avg Node's maximal cliques",
         "Avg size of Node's largest maximal clique",'Assortativity', 'Generator', 'm', 'seed'])

    for m in g:
        for tp in Type:
            array_s = []
            array_avc = []
            array_glc = []
            array_loc = []
            array_av_sub = []
            array_diam = []
            array_peri = []
            array_rad = []
            array_cen = []
            array_nodes_removed = []
            array_cor = []
            array_and = []

            array_n0 = []
            array_n1 = []
            array_nm = []
            array_nm1 = []
            array_r0 = []
            array_r1 = []
            array_rm = []
            array_rm1 = []

            array_gn = []
            array_gc = []
            array_noc = []
            array_ncn = []

            array_assort_fast = []
            for i in range(5000):
                G = nx.read_edgelist(f'D:\\billy\\Diplomatiki\\Graphs100\\\Graphs{m}\\{i}_{tp}.edges',
                                     delimiter=',', nodetype=int)

                # S-metric
                s_metric_edges = [G.degree(edge[0]) * G.degree(edge[1]) for edge in G.edges()]
                s_m = sum(s_metric_edges)
                array_s.append(s_m)

                # Average clustering value
                avc = nx.average_clustering(G)
                array_avc.append(avc)

                # Average global clustering or transitivity value
                glc = nx.transitivity(G)
                array_glc.append(glc)

                # Local efficiency value
                loc = nx.local_efficiency(G)
                array_loc.append(loc)

                # Subgraph centrality value
                sub = nx.subgraph_centrality(G)
                svals = sub.values()
                av_sub = np.mean(list(svals))
                array_av_sub.append(av_sub)

                # Eccentricity, diameter, radius, nodes in periphery, nodes in center
                eccen = nx.eccentricity(G)
                diam = nx.diameter(G, eccen)
                peri = len(nx.periphery(G, eccen))
                rad = nx.radius(G, eccen)
                cen = len(nx.center(G, eccen))
                array_diam.append(diam)
                array_peri.append(peri)
                array_rad.append(rad)
                array_cen.append(cen)

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

                # Average neighbor degree
                nd = nx.average_neighbor_degree(G)
                nd_vals = nd.values()
                avg_nd = np.mean(list(nd_vals))
                array_and.append(avg_nd)

                d = G.degree()
                s = sorted(d, key=lambda x: x[1], reverse=True)
                highest_nodes = [v for v, w in s]
                # Average degree and average degree rank of nodes 0, 1, m, m+1
                n0 = nx.degree(G, 0)
                n1 = nx.degree(G, 1)
                nm = nx.degree(G, m)
                nm1 = nx.degree(G, m + 1)
                r0 = highest_nodes.index(0) + 1
                r1 = highest_nodes.index(1) + 1
                rm = highest_nodes.index(m) + 1
                rm1 = highest_nodes.index(m + 1) + 1

                array_n0.append(n0)
                array_n1.append(n1)
                array_nm.append(nm)
                array_nm1.append(nm1)
                array_r0.append(r0)
                array_r1.append(r1)
                array_rm.append(rm)
                array_rm1.append(rm1)

                # Νumber of maximal cliques in the graph.
                gn = nx.graph_number_of_cliques(G)
                array_gn.append(gn)
                # Size of the largest clique in the graph.
                gc = nx.graph_clique_number(G)
                array_gc.append(gc)

                # Number of maximal cliques for each node.
                noc = nx.number_of_cliques(G)
                nocvals = noc.values()
                array_noc.extend(nocvals)

                # Size of the largest maximal clique containing each given node
                ncn = nx.node_clique_number(G)
                ncnvals = ncn.values()
                array_ncn.extend(ncnvals)

                # Nodes removed until percolation threshold. We remove highest degree nodes 1-1.
                nodes_removed = 0
                s = sorted(d, key=lambda x: x[1], reverse=True)
                highest_nodes = [v for v, w in s]
                for h in highest_nodes:
                    G.remove_node(h)
                    nodes_removed += 1
                    condition = nx.is_connected(G)
                    if not condition:
                        break
                array_nodes_removed.append(nodes_removed)

                #Assortativity
                assort_fast = nx.degree_pearson_correlation_coefficient(G)
                array_assort_fast.append(assort_fast)

                row = [s_m, avc, glc, loc, av_sub, diam, peri, rad, cen, nodes_removed, correlation, avg_nd, n0, r0, n1,
                       r1,nm, rm, nm1, rm1, gn, gc, np.mean(list(nocvals)), np.mean(list(ncnvals)),assort_fast, tp, m, i]
                csv_out.writerow(row)

            with open('Dataset_means_9x.csv', 'a', newline='') as out2:
                csv_out2 = csv.writer(out2)
                row2 = [np.mean(array_s), np.mean(array_avc), np.mean(array_glc), np.mean(array_loc),
                        np.mean(array_av_sub),
                        np.mean(array_diam), np.mean(array_peri), np.mean(array_rad), np.mean(array_cen),
                        np.mean(array_nodes_removed), np.mean(array_cor), np.mean(array_and), np.mean(array_n0),
                        np.mean(array_r0), np.mean(array_n1), np.mean(array_r1), np.mean(array_nm),
                        np.mean(array_rm), np.mean(array_nm1), np.mean(array_rm1), np.mean(array_gn), np.mean(array_gc),
                        np.mean(array_noc), np.mean(array_ncn), np.mean(array_assort_fast), tp, m, i]
                csv_out2.writerow(row2)
