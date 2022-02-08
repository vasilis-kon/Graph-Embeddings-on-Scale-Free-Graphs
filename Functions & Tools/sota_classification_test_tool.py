import pandas as pd
from sota_classification_train_tool import sota_train_classifier
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    'M',
    type=int,
    help='Give the m value',
)
args = parser.parse_args()
# graph = args.g
m = args.M

dg = pd.read_csv('Graph_stats.csv')
X_G = dg[['S-metric', 'Average clustering', 'Transitivity', 'Local efficiency', 'Subgraph centrality', 'Diameter',
          'Nodes in periphery', 'Radius',
          'Nodes in center', 'Nodes removed until break', 'Correlation', 'Average neighbor degree', 'Avg Degree 0',
          'Avg Degree Rank 0',
          'Avg Degree 1', 'Avg Degree Rank 1', 'Avg Degree m', 'Avg Degree Rank m',
          'Avg Degree m+1', 'Avg Degree Rank m+1', 'Maximal cliques', 'Size of largest clique',
          "Avg Node's maximal cliques",
          "Avg size of Node's largest maximal clique", 'Assortativity']]

model = sota_train_classifier(m)
generator = model.predict(X_G)
print('The generator used for creating our graph is...', generator)