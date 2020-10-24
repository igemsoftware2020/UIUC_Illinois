#%% array creation from sequence
import os
os.chdir("/Users/vanta/FASTA_FILES/")

antibodylight = open("antibodylight_6WPT.txt")
antibodylight_sequence = antibodylight.readline().rstrip("\n")
print(antibodylight_sequence)

aa2int_codes = {'A' : 1,
    'R' : 2,
    'N' : 3,
    'D' : 4,
    'C' : 5,
    'Q' : 6,
    'E' : 7,
    'G' : 8,
    'H' : 9,
    'I' : 10,
    'L' : 11,
    'K' : 12,
    'M' : 13,
    'F' : 14,
    'P' : 15,
    'S' : 16,
    'T' : 17,
    'W' : 18,
    'Y' : 19,
    'V' : 20,
    'B' : 21,
    'Z' : 22,
    'X' : 23,
    '*' : 24,
    '-' : 25,
    '?' : 26}

def aa2int(seq:str) -> list:
    return[aa2int_codes[i] for i in seq]

antibodylight_array = aa2int(antibodylight_sequence)
print(antibodylight_array)

#%% set antibody array as input
antibody_inputs = antibodylight_array
num_weights = 107

import numpy
sol_per_pop = 4
pop_size = (sol_per_pop, num_weights)
new_population = numpy.random.uniform(low=1.0, high=23.0, size=pop_size)
print(new_population)

#%% genetic algorithm setup and definitions
class GA_Antibody():
    def cal_pop_fitness(antibody_inputs, pop):
        fitness = numpy.sum(pop*antibody_inputs, axis=1)
        return fitness
    
    def select_mating_pool(pop, fitness, num_parents):
        parents = numpy.empty((num_parents, pop.shape[1]))
        for parent_num in range(num_parents):
            max_fitness = numpy.where(fitness == numpy.max(fitness))
            max_fitness = max_fitness[0][0]
            parents[parent_num, :] = pop[max_fitness, :]
            fitness[max_fitness] = -99999999999
        return parents
    
    def crossover(parents, offspring_size):
        offspring = numpy.empty(offspring_size)
        crossover_point = numpy.uint8(offspring_size[1]/2)
    
        for k in range(offspring_size[0]):
            parent1_idx = k%parents.shape[0]
            parent2_idx = (k+1)%parents.shape[0]
            offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
            offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
        return offspring
    
    def mutation(offspring_crossover):
        for idx in range(offspring_crossover.shape[0]):
            random_value = numpy.random.uniform(-1.0, 1.0, 1)
            offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value
        return offspring_crossover

#%% implement genetic algorithm to antibody sequence
num_generations = 5
num_parents_mating = 4

for generation in range(num_generations):
    print("Generation: ", generation)
    fitness = GA_Antibody.cal_pop_fitness(antibody_inputs, new_population)
    parents = GA_Antibody.select_mating_pool(new_population, fitness, num_parents_mating)
    offspring_crossover = GA_Antibody.crossover(parents, offspring_size=(pop_size[0]-parents.shape[0], num_weights))
    offspring_mutation = GA_Antibody.mutation(offspring_crossover)
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation
    
#%% getting best solution/fitness
fitness = GA_Antibody.cal_pop_fitness(antibody_inputs, new_population)
best_match = numpy.where(fitness == numpy.max(fitness))

print("Best solution: ", new_population[best_match, :])
print("Best solution fitness: ", fitness[best_match])