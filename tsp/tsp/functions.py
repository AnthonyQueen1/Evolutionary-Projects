### functions.py
import random
import math
import inspect
import sys

CITIES = []
POPULATION_SIZE, PERMUTATION_LENGTH = 0, 0
fitnesscounter = 0

class individual():
    def __init__(self, inroute, fit):
        self.route = inroute
        self.fitness = fit

# initializes things
def init(popsize, permlength):
    global POPULATION_SIZE, PERMUTATION_LENGTH
    PERMUTATION_LENGTH, POPULATION_SIZE = permlength, popsize
    initfitness()
    return initpopn(popsize, permlength)

# initializes fitness
def initfitness():
    global CITIES
    with open("tsp.txt") as f:
        # nested loop that also gets rid of the index in the file
        # also i removed the words from the top of the file for simplicity
        CITIES = [[int(x)  for x in line.split() if int(x)>130] for line in f]


# initializes population
def initpopn(popsize, permlength):
    population = set() 
    while len(population) < popsize:
        rang = range(permlength)
        random.shuffle(rang)
        population.add(tuple(rang))
    popn = [individual(list(pop), fitness(pop)) for pop in population]
    return popn

# measure of an individual's desirability
def fitness(ind):
    # allows fitness to take an object or a permutation
    if isinstance(ind, individual): 
        ind = ind.route
    global fitnesscounter
    fitnesscounter+=1
    fitness = 0.0
    for cit in range(PERMUTATION_LENGTH):
        if cit==126: fitness += math.sqrt(pow(CITIES[ind[cit]][0] - CITIES[ind[0]][0],2) + pow(CITIES[ind[cit]][1] - CITIES[ind[0]][1],2))
        else: fitness += math.sqrt(pow(CITIES[ind[cit]][0] - CITIES[ind[cit+1]][0],2) + pow(CITIES[ind[cit]][1] - CITIES[ind[cit+1]][1],2))
    return fitness

# combines two parents to make a child
# partially mapped crossover 
def partmapcrossover(fatherobj, motherobj):
    father, mother = fatherobj.route, motherobj.route
    i, j = randindex()
    child = []
    middledad = set()
    for k in range(PERMUTATION_LENGTH):
        if i <= k <= j: 
            child.insert(k, father[k])
            middledad.add(father[k])
        else: 
            child.insert(k, -1)
    for k in range(i, j+1):
        if mother[k] not in middledad:
            tempindex = mother.index(father[k])
            while i <= tempindex <= j:
                tempindex = mother.index(father[tempindex]) # findns an index outised range i,j
            child[tempindex] = mother[k]
    for k in range(PERMUTATION_LENGTH):
        if child[k] == -1: child[k] = mother[k]
    return individual(child, 0)

# mutates an individual by swapping two of its members randomly
def swapmutate(individualobj):
    individual = individualobj.route
    i, j = randindex()
    individual[i], individual[j] = individual[j], individual[i]

# mutates and individual by inverting the substring between two operators
def invmutate(individualobj):
    individual = individualobj.route
    i, j = randindex()
    while i<j:
        individual[i], individual[j] = individual[j], individual[i]  
        j-=1
        i+=1

# gets two distinct random indeces such that i<j 
def randindex():
    i, j = 0, 0
    while i==j: i, j = random.randint(0, PERMUTATION_LENGTH-1), random.randint(0, PERMUTATION_LENGTH-1)
    i, j = min(i,j), max(i,j)
    return (i,j)

