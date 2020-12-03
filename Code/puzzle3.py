#  id =  996731-20201201-c7599a1b
# @author : Srinjana Pathak

# PART 1 

#we read the given input splitting them by newlines ('\n')
data = open("..\Code\input_d3.txt").read().strip().split('\n')
# print(data)

curr_x = 0
curr_y = 0
result = 0

# starting from top left we go down until the end of the given data. (right 3, down 1)
while curr_y < len(data):
    if data[curr_y][curr_x % len(data[curr_y])] == '#':
        result += 1
    
    curr_y += 1          #right
    curr_x += 3          #down

print(result)

# PART 2
# we need to multiply several trajectories, so using a function is more reasonable
# the base logic of counting the encounters with "#" (trees) remains the same.

def data(right,down):
    data = open("E:\Scripts\Python Scripts\AOC\Advent of code 2020\Code\input_d3.txt").read(
    ).strip().split('\n')

    curr_x, curr_y = 0, 0
    result = 0

    while curr_y < len(data):
        if data[curr_y][curr_x % len(data[0])] == '#':
            result += 1
        curr_x += right
        curr_y += down
    return result

print(data(1,1) * data(3,1) * data(5,1) * data(7,1) * data(1,2))


