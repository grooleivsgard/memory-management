import string
import random

# OS Assignment 1: Memory Management in CSC3002F
# By Gro Elisabeth Oleivsgard, OLVGRO001

# --- Write a python program that implements the FIFO, LRU, and optimal page replacement algorithms

# (1) First, generate a random page-reference string where page numbers range from 0 to 9.

# (2) Apply the random page reference string to each algorithm, and record the number of page faults
#       incurred by each algorithm.

# (3) Implement the FIFO, LRU and optimal (OPT) replacement algorithms so that the number of page
#       frames can vary from 1 to 7. Assume that demand paging is used. The main function should include
#       the following:




def main():
    #...TODO...
    size = int(sys.argv[1])
    print ’FIFO’, FIFO(size,pages), ’page faults.’
    print ’LRU’, LRU(size,pages), ’page faults.’
    print ’OPT’, OPT(size,pages), ’page faults.’

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ’Usage: python paging.py [number of pages]’
    else:
        main()

def reference_generator():
    page_ref = ''.join(random.choice(string.digits) for i in range (10))
    return page_ref

def LRU(size, pages):




