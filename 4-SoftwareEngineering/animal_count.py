#!/usr/bin/env python

import animals
import sys

filename = sys.argv[1]
animal = sys.argv[2]

try:
    mean_count = animals.main(filename, animal)
    print "The mean count of", animal, "is", mean_count
except ZeroDivisionError:
    print "There were no", animal

