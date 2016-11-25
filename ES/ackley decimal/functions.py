import random
import math
from decimal import *
import decimal

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
    getcontext().prec=50
    random.seed()
    global POPULATION_SIZE, INDIVIDUAL_LENGTH, XRANG, YRANG, TPRIME, T
    XRANG, YRANG = xrang, yrang
    TPRIME = 1/Decimal(2*indlength).sqrt()
    T = 1/Decimal(2*math.sqrt(indlength)).sqrt()
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
                parm.insert(0, Decimal(random.uniform(YRANG[0], YRANG[1])))
            else:
                parm.insert(0, Decimal(random.uniform(XRANG[0], XRANG[1])))
            parm.append(1) # since initial sigmas are all 1
        popn.append(individual(parm, 100))
    return popn

# calculates fitness
# adopted from neal holts benchmark function. unm.edu
def fitness(ind):
    getcontext().prec=50
    global fitnesscounter
    fitnesscounter+=1
    # allows us to take either an individual or 
    # an individual's x,y values as input
    if isinstance(ind, individual):
        ind = ind.parameters
    firstsum, secondsum = Decimal(0), Decimal(0)
    for i in range(INDIVIDUAL_LENGTH):
        firstsum += ind[i]**2
        secondsum += cos(2*pi()*ind[i])
    return -Decimal(20)*(-Decimal(0.2)*(firstsum/INDIVIDUAL_LENGTH).sqrt()).exp() - (secondsum/INDIVIDUAL_LENGTH).exp() + 20 + Decimal(1).exp()
    

#mutates an individual
def mutate(ind, iteration):
    # allows us to take either an individual or 
    # an individual's x,y values as input
    if isinstance(ind, individual):
        ind = ind.parameters
    mutatesigma(ind, iteration)
    for i in range(INDIVIDUAL_LENGTH):
        ind[i] = ind[i] + ind[i+INDIVIDUAL_LENGTH]*Decimal(random.gauss(0,1)) 

# mutates the sigma values for an individual
# input is a list of floats x,y,z... ,sigma1, sigma2, sigma3,...
def mutatesigma(ind, iteration):
    gaussn = Decimal(random.gauss(0,1))
    for i in range(INDIVIDUAL_LENGTH, INDIVIDUAL_LENGTH*2):
        ind[i] = ind[i]*(TPRIME*gaussn + T*Decimal(random.gauss(0,1))).exp()
        # to make sure sigma is not too low
        if iteration > 600: 
             if ind[i]<Decimal(1/iteration**25): ind[i] = Decimal(1/iteration**25)
        else:
            if ind[i]<Decimal(1/iteration**10): ind[i] = Decimal(1/iteration**10)

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
    alpha = Decimal(random.random())
    for i in range(len(dad)):
        child.append(Decimal(alpha*dad[i] + (1-alpha)*mom[i]))
    return child

def getfitnesscount():
    return fitnesscounter


##########################3
#everything below i got from the python documentation for the decimal class
def pi():
    """Compute Pi to the current precision.

    >>> print pi()
    3.141592653589793238462643383

    """
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s               # unary plus applies the new precision

# def exp(x):
#     """Return e raised to the power of x.  Result type matches input type.

#     >>> print exp(Decimal(1))
#     2.718281828459045235360287471
#     >>> print exp(Decimal(2))
#     7.389056098930650227230427461
#     >>> print exp(2.0)
#     7.38905609893
#     >>> print exp(2+0j)
#     (7.38905609893+0j)

#     """
#     getcontext().prec += 2
#     i, lasts, s, fact, num = 0, 0, 1, 1, 1
#     while s != lasts:
#         lasts = s
#         i += 1
#         fact *= i
#         num *= x
#         s += num / fact
#     getcontext().prec -= 2
#     return +s

def cos(x):
    """Return the cosine of x as measured in radians.

    >>> print cos(Decimal('0.5'))
    0.8775825618903727161162815826
    >>> print cos(0.5)
    0.87758256189
    >>> print cos(0.5+0j)
    (0.87758256189+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def sin(x):
    """Return the sine of x as measured in radians.

    >>> print sin(Decimal('0.5'))
    0.4794255386042030002732879352
    >>> print sin(0.5)
    0.479425538604
    >>> print sin(0.5+0j)
    (0.479425538604+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s