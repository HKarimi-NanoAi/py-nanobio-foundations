#Topic: Parsing CSV Data and Dataset Inspection Using Pandas
#Description: Simulating file I/O operations to load a comma-separated (CSV) clinical dataset into a DataFrame, inspecting its schema with info(), and calculating mean biomarker concentrations.
#Application: Reading real-world clinical electronic health records (EHR) and initiating the exploratory data analysis (EDA) phase.
#_____________________________________________________________________________________________________________________

hospital_csv = """Patient_ID,Age,Gender,CRP_Level
P01,28,M,3.2
P02,45,F,12.4
P03,32,M,1.5
P04,61,F,45.8
P05,50,M,8.9"""

hospital_df = pd.read_csv(io.StringIO(hospital_csv))
hospital_info = hospital_df.info()
hospital_crp_mean = hospital_df['CRP_Level'].mean()
print(f"Mean of CPR levels for this hospital cohort is {hospital_crp_mean}")
