from Genetic_Algorithm import *
from Snake_Game import *
import numpy as np
import matplotlib.pyplot as plt

# n_x -> no. of input units
# n_h -> no. of units in hidden layer 1
# n_h2 -> no. of units in hidden layer 2
# n_y -> no. of output units

# The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
sol_per_pop = 50
num_weights = n_x * n_h + n_h * n_h2 + n_h2 * n_y

# Defining the population size.
pop_size = (sol_per_pop, num_weights)
# Creating the initial population.
new_population = np.random.choice(np.arange(-1, 1, step=0.01), size=pop_size, replace=True)

num_generations = 100
num_parents_mating = 12

# To store fitness scores of each generation
fitness_progress = []

# Open file to store output
with open("fitness_scores.txt", "w") as file:
    for generation in range(num_generations):
        file.write(f'############## GENERATION {generation} ###############\n')
        print(f'############## GENERATION {generation} ###############')

        # Measuring the fitness of each chromosome in the population.
        fitness = cal_pop_fitness(new_population)
        max_fitness = np.max(fitness)
        file.write(f'Fittest chromosome in generation {generation} has fitness value: {max_fitness}\n')
        print(f'Fittest chromosome in generation {generation} has fitness value: {max_fitness}')

        # Log fitness of each chromosome
        for i, fit in enumerate(fitness):
            file.write(f'Chromosome {i+1}: Fitness = {fit}\n')

        # Store fitness for plotting
        fitness_progress.append(max_fitness)

        # Selecting the best parents in the population for mating.
        parents = select_mating_pool(new_population, fitness, num_parents_mating)

        # Generating next generation using crossover.
        offspring_crossover = crossover(parents, offspring_size=(pop_size[0] - parents.shape[0], num_weights))

        # Adding some variations to the offspring using mutation.
        offspring_mutation = mutation(offspring_crossover)

        # Creating the new population based on the parents and offspring.
        new_population[0:parents.shape[0], :] = parents
        new_population[parents.shape[0]:, :] = offspring_mutation

# Plot fitness progression
plt.figure(figsize=(10, 5))
plt.plot(fitness_progress, color='blue', marker='o', linestyle='-', markersize=5)
plt.title('Fitness Score Progression Across Generations')
plt.xlabel('Generation')
plt.ylabel('Fitness Score')
plt.grid(True)
plt.show()
