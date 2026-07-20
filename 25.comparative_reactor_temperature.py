#Topic: Multi-Series Line Plots and Legends in Matplotlib
#Description: Plotting and customizing a multi-series time-series graph to compare the temperature profiles of two distinct chemical reactors.
#Application: Process monitoring in bio-nanotechnology, chemical engineering and comparing experimental vs. control group dynamics.
#___________________________________________________________________________

time_h = [0, 1, 2, 3, 4]
reactor_temp_a = [25, 50, 75, 75, 40]
reactor_temp_b = [25, 40, 60, 80, 55]

plt.plot(time_h, reactor_temp_a , color = 'orange', linewidth = 2.5 , marker = 'P', markersize = 10, markerfacecolor = 'forestgreen', label = 'Reactor 1')
plt.plot(time_h, reactor_temp_b , color = 'purple', linewidth = 2.5 , marker = 'D', markersize = 10, markerfacecolor = 'teal', label = 'Reactor 2')

plt.title('Reactors temperature over 4 hours')
plt.xlabel('Time (hour)')
plt.ylabel('Temperature')
plt.grid(True, linestyle =':')
plt.legend(loc = 'upper left')

plt.show()
