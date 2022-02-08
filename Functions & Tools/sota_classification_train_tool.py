import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import argparse
import networkx as nx

def sota_train_classifier(m): #state-of-art classification / G is a networkx graph

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
    print('Accuracy of RandomForest on train set is:', model.score(X_train, y_train))

    return model

parser = argparse.ArgumentParser()
parser.add_argument(
    'M',
    type=int,
    help='Give the m value',
)
args = parser.parse_args()
m = args.M