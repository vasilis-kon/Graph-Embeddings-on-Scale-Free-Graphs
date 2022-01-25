import networkx as nx
from karateclub import FeatherGraph
from sklearn.ensemble import GradientBoostingClassifier

def ge_classification(X_GE,m):
    graphs = []
    y_train = []
    Type = ["JESSEN_FULL", "JESSEN_MINIMAL", "ORDERED", "RANDOM", "ROMANTIC", "BARABASI_ALBERT",
            "POWERLAW_CLUSTER","BARABASI_IGRAPH", "BARABASI_NX_CLIQUE"]

    # create a list of graphs for the graph embedding
    for tp in Type:
        for i in range(10):
            g = nx.read_edgelist(f'C:\\Users\\billy\\Diplomatiki\\Graphs100\\Graphs{m}\\{i}_{tp}.edges',
                                 delimiter=',', nodetype=int)
            graphs.append(g)
            # creating a list of labels for the classification
            gen = f'{tp}'
            y_train.append(gen)
    # set the model & load graphs to create the embedding
    model = FeatherGraph()
    model.fit(graphs)
    X_train = model.get_embedding()

    model = GradientBoostingClassifier(n_estimators=200,learning_rate=0.6,max_features=2,max_depth=4)
    model.fit(X_train, y_train)
    y_test = model.predict(X_GE) #the predicted generator
    print('Accuracy of Gradient Boosting on train set is:', model.score(X_train, y_train))
    print(y_test)
