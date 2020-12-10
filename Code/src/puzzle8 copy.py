#  id =  996731-20201201-c7599a1b
# @author : Srinjana Pathak

import sys
import random
import math
import itertools
import heapq
from functools import lru_cache
from collections import *



def run(prog):
    pc = 0
    acc = 0
    seen = set()
    while pc < len(prog):
        if pc in seen:
            # part 1, return acc here
            return None

        seen.add(pc)
        op, x = prog[pc]
        if op == "acc":
            acc += x
            pc += 1
        elif op == "jmp":
            pc += x
        else:
            pc += 1

    return acc


def main():
    fin = open("E:\Scripts\Python Scripts\AOC\Advent of code 2020\Code\input\input_d8.txt", "r")
    prog = [line.strip().split() for line in fin.readlines() if line.strip()]
    prog = [(op, int(x)) for op, x in prog]

    for i in range(len(prog)):
        if prog[i][0] == "acc":
            continue
        new_op = "jmp" if prog[i][0] == "nop" else "nop"
        new_prog = prog[:i] + [(new_op, prog[i][1])] + prog[i+1:]
        x = run(new_prog)
        if x is not None:
            print(x)


if __name__ == "__main__":
    main()
