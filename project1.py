# tuple is very important when trying to store data of relative attributes
# it more useful than list and dictrionary becauase they can save data that are related to eachother.

# asumming we want to store names of students and thier ages together without mixing each students name and age.
# tuple is more useful than list in this aspect
studData = [
    ('Qudus', 27),
    ('Daneil', 19),
    ('Joe', 23)
]

for name, age in studData:
    # this print each students information
    print(f'{name} is {age} years old')

print('======= zip function =======')

# the zip function is used to zip 2 lists together..
# Suppose the above data was in 2 parallel lists:

names = ['Qudus', 'Daneil', 'Joe']
ages = [27, 19, 23]

# then we can print same output using below syntax:
for (name, age) in zip(names, ages):
    print(name, 'is ', age, ' years old')

print('======= enumerate function =======')

# The enumerate function assigns the indices to individual elements of list..
# If we wanted to give a index to each student, we could do below:

for (index, name) in enumerate(names):
    # to start the index from 1
    print(index+1, ':', name)

print('======= items method =======')

# The items method is used in dictionary, Where it returns the key value pair of
# the dictionary in tuple format

# If the above tuple list was in dictionary format like below:

ageDict = {'Jack': 11, 'Rochell': 20, 'Amy': 45}

# Then using the dictionary, we can print same output with below code:

for (name, age) in ageDict.items():

       print(name, 'is ', age, 'years old')

