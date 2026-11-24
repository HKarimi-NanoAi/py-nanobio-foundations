#Topic: Agglomerative Hierarchical Clustering & Dendrogram Analysis
#Description: Standardizing CD4 and CD8 flow cytometry signals, computing Ward linkage hierarchy via SciPy to plot a dendrogram and extracting 3 immune cell subpopulations via AgglomerativeClustering.
#Application: Computational immunology, hierarchical cell lineage mapping and flow cytometry subpopulation profiling.

#________________________________________________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import linkage, dendrogram

immune_cells_df = pd.DataFrame({
    'CD4_Signal': [15, 18, 14, 16, 120, 125, 118, 122, 240, 250, 235, 245, 17, 121, 242],
    'CD8_Signal': [210, 220, 205, 215, 95, 100, 90, 98, 20, 25, 18, 22, 212, 92, 21]
})

X = immune_cells_df[['CD4_Signal', 'CD8_Signal']]
X_scaled = StandardScaler().fit_transform(X)

Z = linkage(X_scaled, method = 'ward')

plt.figure(figsize =(9,4))
dendrogram(Z)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Sample Index")
plt.ylabel("Distance (Ward)")
plt.show()

agg = AgglomerativeClustering(n_clusters = 3, linkage = 'ward')
clusters = agg.fit_predict(X_scaled)

immune_cells_df['Hierarchical_Cluster'] = agg.fit_predict(X_scaled)


cluster_mean = immune_cells_df.groupby('Hierarchical_Cluster').mean()

print(f'Mean Phenotypic Signal Profile per Hierarchical Cluster:')

print(cluster_mean) 
