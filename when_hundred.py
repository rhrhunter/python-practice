#solution to practicepython.org exercise 1

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

years_till_100 = 100 - age
year_turn_100 = str(years_till_100 + 2016)

print( name + ", you will be 100 years old in " + year_turn_100)
