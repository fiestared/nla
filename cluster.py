import pandas as pd
import numpy as np
import csv
from sklearn.cluster import KMeans

cust_df = np.loadtxt('vec_pca_result.csv', delimiter=",")

model = KMeans(n_clusters=7).fit(cust_df)

labels = model.labels_

for label in labels:
    print label
