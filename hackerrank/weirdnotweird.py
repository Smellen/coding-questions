#!/bin/python3

import math
import os
import random
import re
import sys

def IsEven(val):
    if val % 2 == 0:
        return True
    else:
        return False

def IsOdd(val):
    if val % 2 == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    n = int(input().strip())

# If N is odd, print Weird
# If N is even and in the inclusive range of 2 to 5, print Not Weird
# If N is even and in the inclusive range of 6 to 20, print Weird
# If N is even and greater than 20, print Not Weird

if IsEven(n) and n >= 6 and n <= 20:
    print("Weird")
elif IsEven(n) and n>=2 and n<=5:
    print("Not Weird")
elif n >= 20 and IsEven(n):
    print("Not Weird")
elif IsOdd(n):
    print("Weird")

