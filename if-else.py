import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    r = range(6,21)
    if n % 2 != 0:
        print 'Weird'
    elif n % 2 == 0 and 6 <= n <= 20:
        print "Weird"
    else:
        print "Not Weird"

        