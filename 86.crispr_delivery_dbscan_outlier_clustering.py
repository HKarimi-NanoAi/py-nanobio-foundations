#Topic: Density-Based Clustering & Outlier Detection in CRISPR Delivery via DBSCAN
#Description: Standardizing CRISPR editing efficiency and cell viability metrics, applying DBSCAN (eps=0.8, min_samples=2) to discover dense functional groups, isolating cytotoxic/noisy outliers (label -1), and visualizing the spatial distribution.
#Application: Nanocarrier cytotoxicity screening, CRISPR-Cas9 delivery optimization and density-based anomaly detection in bioassays.
#____________________________________________________________________________________

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

crispr_delivery_df = pd.DataFrame({
    'Editing_Efficiency_pct': [12, 15, 14, 11, 78, 82, 80, 76, 13, 81, 45, 98],
    'Cell_Viability_pct': [92, 90, 94, 91, 84, 86, 85, 83, 93, 85, 25, 15]
})

X = crispr_delivery_df[['Editing_Efficiency_pct','Cell_Viability_pct']]
X_scaled = StandardScaler().fit_transform(X)

dbscan = DBSCAN(eps = 0.8, min_samples = 2)
crispr_delivery_df['Density_Group'] = dbscan.fit_predict(X_scaled)

cluster_count = crispr_delivery_df['Density_Group']. value_counts()

print("Sample Counts per Cluster (-1 Indicates Noise/Outliers)")
print(cluster_count)

noise_samples = crispr_delivery_df[crispr_delivery_df['Density_Group'] == -1]

print ('Detected Cytotoxic / Noisy Outlier Samples')
print(noise_samples)


scatter = plt.scatter(crispr_delivery_df['Editing_Efficiency_pct'], crispr_delivery_df['Cell_Viability_pct'], c = crispr_delivery_df["Density_Group"], cmap = 'plasma', s = 50, alpha=0.3, edgecolors='black')

cbar = plt.colorbar(scatter)
cbar.set_label('Density group (cluster/ noise)', fontsize = 9)

plt.title('CRISPR Delivery Profiling & Outlier Detection (DBSCAN)')
plt.xlabel('Editing Efficiency (%)')
plt.ylabel('Cell Viability (%)')
plt.grid(True, linestyle = '-.')

plt.show()
