### functions.py
import random
import math
import inspect
import sys

fitlistdown = []
fitlistup   = []
POPULATION_SIZE, PERMUTATION_LENGTH = 0, 0
fitnesscounter = 0

class individual():
    def __init__(self, inboard, fit):
        self.board = inboard
        self.fitness = fit

# initializes things
def init(popsize, permlength):
    global POPULATION_SIZE, PERMUTATION_LENGTH 
    PERMUTATION_LENGTH, POPULATION_SIZE = permlength, popsize
    initfitness(permlength)
    return initpopn(popsize, permlength)

# initializes arrays to be used with fitness
# fitlistdown is for the downward diagonal and
# fitlistup is for the upward diagonal
# they are 2d arrays with all numbers the same on the diagonal
def initfitness(permlength):
    for i in range(permlength):
        templistdown = []
        templistup   = []
        # loop that iterates 4 times while increasing the starting index
        for j in range(i, permlength + i):
            templistdown.append(j)
            templistup.append(-permlength-j+i*2)
        fitlistdown.append(templistdown)
        fitlistup.append(templistup)

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
        ind = ind.board
    global fitnesscounter
    fitnesscounter+=1
    if fitnesscounter == 1000000: sys.exit('\nPROGRAM STOPPED!\n1 million fitness calculations\n')
    fitset = set()
    fitness = 0.0
    for row, col in enumerate(ind):
        if fitlistdown[row][col] in fitset: fitness+=1
        if fitlistup[row][col] in fitset: fitness+=1
        if fitlistdown[row][col] in fitset and fitlistup[row][col] in fitset: fitness+=.5
        else:
            fitset.add(fitlistdown[row][col])
            fitset.add(fitlistup[row][col])
    return fitness

# combines two parents to make a child
# partially mapped crossover 
def partmapcrossover(fatherobj, motherobj):
    father, mother = fatherobj.board, motherobj.board
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
    individual = individualobj.board
    i, j = randindex()
    individual[i], individual[j] = individual[j], individual[i]

# mutates and individual by inverting the substring between two operators
def invmutate(individualobj):
    individual = individualobj.board
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

