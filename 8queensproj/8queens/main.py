### main.py
from functions import init
from selection import natselect, getbest
from timeit import default_timer as timer


MAXITERATIONS       = 1000000
POPULATION_SIZE     = 100
PERMUTATION_LENGTH  = 100
TOURNAMENT_SIZE     = 20

def startit():
    global avg
    start = timer()
    
    old = start
    popn = init(POPULATION_SIZE, PERMUTATION_LENGTH)       
    i=0
    globmin = popn[0]
    while i<MAXITERATIONS and globmin.fitness!=0:
        i+=1
        natselect(popn, TOURNAMENT_SIZE)
        if i%1000==0:
            globmin = getbest()
            current = timer()
            print '\n-----------------------------'
            print 'elapsed time: ' + str(current-old) + '\niteration: ' + str(i) + '\nfitness: ' + str(globmin.fitness) + '\n'
            print globmin.board
            old = current
    print '\nCOMPLETE!\niteration: ' + str(i)
    print globmin.board
    end = timer()
    print '\ntotal time: ' + str(end-start)
    return (end-start, i)
    del popn[:]

def getaverage():
    print 'average elapsed time: ' + str(sum(avg)/float(len(avg)))

startit()
# getaverage()