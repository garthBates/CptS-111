###############################################################################
# S.L. Broschat
# CptS 111, Spring 2018
# Programming Assignment #6
# 
# show_digits.py
#
# Prints the occurrences of leading digits 1-9 for a given datafile together
# with the number of occurrences predicted by Benford's law.
###############################################################################
# Import log10 to calculate Benford's law.
from math import log10

def show_digits(nums):
    '''
    Calculate the total number of datapoints which is the sum of the
    occurrences of each leading digit.  Print leading digit, measured
    number of occurrences, and predicted number of occurrences.
    '''
    num_pts = sum(nums)
    print('Total number of datapoints =', num_pts)
    print('Number of occurrences of leading digits:')
    print('  digit  measured  predicted')
    for digit in range(1, 10):
        predicted = int(round(num_pts * log10(1.0 + 1.0 / digit)))
        print('  {:3d}  {:8d} {:8d}'.format(digit, nums[digit - 1], predicted))
    return
