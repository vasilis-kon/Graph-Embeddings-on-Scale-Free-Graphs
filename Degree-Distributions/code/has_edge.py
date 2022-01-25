import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

nodes = [6, 7, 8, 9, 10]
Type = ["RANDOM","BARABASI_IGRAPH", "BARABASI_NX_CLIQUE"]

for n in nodes:
    for tp in Type:
        count = np.zeros((1, n-1))
        for graphs in range(10000):
            G = nx.read_edgelist(f'C:\\Users\\billy\\Diplomatiki\\Degree-Distribution\\Graphs_{n}\\{graphs}_{tp}.edges',
                                 delimiter=',', nodetype=int)
            for i in range(n-1):
                if G.has_edge(i, n - 1):
                    count[0][i] += 1
        if (tp == 'RANDOM'):
            random_vals = count/10000
        elif (tp == 'BARABASI_IGRAPH'):
            ig_vals = count/10000
        else:
            nx_vals = count/10000

    print('Number of nodes is..', n)
    print('-------RANDOM-------', random_vals)
    print('--BARABASI IGRAPH---', ig_vals)
    print('-BARABASI NX CLIQUE-', nx_vals)

    if n == 6:
        names = ['(1,6)', '(2,6)', '(3,6)', '(4,6)', '(5,6)']
    elif n == 7:
        names = ['(1,7)', '(2,7)', '(3,7)', '(4,7)', '(5,7)', '(6,7)']
    elif n == 8:
        names = ['(1,8)', '(2,8)', '(3,8)', '(4,8)', '(5,8)', '(6,8)', '(7,8)']
    elif n == 9:
        names = ['(1,9)', '(2,9)', '(3,9)', '(4,9)', '(5,9)', '(6,9)', '(7,9)', '(8,9)']
    else:
        names = ['(1,10)', '(2,10)', '(3,10)', '(4,10)', '(5,10)', '(6,10)', '(7,10)', '(8,10)', '(9,10)']

    plt.figure(figsize=(15, 5))
    plt.subplot(131)
    plt.bar(names, random_vals[0][:])
    plt.xlabel("Pairs of nodes")
    plt.ylabel("Percentage")
    plt.subplot(132)
    plt.bar(names, ig_vals[0][:])
    plt.xlabel("Pairs of nodes")
    plt.ylabel("Percentage")
    plt.subplot(133)
    plt.bar(names, nx_vals[0][:])
    plt.xlabel("Pairs of nodes")
    plt.ylabel("Percentage")
    plt.suptitle('RANDOM / IGRAPH / NX CLIQUE (10000 graphs each)')
    plt.show()
