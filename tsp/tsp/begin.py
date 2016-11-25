import random
from random import randint

iteration = 0
fitness = 0.0
MAX_ITS = 1000
population = list()
maximum = 1

def mutate(num):
    mut = 1
    if random.random() <.5:
        mut = -1
    return num + mut

def fitness(num):
    return num*num-num

def init():
    for i in range(0,15):
        population.append(randint(0,100))

init()
while (iteration < MAX_ITS):
    minimum = 10000
    maximum = 1
    for pop in population:
        pop = mutate(pop)
    
    minimum = min(population, key=fitness)
    maximum = max(population, key=fitness)

    population.append(mutate(maximum))
    population.remove(minimum)
    print population
    iteration +=1