#Topic: Immune Cell Subpopulation Discovery via Elbow Method & K-Means
#Description: Standardizing CD4 and CD8 flow cytometry signals, evaluating Within-Cluster Sum of Squares (Inertia) across K=1..7 via the Elbow Method to select optimal K=3, and clustering T-cell subpopulations.
#Application: Computational immunology, flow cytometry gating automation and unsupervised immune cell phenotyping.

#_____________________________________________________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


immune_cells_df = pd.DataFrame({
    'CD4_Signal': [15, 18, 14, 16, 120, 125, 118, 122, 240, 250, 235, 245, 17, 121, 242],
    'CD8_Signal': [210, 220, 205, 215, 95, 100, 90, 98, 20, 25, 18, 22, 212, 92, 21]
})

x = immune_cells_df[['CD4_Signal','CD8_Signal']].values



scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

inertia_list = []
K_range = range(1,8)

for k in K_range:
    km = KMeans(n_clusters = k, random_state = 42)
    km.fit(x_scaled)
    inertia_list.append(km.inertia_)


plt.plot(K_range, inertia_list, marker ='s', linestyle = '--')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia (WCSS)')
plt.title('Elbow Method for Optimal K')
plt.grid(True, alpha = 0.5)
plt.show()

#step 2
optimal_k = 3
kmeans = KMeans(n_clusters = optimal_k, random_state = 42)
clusters = kmeans.fit_predict(x_scaled)
immune_cells_df['Cell_Subpopulation'] = clusters

print(immune_cells_df)
