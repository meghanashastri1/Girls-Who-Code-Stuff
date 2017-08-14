import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
print(countries[1])
print(countries)


user_input = input("Enter a country: ")
there = "{} was found!" .format(user_input)
not_there = "{} was not found." .format(user_input)
low = 0
high = length - 1
pivot = len(countries)//2

found = False

if found:
    user_input == pivot
    print (there)

not_found = True

while (low <= high):
    if user_input == pivot:
        print (not_there)
    elif (pivot > user_input):
        high = pivot - 1
    elif (pivot < user_input):
        low = pivot + 1
    else:
        found = True
        break

print(not_true)

# Start your search algorithm here.
