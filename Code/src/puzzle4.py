#  id =  996731-20201201-c7599a1b
# @author : Srinjana Pathak

# Parsing input and processing it to make it readable by functions
# the data is split into a key-val pair dict() finally, along with each pass
raw_data = open("..\Code\input\input_d4.txt").read(
).strip().split("\n")

for i in range(len(raw_data)):
    if raw_data[i] == "":
        raw_data[i] = "\n"

rawPassports = " ".join(raw_data).split(" \n ")

# print(rawPassports)

passports = []
for rawPassport in rawPassports:
    passport = dict()
    for kvp in rawPassport.split():
        k, v = kvp.split(":")
        passport[k] = v

    passports.append(passport)

# PART 1
# (checking if all necessary fields are present in the particular password with the exception of 'cid')

cond1 = [
    lambda pp: all(field in pp for field in [
                   "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
]

def isValid1(passport):
    return all(check(passport) for check in cond1)

result1 = sum(isValid1(passport) for passport in passports)
print("All valid passports: {}".format(result1))

# PART 2
# (checking the given constraints in each field and if all are satisfied, along with the earlier condition, the passport is valid)

cond2 = [
    lambda pp: 1920 <= int(pp["byr"]) <= 2002,
    lambda pp: 2010 <= int(pp["iyr"]) <= 2020,
    lambda pp: 2020 <= int(pp["eyr"]) <= 2030,
    lambda pp: (pp["hgt"][-2:] == "cm" and 150 <= int(pp["hgt"][:-2]) <= 193) or
               (pp["hgt"][-2:] == "in" and 59 <= int(pp["hgt"][:-2]) <= 76),
    lambda pp: pp["hcl"][0] == "#" and all(
        c in "0123456789abcdef" for c in pp["hcl"][1:]),
    lambda pp: pp["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    lambda pp: len(pp["pid"]) == 9 and all(
        c in "0123456789" for c in pp["pid"])
]

def isValid2(passport):
    return isValid1(passport) and all(check(passport) for check in cond2)

result2 = sum(isValid2(passport) for passport in passports)
print("All Acceptable passports: {}".format(result2))
