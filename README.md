# MemoryManagement

This program implements three different page replacement algorithms used for memory management, 
namely FIFO (First-In-First-Out), OPT (Optimal Page Replacement) and LRU (Least Recently Used).

A simulation of referenced pages is used, with a random page generator that generates a string of
N numbers between 0 and 9 that will be put into a virtual memory containing frames of a set size.
The algorithms returns the number of page faults from each run, thus indicating its efficiency with
the lowest number of page faults being the most efficient for that particular combination.
