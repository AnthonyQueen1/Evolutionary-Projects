#### selection.py
from functions import fitness, individual, partmapcrossover, swapmutate, invmutate
import random

globmin = individual([], 10000000000)

# selects best individual in a tournament
# population is a list of individual objects
# size is a int representing the size of the tournament
# selects for either winners or losers
def tournament(population, size, winners):
    global globmin
    s = []
    # generates random members of the tournament
    while len(s) < size:
        s.append(random.randint(0, len(population)-1))
    sublist = [population[i] for i in s]
    best = sublist[0]
    if winners:
        for sub in sublist: 
            if sub.fitness<best.fitness and random.random()<.9: best = sub
        if best.fitness<=globmin.fitness: globmin = best
    else:
        for sub in sublist:
            if sub.fitness>best.fitness and random.random()<.6: best = sub
    return best

def natselect(population, tournsize):
    global globmin
    win, loose = True, False
    # gets two tournament winners
    dad, mom = tournament(population, tournsize, win), tournament(population, tournsize, win)
    # make sure we still have that best individual
    if globmin not in population: mom = globmin
    # creates children of the tournament winners
    mom, dad = partmapcrossover(dad, mom), partmapcrossover(mom, dad)
    # tournament to select losers
    worstmom, worstdad = tournament(population, tournsize, loose), tournament(population, tournsize, loose)
    mutater(mom)
    mutater(dad)
    # checks to make sure we are not trying to assign the same individual to 
    # two different children
    if worstdad != worstmom: 
        population[population.index(worstdad)] =  dad
        dad.fitness = fitness(dad)
    population[population.index(worstmom)] =  mom
    mom.fitness = fitness(mom)
    #####
    # if globmin not in population: son = globmin
    # population[population.index(worstdad)] = son
    # son.fitness = fitness(son)

# mutates an individual
def mutater(ind):
    if random.random() < 1:
        if random.random()<.9:
            swapmutate(ind)
        else: invmutate(ind)

# gets the global best
def getbest():
    global globmin
    return globmin