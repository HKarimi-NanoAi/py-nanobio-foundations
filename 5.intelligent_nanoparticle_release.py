#___________________________________________________________________________________________________________________________
# Topic: Conditional Logic for Intelligent Nanoparticle Drug Release
# Description: Simulating smart drug delivery system responding to tumor microenvironment triggers (acidic pH and high MMP concentration).
# Application: Teaching (if-elif-else), using real-world cancer detection and targeted therapy logic.
#_________________________________________________________________________________________________________________________

ph_level = float(input("pH of the environment: "))
metalloproteinase_enzyme_concentration = float(input("Metalloproteinase enzyme concentration(MMP): "))

if ph_level < 6.5 and metalloproteinase_enzyme_concentration > 50:
    print("Full Release!")    
    
elif ph_level < 6.5 or metalloproteinase_enzyme_concentration > 50:
    print("The environment is suspicious! Partial Leakage...")
    
else:
    print ("The environment is perfectly healthy...")
