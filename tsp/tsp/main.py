##### main
from functions import init
from selection import natselect, getbest
from timeit import default_timer as timer


MAXITERATIONS       = 1000000
POPULATION_SIZE     = 300
PERMUTATION_LENGTH  = 127
TOURNAMENT_SIZE     = 10

TRIALS = 1
avg = []

def startit():
    global avg
    start = timer()
    
    old = start
    popn = init(POPULATION_SIZE, PERMUTATION_LENGTH)       
    i=0
    globmin = popn[0]
    while i<MAXITERATIONS and globmin.fitness>=118283:
        i+=1
        natselect(popn, TOURNAMENT_SIZE)
        if i%1000==0:
            globmin = getbest()
            current = timer()
            print '\n-----------------------------'
            print 'elapsed time: ' + str(current-old) + '\niteration: ' + str(i) + '\nfitness: ' + str(globmin.fitness) + '\n'
            print globmin. route
            old = current
    print '\nCOMPLETE!\niteration: ' + str(i)
    print globmin. route
    end = timer()
    avg.append(end-start)
    print '\ntotal time: ' + str(end-start)
    del popn[:]
    return (end-start, i)
    

def getaverage():
    print 'average elapsed time: ' + str(sum(avg)/float(len(avg)))

startit()
# getaverage()