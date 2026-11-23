#Topic: Automated Optimal Cluster Selection via Silhouette Analysis
#Description: Standardizing CD4 and CD8 flow cytometry signals, evaluating clustering cohesion and separation across K=2..6 using the Silhouette Score, automatically selecting optimal K and summarizing phenotypic feature means per subpopulation.
#Application: Automated flow cytometry gating, quantitative cluster validation and computational immunology phenotyping.
#__________________________________________________________________________


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

immune_cells_df = pd.DataFrame({
    'CD4_Signal': [15, 18, 14, 16, 120, 125, 118, 122, 240, 250, 235, 245, 17, 121, 242],
    'CD8_Signal': [210, 220, 205, 215, 95, 100, 90, 98, 20, 25, 18, 22, 212, 92, 21]
})


x = immune_cells_df[['CD4_Signal','CD8_Signal']]
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

inertia_list = []
silhouette_scores = {}
K_range = range(2,7)

for k in K_range:
    K_mean = KMeans(n_clusters = k, random_state = 42)
    labels = K_mean.fit_predict(x_scaled)
    inertia_list.append(K_mean.inertia_)
    score = silhouette_score(x_scaled, labels)
    silhouette_scores[k] = score
    print(f'Silhouette Score for K={k}: {score:.3f}')



best_k = max(silhouette_scores, key=silhouette_scores.get)
print(f'The best K based on Silhouette Score is {best_k}')

final_kmean = KMeans(n_clusters = best_k, random_state = 42)
immune_cells_df['Optimal_Cluster'] = final_kmean.fit_predict(x_scaled)

cluster_mean = immune_cells_df.groupby('Optimal_Cluster').mean()
print(f'Mean features for each cluster:')
print(cluster_mean)
