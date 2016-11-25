from selection import natselect, init, getglobbest
from functions import getfitnesscount
import sys
from timeit import default_timer as timer

XRANG = (-60, 40)
YRANG = (-30, 70)
POPULATION_SIZE = 5
INDIVIDUAL_LENGTH = 2
MAX_ITERATIONS = 10000

start = timer()
popn = init(POPULATION_SIZE, INDIVIDUAL_LENGTH, XRANG, YRANG)

for i in range(MAX_ITERATIONS):
    popn = natselect(popn, i+1)
    if getfitnesscount()>=2000: 
        getglobbest()
        end = timer()
        print ('\ntotal time: ' + str(end-start))
        sys.exit('\nPROGRAM STOPPED!\nmaximum fitness calculations')