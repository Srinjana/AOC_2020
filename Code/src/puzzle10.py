#  id =  996731-20201201-c7599a1b
# @author : Srinjana Pathak

import functools
from collections import Counter

raw_data = open("E:\Python Scripts\Python Scripts\AOC\Advent of code 2020\Code\input\input_d10.txt", "r")
data = [int(line.strip()) for line in raw_data.readlines() if line.strip()]

#part 1
def p1(data):
    joltage = sorted(data)
    s1, s2, last = 0, 0, 0

    for i, adapter in enumerate(joltage):
        diff = adapter - last

        if diff == 1:
            s1 += 1
        elif diff == 3:
            s2 += 1
        
        last = adapter 

    return(s1 * (s2+1))

# Part 2
def p2 (data):
    joltage = sorted(data)
    joltage.append(joltage[-1]+3)

    dp = Counter()
    dp[0] = 1

    for j in joltage:
        dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3]

    return(dp[joltage[-1]])


print(p1(data))
print(p2(data))
