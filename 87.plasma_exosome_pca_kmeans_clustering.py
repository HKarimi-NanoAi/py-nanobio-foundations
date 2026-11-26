#Topic: Plasma Exosome Subpopulation Clustering & Dimensionality Reduction via PCA
#Description: Standardizing 4-dimensional exosome characterization metrics (CD63, CD81, particle concentration, mean diameter), clustering into 3 distinct subpopulations with K-Means, and projecting the clusters onto a 2D Principal Component Analysis (PCA) space.
#Application: Extracellular vesicle (EV) characterization, NTA/flow cytometry multivariate analysis and high-dimensional biological visualization.
#___________________________________________________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

plasma_exosome_df = pd.DataFrame({
    'CD63_Intensity': [15, 18, 14, 120, 125, 118, 240, 248, 238, 16, 122, 245],
    'CD81_Intensity': [20, 22, 19, 110, 115, 108, 215, 220, 210, 21, 112, 218],
    'Particle_Conc_1e8': [1.1, 1.2, 1.0, 5.4, 5.8, 5.2, 9.5, 10.1, 9.2, 1.15, 5.5, 9.8],
    'Mean_Diameter_nm': [65, 68, 64, 105, 110, 102, 145, 150, 142, 66, 108, 148]
})

X = plasma_exosome_df[['CD63_Intensity','CD81_Intensity','Particle_Conc_1e8','Mean_Diameter_nm']]
X_scaled = StandardScaler().fit_transform(X)

kmean = KMeans(n_clusters = 3, random_state = 42)
plasma_exosome_df['Exosome_Group'] =kmean.fit_predict(X_scaled)

pca = PCA(n_components = 2, random_state = 42)
X_pca = pca.fit_transform(X_scaled)


plt.scatter(X_pca[:, 0], X_pca[:, 1], c = plasma_exosome_df['Exosome_Group'], cmap = 'viridis', s = 50, alpha=0.6, edgecolors='black', marker = 'v' )
plt.title('Principal Component Analysis Plot')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.grid(True, linestyle = '--')

plt.show()
