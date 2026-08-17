#Topic: Independent Two-Sample T-Test for Nanoparticle Cytotoxicity Screening
#Description: Evaluating statistical significance in cell lethality/viability percentages between two novel nanocarrier formulations (Nano_A vs Nano_B) using SciPy stats.ttest_ind to compare cytotoxicity profiles.
#Application: Nanomaterial synthesis optimization, biophysical characterization Nanotoxicology assessment, in vitro cell viability assays (MTT/CCK-8) and comparative biocompatibility analysis in medical diagnostics  
#________________________________________

import pandas as pd
import numpy as np
from scipy import stats

nano_data = {
    'Nano_A': [14.2, 15.1, 13.8, 14.9, 15.5, 14.0],
    'Nano_B': [18.2, 19.5, 17.9, 18.8, 20.1, 18.4]
}
df_nano = pd.DataFrame(nano_data)

mean_nano_a = np.mean(df_nano['Nano_A'])
mean_nano_b = np.mean(df_nano['Nano_B'])
std_nano_a = np.std(df_nano['Nano_A'])
std_nano_b = np.std(df_nano['Nano_B'])

t_test, p_value = stats.ttest_ind(df_nano['Nano_A'], df_nano['Nano_B'])

print(f"Mean of Nano-A and Nano-B are {mean_nano_a:.2f} and {mean_nano_b:.2f} respectively. ")
print(f'The Standard Deviation of Nano-A and Nano-B are {std_nano_a:.2f} and {std_nano_b:.2f} respectively. ')
print(f't-Test and p-value are {t_test:.3f} and {p_value:.3f} respectively.')

if p_value < 0.05:
    print('Statistically Significant Difference Detected (p < 0.05).')
else:
    print('The Difference is NOT significant (P-value > 0.05).')
