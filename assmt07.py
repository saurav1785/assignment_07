# ASSIGNMENT -7
# Question-1: Create user defined dictionary and print keys and value
# Answer
dict1 = {}
i = 1
while i != 0:
    key = input('enter the key value ')
    value = input('enter the value for corresponding key: ')
    dict1[key] = value
    i = int(input('enter 0 to print dictionary otherwise anything to continue'))
print(dict1)

# Quesion-2: Nested dictionary
# Answer
records = {'Saurav':{'Science':70,'Maths':75,'English':85},'Richa':\
         {'Science':86,'Maths':85,'English':98},'Sumit':\
         {'Science':72,'Maths':100,'English':84}}
name = input("Enter the name: ")
for key in records:
    if name == key:
        print(key, records[key])
