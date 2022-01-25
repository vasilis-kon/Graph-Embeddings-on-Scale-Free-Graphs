import networkx as nx
import igraph._igraph as ig

g = [2, 3, 4, 5, 6, 7, 8, 9]
for m in g:
    C = nx.complete_graph(m)
    for i in range(5000):
        G = nx.barabasi_albert_graph(100, m, i)
        nx.write_edgelist(G, f"D:\\billy\\Diplomatiki\\Graphs100\\Graphs{m}\\{i}_BARABASI_ALBERT.edges", delimiter=',', data=False)

        G = nx.powerlaw_cluster_graph(100, m, 0.5, i)
        nx.write_edgelist(G, f"D:\\billy\\Diplomatiki\\Graphs100\\\Graphs{m}\\{i}_POWERLAW_CLUSTER.edges", delimiter=',', data=False)

         # Gi = ig.GraphBase.Barabasi(1000, m)
         # A = Gi.get_edgelist()
         # G = nx.Graph(A)
         # nx.write_edgelist(G, f"C:\\Users\\billy\\Diplomatiki\\Graphs1000\\Graphs{m}\\{i}_BARABASI_IGRAPH.edges", delimiter=',', data=False)
         #
         # G = nx.barabasi_albert_graph(1000, m, i, initial_graph=C)
         # nx.write_edgelist(G, f"C:\\Users\\billy\\Diplomatiki\\Graphs1000\\Graphs{m}\\{i}_BARABASI_NX_CLIQUE.edges", delimiter=',', data=False)