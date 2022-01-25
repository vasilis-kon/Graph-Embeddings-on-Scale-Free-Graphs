import networkx as nx
from karateclub import FeatherGraph, Graph2Vec,WaveletCharacteristic, LDP, IGE, GeoScattering, GL2Vec, NetLSD, SF, FGSD
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression


# Type = ["JESSEN_FULL", "JESSEN_MINIMAL", "ORDERED", "RANDOM", "ROMANTIC", "BARABASI_ALBERT",
#         "POWERLAW_CLUSTER","BARABASI_IGRAPH", "BARABASI_NX_CLIQUE"]
Type = ["RANDOM", "BARABASI_IGRAPH", "BARABASI_NX_CLIQUE"]
g = [2, 3, 4, 5, 6, 7, 8, 9]
graphs = []
y = []

#create a list of graphs for the graph embedding
for m in g:
    for tp in Type:
        for i in range(20):
            G = nx.read_edgelist(f'C:\\Users\\billy\\Diplomatiki\\Graphs100\\Graphs{m}\\{i}_{tp}.edges',
                                 delimiter=',', nodetype=int)
            graphs.append(G)
            # creating a list of labels for the classification
            generator = f'{tp}'
            y.append(generator)

#set the model & load graphs to create the embedding
model = FeatherGraph()
model.fit(graphs)
X = model.get_embedding()

# --- Classification ----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

downstream_model = LogisticRegression(random_state=0, max_iter=200).fit(X_train, y_train)
y_hat = downstream_model.predict_proba(X_test)
auc = roc_auc_score(y_test, y_hat, multi_class='ovr')
print('AUC: {:.4f}'.format(auc))
