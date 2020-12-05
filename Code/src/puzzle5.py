#  id =  996731-20201201-c7599a1b
# @author : Srinjana Pathak

raw_data = open("E:\Scripts\Python Scripts\AOC\Advent of code 2020\Code\input\input_d5.txt").read(
).strip().split("\n")

# Processing Raw data to find the row and column of ticket position. front stores front and back info and side stores left and right info

def solve(ticket):
    front = ticket[:-3]
    side = ticket[-3:]

    row = 0
    col = 0

    for i, passes in enumerate (front[::-1]):
        row += 2 ** i if passes == 'B' else 0

    for i, passes in enumerate(side[::-1]):
        col += 2 ** i if passes == 'R' else 0

    return (row, col)

#  PART 1
# we compute ID from seat row and col and print the max value

print("Maximum ticket ID is :")
print (max(solve(passes)[0] * 8 + solve(passes)[1] for passes in raw_data))

# PART 2
# Finding my ticket id searches for missing IDs and returns the middle one as it isn't a front or back seat. 
# sorting IDs and putting missing ones in absent list and printing the mid val
boarding = sorted(solve(passes)[0] * 8 + solve(passes)[1] for passes in raw_data)
absent = []

for passes in range(8 * 128):
    if passes not in boarding:
        absent.append(passes)

for passes in absent:
    if passes + 1 in boarding and passes -1 in boarding:
        print("Your ticket Id is: ")
        print(passes)
                
