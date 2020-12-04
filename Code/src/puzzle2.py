#  id =  996731-20201201-c7599a1b
# @author : Srinjana Pathak

import collections

with open("..\Code\input_d2.txt", "r") as f:
    dataset= list(f.readlines())

# solution for Part 1 of the problem
# the data is split into it's components and the condition for valid passwords is checked.
valid = 0
for entry in dataset:
    count, alpha, pword = entry.split()
    least, most = map(int, count.split("-"))
    if least <= collections.Counter(pword)[alpha[0]] <= most:
        valid += 1

print("Number of Valid passwords: ")
print(valid)

# solution for part 2
# takes a similar approach, if the element in the least or most position matches condition and has count 1, it is correct.
correct = 0
for entry in dataset:
    counting, alpha, pword = entry.split()
    least, most = map(int, counting.split("-"))
    s = pword[least - 1] + pword[most - 1]
    if s.count(alpha[0]) == 1:
        correct += 1

print("Number of updated correct passwords: ")
print(correct)
