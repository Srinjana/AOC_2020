#  id =  996731-20201201-c7599a1b
# @author : Srinjana Pathak

from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys


def main():
    raw_data = open("E:\Scripts\Python Scripts\AOC\Advent of code 2020\Code\input\input_d9.txt", "r")
    data = [int(line.strip()) for line in raw_data.readlines() if line.strip()]

# PART 1
    sums = set()
    n = len(data)
    for i, x in enumerate(data):
        valid = x in sums or i < 25
        if not valid:
            print("part 1", x)
            res1 = x
            break
        for j in range(n):
            sums.add(x + data[j])

# Part 2
    for i in range(n-1):
        s = 0
        for j in range(i, n):
            s += data[j]
            if s == res1:
                a = data[i:j+1]
                print("part 2", min(a)+max(a))
                
                
                break


    print("SECOND ITERATION OF PART 2 IS WRONG. I CANT FIX IT YET")


if __name__ == "__main__":
    main()
