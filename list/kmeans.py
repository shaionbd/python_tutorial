import numpy as np
import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans

X = np.array([[6,9],[1,3],[3,6],[7,12],[2,5],[8,11]])

# clf = KMeans(n_clusters=2)
# clf.fit(X)
#
# centeriods = clf.cluster_centers_
# labels = clf.labels_
plt.scatter(X[:, 0], X[:, 1], s=100)
plt.show()
colors = 10*['r.', 'g.', 'b.', 'c.', 'k.']
