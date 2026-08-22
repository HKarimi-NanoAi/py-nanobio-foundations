#Topic: Gene Co-expression Analysis via Pearson Correlation Coefficient
# Description: Quantifying linear association strength and statistical significance (p-value) between expression profiles of two genes (Gene_X and Gene_Y) using SciPy stats.pearsonr for co-regulation analysis.
#Application: Systems biology, gene co-expression network reconstruction and biomarker co-variance analysis in genomic profiling.
#__________________________________________________________________
from scipy import stats

gene_x = [1.2, 2.4, 3.1, 4.5, 5.0]
gene_y = [2.1, 4.0, 5.9, 8.2, 9.8]

gene_pearson, p_value = stats.pearsonr(gene_x, gene_y)

print(f'Pearson correlaton is{gene_pearson:.3f} and p_value is {p_value:.3f}')
