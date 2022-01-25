import os

# type = ["JESSEN_FULL", "JESSEN_MINIMAL", "ORDERED", "RANDOM", "ROMANTIC"]  # JESSEN_SIMPLE only for g = [2]
type = ["ORDERED", "ROMANTIC"]
g = [2, 3, 4, 5, 6, 7, 8, 9]
for m in g:
    for tp in type:
        for i in range(5000):
            os.system(
                f"D:\\billy\\Diplomatiki\\generate-graph-0.2\\bin\\generate-graph -t {tp} -n 100 -m {m} -s {i} > C:\\Users\\billy\\Diplomatiki\\Graphs100\\Graphs{m}\\{i}_{tp}.edges")
