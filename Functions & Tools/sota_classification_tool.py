import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import argparse
import networkx as nx
import numpy as np
import scipy.stats as sc
import csv

def nodes_pairs(n):
    k = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            k.append((i, j))
    return k

def graph_values(G,m): #G is a networkx graph
    values = []
    # S-metric
    s_metric_edges = [G.degree(edge[0]) * G.degree(edge[1]) for edge in G.edges()]
    s_m = sum(s_metric_edges)

    # Average clustering value
    avc = nx.average_clustering(G)

    # Average global clustering or transitivity value
    glc = nx.transitivity(G)

    # Local efficiency value
    loc = nx.local_efficiency(G)

    # Subgraph centrality value
    sub = nx.subgraph_centrality(G)
    svals = sub.values()
    av_sub = np.mean(list(svals))

    # Eccentricity, diameter, radius, nodes in periphery, nodes in center
    eccen = nx.eccentricity(G)
    diam = nx.diameter(G, eccen)
    peri = len(nx.periphery(G, eccen))
    rad = nx.radius(G, eccen)
    cen = len(nx.center(G, eccen))

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


    # Average neighbor degree
    nd = nx.average_neighbor_degree(G)
    nd_vals = nd.values()
    avg_nd = np.mean(list(nd_vals))

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

    # Νumber of maximal cliques in the graph.
    gn = nx.graph_number_of_cliques(G)

    # Size of the largest clique in the graph.
    gc = nx.graph_clique_number(G)

    # Number of maximal cliques for each node.
    noc = nx.number_of_cliques(G)
    nocvals = noc.values()

    # Size of the largest maximal clique containing each given node
    ncn = nx.node_clique_number(G)
    ncnvals = ncn.values()

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

    #Assortativity
    assort = nx.degree_pearson_correlation_coefficient(G)
    print("Graph Characteristics's calculation has been completed")
    characteristics = ['S-metric', 'Average clustering', 'Transitivity', 'Local efficiency', 'Subgraph centrality', 'Diameter',
         'Nodes in periphery', 'Radius',
         'Nodes in center', 'Nodes removed until break', 'Correlation', 'Average neighbor degree', 'Avg Degree 0',
         'Avg Degree Rank 0',
         'Avg Degree 1', 'Avg Degree Rank 1', 'Avg Degree m', 'Avg Degree Rank m',
         'Avg Degree m+1', 'Avg Degree Rank m+1', 'Maximal cliques', 'Size of largest clique',
         "Avg Node's maximal cliques",
         "Avg size of Node's largest maximal clique",'Assortativity']
    # val = [s_m, avc, glc, loc, av_sub, diam, peri, rad, cen, nodes_removed, correlation, avg_nd, n0, r0, n1,
    #            r1, nm, rm, nm1, rm1, gn, gc, np.mean(list(nocvals)), np.mean(list(ncnvals)), assort]
    values.append(s_m)
    values.append(avc)
    values.append(glc)
    values.append(loc)
    values.append(av_sub)
    values.append(diam)
    values.append(peri)
    values.append(rad)
    values.append(cen)
    values.append(nodes_removed)
    values.append(correlation)
    values.append(avg_nd)
    values.append(n0)
    values.append(r0)
    values.append(n1)
    values.append(r1)
    values.append(nm)
    values.append(rm)
    values.append(nm1)
    values.append(rm1)
    values.append(gn)
    values.append(gc)
    values.append(np.mean(list(nocvals)))
    values.append(np.mean(list(ncnvals)))
    values.append(assort)

    with open('Graph_stats.csv', 'w', newline='') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(
            ['S-metric', 'Average clustering', 'Transitivity', 'Local efficiency', 'Subgraph centrality', 'Diameter',
             'Nodes in periphery', 'Radius',
             'Nodes in center', 'Nodes removed until break', 'Correlation', 'Average neighbor degree', 'Avg Degree 0',
             'Avg Degree Rank 0',
             'Avg Degree 1', 'Avg Degree Rank 1', 'Avg Degree m', 'Avg Degree Rank m',
             'Avg Degree m+1', 'Avg Degree Rank m+1', 'Maximal cliques', 'Size of largest clique',
             "Avg Node's maximal cliques",
             "Avg size of Node's largest maximal clique", 'Assortativity'])
        csv_out.writerow(values)

    return characteristics, values

def soa_classification(X_G, m): #state-of-art classification / G is a networkx graph

    #Use our dataset to train the model for classification using the best performing classifier
    df = pd.read_csv(f'Dataset_100_{m}.csv')

    X_train = df[['S-metric', 'Average clustering', 'Transitivity', 'Local efficiency', 'Subgraph centrality', 'Diameter',
         'Nodes in periphery', 'Radius',
         'Nodes in center', 'Nodes removed until break', 'Correlation', 'Average neighbor degree', 'Avg Degree 0',
         'Avg Degree Rank 0',
         'Avg Degree 1', 'Avg Degree Rank 1', 'Avg Degree m', 'Avg Degree Rank m',
         'Avg Degree m+1', 'Avg Degree Rank m+1', 'Maximal cliques', 'Size of largest clique',
         "Avg Node's maximal cliques",
         "Avg size of Node's largest maximal clique",'Assortativity']]

    y_train = df['Generator']
    model = RandomForestClassifier(n_estimators=100, max_features=4)
    model.fit(X_train, y_train)
    generator = model.predict(X_G)
    print('Accuracy of RandomForest on train set is:', model.score(X_train, y_train))

    return generator


parser = argparse.ArgumentParser(description="Hello")
parser.add_argument(
    'g',
    help='Give the Graph',
)
parser.add_argument(
    'M',
    type=int,
    help='Give the m value',
)
args = parser.parse_args()
graph = args.g
m = args.M

G = nx.read_edgelist(graph, delimiter=',', nodetype=int)
chars, values = graph_values(G,m)
print("Our graphs' characteristics & their values are...")
print(chars)
print(values)
dg = pd.read_csv('Graph_stats.csv')
X_G = dg[['S-metric', 'Average clustering', 'Transitivity', 'Local efficiency', 'Subgraph centrality', 'Diameter',
          'Nodes in periphery', 'Radius',
          'Nodes in center', 'Nodes removed until break', 'Correlation', 'Average neighbor degree', 'Avg Degree 0',
          'Avg Degree Rank 0',
          'Avg Degree 1', 'Avg Degree Rank 1', 'Avg Degree m', 'Avg Degree Rank m',
          'Avg Degree m+1', 'Avg Degree Rank m+1', 'Maximal cliques', 'Size of largest clique',
          "Avg Node's maximal cliques",
          "Avg size of Node's largest maximal clique", 'Assortativity']]

generator = soa_classification(X_G, m)
print('The generator used for creating our graph is...', generator)