#Topic: Clinical Biomarker Preprocessing, Cohort Filtering and Excel Export
#Description: Imputing missing clinical biomarker levels via column mean strategy, subsetting high-risk patient cohorts ('Severe' condition) and exporting curated patient profiles to an Excel spreadsheet.
#Application: Automated clinical reporting, biomarker threshold screening and downstream laboratory data exchange pipelines.

#_____________________________________________________________________________

import pandas as pd
import numpy as np

raw_data = {
    'Patient_ID': ['PT_A', 'PT_B', 'PT_C', 'PT_D'],
    'Biomarker_Level': [14.2, np.nan, 18.5, 12.0],
    'Status': ['Severe', 'Mild', 'Severe', 'Mild']
}

raw_data_pd = pd.DataFrame(raw_data)

raw_data_pd['Biomarker_Level'] = raw_data_pd['Biomarker_Level'].fillna(raw_data_pd['Biomarker_Level'].mean())
print(f'NaN Values Imputed with Feature Mean:\n{raw_data_pd}')
print('Patients who are in Severe condition is loading ...')
severe_df = raw_data_pd[raw_data_pd['Status'] == 'Severe']
print(severe_df)
severe_df.to_excel('severe_patients.xlsx', index = False)
print('Your file generated Successfully.')
