#Topic: Unsupervised Exosome Flow Cytometry Subtype Clustering via K-Means
#Description: Discovering hidden biological clusters in unlabeled exosome flow cytometry data using K-Means clustering, extracting centroid coordinates, and visualizing cluster separation.
#Application: Unsupervised cell/exosome sorting, biomarker discovery and unlabeled clinical data pattern recognition.

#______________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

exosome_unlabeled_df = pd.DataFrame({
    'Exosome_Count': [120, 130, 115, 850, 920, 890, 125, 950, 110, 880],
    'Fluorescence_Signal': [10, 12, 11, 85, 92, 88, 9, 96, 13, 90]
})

kmeans = KMeans(n_clusters =2 , random_state = 42)
exosome_unlabeled_df["Exosome_Cluster"] = kmeans.fit_predict(exosome_unlabeled_df)

print("New DataFrame:")
print(exosome_unlabeled_df)

cluster_center = kmeans.cluster_centers_
print(f"Cluster center is :\n{cluster_center}")

plt.scatter(exosome_unlabeled_df["Exosome_Count"], exosome_unlabeled_df['Fluorescence_Signal'], c=exosome_unlabeled_df['Exosome_Cluster'], cmap='viridis', s = 60, alpha = 0.5, edgecolors = 'white', linewidths = 0.8 )
plt.scatter(cluster_center[:,0], cluster_center[:,1], marker ='X', s = 200, color = 'red', edgecolors = 'black', linewidths = 0.5, label = 'Cluster Center')

plt.xlabel('Exosome_Count')
plt.ylabel('Fluorescence_Signal')
plt.title('Exosome Clustering (K-Means)')
plt.colorbar(label = 'Cluster')
plt.legend()
plt.grid(True, alpha = 0.3)
plt.tight_layout()
plt.show()
