#Topic: Customized Bar Charts and Hatching Patterns in Matplotlib
#Description: Creating a visually enhanced bar plot with color gradients, custom bar widths, edge borders and cross-hatching patterns to illustrate cumulative drug release kinetics over time.
#Application: Nanomedicine, controlled drug delivery systems and in-vitro pharmaceutical release profiling.
#____________________________________________________________

import matplotlib.pyplot as plt

time = ['1h', '2h', '4h', '8h']
drug_release = [15, 40, 70, 95]

plt.bar(time, drug_release, color = ['gold', 'orange', 'coral', 'crimson'], edgecolor = 'black', width = 0.5, hatch='/')
plt.title('Anti-cancer drug release in 4 different times.')
plt.xlabel('Time')
plt.ylabel('Drug release')
plt.grid(axis = 'y', linestyle = '-')

plt.show()
