from numpy.random import seed
from numpy.random import randn
import pandas as pd
from scipy.stats import kruskal

# generate three independent samples
dt = pd.read_csv(f"Dataset_100_2.csv")
data = dt[['Average neighbor degree']]
data_t = data.T
j = 0
same = 0
different = 0
for i in range(44996):
	data1 = [data_t[i][0]]
	data2 = [data_t[i+1][0]]
	data3 = [data_t[i+2][0]]
	data4 = [data_t[i+3][0]]
	data5 = [data_t[i+4][0]]
	# compare samples
	stat, p = kruskal(data1, data2, data3, data4, data5)
	# print('Statistics=%.3f, p=%.3f' % (stat, p))
	# interpret
	alpha = 0.05
	if p > alpha:
		same = same + 1
		# print('Same distributions (fail to reject H0)')
	else:
		# print('Different distributions (reject H0)')
		different = different + 1
print(same,'out of 44996 sets come from the same distribution')
print(different,'out of 44996 sets come from the same distribution')