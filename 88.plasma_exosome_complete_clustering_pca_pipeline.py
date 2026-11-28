#Topic: Comprehensive Plasma Exosome Clustering, Validation & PCA Pipeline
#Description: Standardizing 4-dimensional exosome profiling metrics, performing K-Means clustering (K=3), validating cluster quality via Silhouette Score, summarizing phenotypic feature means per cluster, and projecting results onto a 2D PCA space.
#Application: Extracellular vesicle (EV) subtyping, automated NTA/flow cytometry phenotyping, and validated unsupervised biomedical workflows.
#______________________________________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

plasma_exosome_df = pd.DataFrame({
    'CD63_Intensity': [15, 18, 14, 120, 125, 118, 240, 248, 238, 16, 122, 245],
    'CD81_Intensity': [20, 22, 19, 110, 115, 108, 215, 220, 210, 21, 112, 218],
    'Particle_Conc_1e8': [1.1, 1.2, 1.0, 5.4, 5.8, 5.2, 9.5, 10.1, 9.2, 1.15, 5.5, 9.8],
    'Mean_Diameter_nm': [65, 68, 64, 105, 110, 102, 145, 150, 142, 66, 108, 148]
})

X = plasma_exosome_df[['CD63_Intensity','CD81_Intensity','Particle_Conc_1e8','Mean_Diameter_nm']]
X_scaled = StandardScaler().fit_transform(X)

km = KMeans(n_clusters = 3, random_state = 42)
plasma_exosome_df['Exosome_Group'] = km.fit_predict(X_scaled)

sil_score = silhouette_score(X_scaled, plasma_exosome_df['Exosome_Group'])
print(f'Silhouette Score: {sil_score:.3f}')

cluster_mean = plasma_exosome_df.groupby('Exosome_Group').mean()
print(f'Mean features for each cluster:')
print(cluster_mean)

pca = PCA(n_components = 2, random_state = 42)
X_pca = pca.fit_transform(X_scaled)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c = plasma_exosome_df['Exosome_Group'], cmap = 'plasma', s = 50, alpha = 0.2, edgecolors='black', marker = 's' )
plt.title('Principal Component Analysis Plot')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.grid(True, linestyle = '--')

plt.show()
