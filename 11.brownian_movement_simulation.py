#Topic: Stochastic Simulation of Brownian Movement in Nanoparticles
#Description: Simulating the random displacement of nanoparticles (nm) using 'random' library and 'while' loop control.
# Application: Fundamental for understanding particle diffusion, fluid dynamics and collision rates in nanobiosensor environments.
#________________________________________________________________________________________________________________________________

import random


def simulate_particle_movement():
    number_range = random.uniform(1.0, 5.0)  # based on nm
    return number_range


movement_history = []
movement_count = 1
while movement_count <= 5:
    movement_simul = simulate_particle_movement()
    movement_history.append(movement_simul)
    movement_count = movement_count + 1
    
print(f"List of movement changes {movement_history}")
