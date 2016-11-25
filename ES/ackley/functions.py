import random
import math

POPULATION_SIZE, INDIVIDUAL_LENGTH, TPRIME, T = 0,0,0,0
XRANG, YRANG = tuple(), tuple()
fitnesscounter = 0

# an individual
class individual():
    def __init__(self, parm, fit):
        self.parameters = parm
        self.fitness = fit

# initializes things
def initfun(popsize, indlength, xrang, yrang):
    random.seed()
    global POPULATION_SIZE, INDIVIDUAL_LENGTH, XRANG, YRANG, TPRIME, T
    XRANG, YRANG = xrang, yrang
    TPRIME = 1/math.sqrt(2*indlength)
    T = 1/math.sqrt(2*math.sqrt(indlength))
    INDIVIDUAL_LENGTH, POPULATION_SIZE = indlength, popsize
    return initpopn()

# initialize population
def initpopn():
    popn = list()
    while len(popn) < POPULATION_SIZE:
        parm = list()
        for x in range(INDIVIDUAL_LENGTH):
            #this puts it in the order x,y,sigma,sigma
            if(len(parm)<INDIVIDUAL_LENGTH):
                parm.insert(0, random.uniform(YRANG[0], YRANG[1]))
            else:
                parm.insert(0, random.uniform(XRANG[0], XRANG[1]))
            parm.append(1) # since initial sigmas are all 1
        popn.append(individual(parm, 100))
    return popn

# calculates fitness
# adopted from neal holts benchmark function. unm.edu
def fitness(ind):
    global fitnesscounter
    fitnesscounter+=1
    # allows us to take either an individual or 
    # an individual's x,y values as input
    if isinstance(ind, individual):
        ind = ind.parameters
    firstsum, secondsum = 0.0, 0.0
    for i in range(INDIVIDUAL_LENGTH):
        firstsum += ind[i]**2
        secondsum += math.cos(2.0*math.pi*ind[i])
    return -20.0*math.exp(-0.2*math.sqrt(firstsum/INDIVIDUAL_LENGTH)) - math.exp(secondsum/INDIVIDUAL_LENGTH) + 20 + math.e
    

#mutates an individual
def mutate(ind, iteration):
    # allows us to take either an individual or 
    # an individual's x,y values as input
    if isinstance(ind, individual):
        ind = ind.parameters
    mutatesigma(ind, iteration)
    for i in range(INDIVIDUAL_LENGTH):
        ind[i] = ind[i] + ind[i+INDIVIDUAL_LENGTH]*random.gauss(0,1) 

# mutates the sigma values for an individual
# input is a list of floats x,y,z... ,sigma1, sigma2, sigma3,...
def mutatesigma(ind, iteration):
    gaussn = random.gauss(0,1)
    for i in range(INDIVIDUAL_LENGTH, INDIVIDUAL_LENGTH*2):
        ind[i] = ind[i]*math.exp(TPRIME*gaussn + T*random.gauss(0,1))
        # to make sure sigma is not too low
        if iteration > 600: 
             if ind[i]<1/iteration**25: ind[i] = 1/iteration**25
        else:
            if ind[i]<1/iteration**10: ind[i] = 1/iteration**10

# discrete recombination
# takes in two individuals or lists of floats as parents
# returns a list of floats (child)
def discrete_recomb(parents):
    if isinstance(parents[0], individual):
        dad, mom = parents[0].parameters, parents[1].parameters
    child = list()
    for i in range(len(dad)):
        if random.random()<.5:
            child.append(dad[i])
        else:
            child.append(mom[i])
    return child

# indermediary recombination
# takes in two individuals or lists of floats as parents
# returns a list of floats (child)
def indermediary_recomb(parents):
    if isinstance(parents[0], individual):
        dad, mom = parents[0].parameters, parents[1].parameters
    child = list()
    alpha = random.random()
    for i in range(len(dad)):
        child.append(alpha*dad[i] + (1-alpha)*mom[i])
    return child

def getfitnesscount():
    return fitnesscounter
