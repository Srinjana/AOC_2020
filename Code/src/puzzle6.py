#  id =  996731-20201201-c7599a1b
# @author : Srinjana Pathak


from collections import Counter

# parsing Input and splitting into lists based on blank lines
data = open("E:\Scripts\Python Scripts\AOC\Advent of code 2020\Code\input\input_d6.txt").read(
).split("\n\n")

# part 1 solution
# counting the unique different chars in each set and adding them together
def first():
    sum_counts = 0

    for line in data:
        questions = set(char for char in line if char != '\n')
        sum_counts += len(questions)

    return(sum_counts)

print(first())

# part 2 solution
# we split the list further down and check for any reapeating alphabets. if it does not occur in all sets, its not a valid answer
# we do the checking by counting the number of items in the list in total and subtracting the invalid conditions from it.
def second():
    new_counts = 0

    for line in data:
        x = len(line.split())
        # print(x)
        c = Counter(line)
        new_counts += sum(v == x for _, v in c.items())

        if c['\n'] == x:
            new_counts -= 1

    return(new_counts)

print(second())
