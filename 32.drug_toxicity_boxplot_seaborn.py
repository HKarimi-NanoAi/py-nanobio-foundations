#Topic: Statistical Distribution Analysis via Seaborn Boxplots
#Description: Visualizing cytotoxicity variations across multiple drug treatments using Seaborn's boxplot to compare medians, interquartile ranges and distribution spreads with the Set2 color palette.
#Application: In vitro cytotoxicity profiling, drug safety evaluation and comparative pharmacology screening.
#__________________________________________________________

import seaborn as sns
import matplotlib.pyplot as plt

drug = ['Drug X', 'Drug X', 'Drug X', 'Drug X', 'Drug Y', 'Drug Y', 'Drug Y', 'Drug Y', 'Drug Z', 'Drug Z', 'Drug Z', 'Drug Z']
toxicity = [12, 15, 14, 18, 45, 48, 52, 50, 80, 85, 82, 98]

sns.set_theme(style ='whitegrid')

plt.figure(figsize = (6,4))
sns.boxplot(x = drug, y = toxicity, palette = 'Set2')
plt.title('Cell Toxicity Comparison across Drugs')
plt.xlabel('Drugs')
plt.ylabel('Toxicity (%)')

plt.show()
