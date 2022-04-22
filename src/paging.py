import string
import random
import sys


# OS Assignment 1: Memory Management in CSC3002F
# By Gro Elisabeth Oleivsgard, OLVGRO001

# --- Write a python program that implements the FIFO, LRU, and optimal page replacement algorithms

# (1) First, generate a random page-reference string where page numbers range from 0 to 9.

# (2) Apply the random page reference string to each algorithm, and record the number of page faults
#       incurred by each algorithm.

# (3) Implement the FIFO, LRU and optimal (OPT) replacement algorithms so that the number of page
#       frames can vary from 1 to 7. Assume that demand paging is used. The main function should include
#       the following: (at the bottom)



#   Random page-reference generator returns a string of length n with values
#   ranging between 0 and 9.

def page_generator(n):
    page_ref = ''.join(random.choice(string.digits) for _ in range(n))
    return page_ref


#   FIFO algorithm swaps values in a "First-In-First-Out"-manner.  The "First-In" value
#   is kept track of by a pointer "top", that relocates as the values are added into the
#   array.

def FIFO(size, pages):

    page_faults = 0

    #   Creates empty array 'f' to contain frames in memory
    f = []
    top = 0

    #   Values are only inserted if it does not already exist in the memory
    for i in pages:
        if i not in f:

            #           Case: Memeory is not full
            if len(f)<size:
                f.append(i)
            #           Case: Memory is full, swap values with value at "top" ("First-In").
            else:
                f[top] = i
                top = (top + 1) % size
            #           Increment page-faults for each value inserted in the memory
            page_faults += 1
    return page_faults


#   OPT algorithm keeps track of the "frequency" of the pages, in order to exchange the
#   value that will be used the least in the near future. This is done with nested for-loops
#   that iterates through the page-reference string.
#   If a value in the memory is not in the remaining string, then that value
#   will be swapped with the current value. If all values in memory are present in the
#   string, the current value will be swapped with the value that will occur the latest.

def OPT(size, pages):

    page_faults = 0
    p = pages

    #   Creates empty array 'f' to contain frames
    f = []

    #   Variable that checks for similar numbers in the page-reference string
    frequency = [None for i in range(size)]


    for i in range(len(p)):

        #       Insert numbers as long as the number is not identical to a number already in memory
        if p[i] not in f:
            if len(f) < size:
                f.append(p[i])

            #           If memory is full, replace the page that will not be used for the longest period of time
            else:
                for x in range(len(f)):
                    if f[x] not in p[i+1:]:
                        f[x] = p[i]
                        break
                    else:
                        frequency[x] = p[i+1:].index(f[x])
                else:
                    f[frequency.index(max(frequency))] = p[i]
            page_faults += 1

    return page_faults

#   LRU algorithm keeps track of the Least Recently Used value. The elements of
#   pages is traversed, and it is checked if the element is present in memory.
#   If the element is present, it is moved to the end. If the element is not present,
#   but the memory is full, then the first element is removed as this is the least recently
#   used, and the elemnt is added to the end. This way, the least recently used element
#   will always be the first element.

def LRU(size, pages):


    page_faults = 0
    p = pages

    v = []

    for i in range(len(p)):
        #       Element not present in memory
        if p[i] not in v:
            #           If memory is full
            if len(v) == size:
                #               Remove the first element (least recently used)
                v = v[1:]

            #           Add element to the memory
            #           Increase count
            v.append(p[i])
            page_faults += 1

        #       Element present in the memory
        else:
            #           Remove and add it to the end
            v.remove(p[i])
            v.append(p[i])

    return page_faults


def main():
    size = int(sys.argv[1])
    length = int(sys.argv[2])
    pages = page_generator(length)

    print ('FIFO', FIFO(size,pages), 'page faults.')
    print ('LRU', LRU(size,pages), 'page faults.')
    print ('OPT', OPT(size,pages), 'page faults.')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print ('Usage: python paging.py [number of pages] [length of string]')
    else:
        main()























