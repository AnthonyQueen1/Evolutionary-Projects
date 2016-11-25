from functions import mutate, indermediary_recomb, discrete_recomb, individual, fitness, initfun
import random

POPULATION_SIZE = 0
globbest = individual([], 10000)

# initializes things
def init(popsize, indlength, xrang, yrang):
    global POPULATION_SIZE
    POPULATION_SIZE = popsize
    return initfun(popsize, indlength, xrang, yrang)

# natural selection mechanism
# does either indermediary or discrete recombination
def natselect(popn, iteration):
    tpopn = list()
    while len(tpopn) < 200:
        if random.random() < .5:
            child = indermediary_recomb(parentselect(popn))
            mutate(child, iteration)
            tpopn.append(individual(child, fitness(child)))
        else:
            child = discrete_recomb(parentselect(popn))
            mutate(child, iteration)
            tpopn.append(individual(child, fitness(child)))
    return survivorselect(tpopn)


# uniform random selection for parent
def parentselect(popn):
    return [random.choice(popn), random.choice(popn)]

# deterministic selection of survivors
def survivorselect(popn):
    global globbest
    newpopn = sorted(popn,key=lambda x: x.fitness, reverse = False)
    if globbest.fitness > newpopn[0].fitness:
        globbest = newpopn[0]
    return [newpopn[i] for i in range(POPULATION_SIZE)]

def getglobbest():
    print('\nBest individual: ' + str(globbest.parameters) + '\n\nfitness: ' + str(globbest.fitness))