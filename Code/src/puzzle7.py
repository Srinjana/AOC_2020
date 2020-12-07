#  id =  996731-20201201-c7599a1b
# @author : Srinjana Pathak

data = open("E:\Scripts\Python Scripts\AOC\Advent of code 2020\Code\input\input_d7.txt").read(
).strip().split("\n")

# An empty dict to stor all the bags that allow a shiny gold bag
allowed = {}

# processing input to isolate the color and bags allowed in it
for line in data:
    color, contains = line.split(' bags contain ', 1)
    allowed[color] = contains

prev_res = []
result = ['shiny gold']

# every time we encounter a bag that allows shiny gold we keep adding an element to the result list. and print the total number of times it appears later.

while list(set(prev_res)) != list(set(result)):
    prev_res = result.copy()
    for color in result:
        for key, val in allowed.items():
            if color in val:
                result.append(key)

# subtracrting 1 because the list was initialized with an extra element
print(len(list(set(result))) - 1)

#  removing unwanted text from input
def remove(s, t):
    return ''.join(s.split(t))

# parsing only valid data into the final dict. by removing other terms and spaces.
def parse(s):
    if 'no other bags.' == s: return []
    return [bag.split(' ', 1) for bag in remove(remove(s.strip('.'), ' bags'), ' bag').split(', ')]


def calculate(s):
    # contains data of all bags that allow further nesting
    bags = parse(allowed[s])
    res = 1
    # count the number of bafs that can be supported by another bag by this recursive func.
    for n, typ in bags:
        res += int(n) * calculate(typ)
    return res

# subtracting 1 since the initial value of res was 1
print(calculate('shiny gold') - 1)
