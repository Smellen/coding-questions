#!/bin/python3

# Read an integer N. For all non-negative integers i < N , print i squared. See the sample for details.




if __name__ == '__main__':
    n = int(input())

    if n > 0:
        for val in range(n):
            print(val**2)
