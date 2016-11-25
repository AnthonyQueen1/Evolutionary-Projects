from selection import natselect, init, getglobbest
from functions import getfitnesscount
import sys
from timeit import default_timer as timer

XRANG = (-60, 40)
YRANG = (-30, 70)
POPULATION_SIZE = 20
INDIVIDUAL_LENGTH = 30
MAX_ITERATIONS = 10000

start = timer()
popn = init(POPULATION_SIZE, INDIVIDUAL_LENGTH, XRANG, YRANG)

for i in range(MAX_ITERATIONS):
    print(i)
    popn = natselect(popn, i+1)
    if i%200 == 0:
        getglobbest()
    if getfitnesscount()==200000: 
        getglobbest()
        end = timer()
        print ('\ntotal time: ' + str(end-start) + ' seconds')
        sys.exit('\nPROGRAM STOPPED!\nmaximum fitness calculations')