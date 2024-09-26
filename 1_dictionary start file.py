import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

'''

print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)

print(len(phonebook))

mydict = {}

print(mydict)

mydict= dict(m=8, n=9)

print(mydict)



print()
print('*****  end section 1 ********')
print()


'''


print()
print('*****  start section 2 - search dictionary ********')
print()

phone = phonebook['Chris']
print(phone)

#if you want to do an if statement to see what is wrong

#name = "Chris"

#if name in phonebook:
    #phone = phonebook[name]
    #print(phone)
#else:
    #print(f"{name} is not in the phonebook")

#print(type(phonebook['Chris']))



print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook["Joe"] = '555-0123'
phonebook['Chris'] = '555-4444'
print(phonebook)




print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook['Chris']
print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:
    print(f"The name is {key} and the phone number is {phonebook[key]}")

for value in phonebook.values():
    print(f"Phone number: {value}")

for item in phonebook.items():
    print(item)

#for key, value in phonebook.items():
   # print(f"The name is {key} and the phone number is {phonebook[value]}")


print()
print('*****  end section 5 ********')
print()

phone = phonebook.get('chris', '555-0000')
print(phone)

phonebook.clear()
print(phonebook)

print()
print('*****  start section 6 - using get and clear ********')
print()






print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()


phone = phonebook.pop('Chris', 'not found')
print(phone)
print(phonebook)



print()
print('*****  end section 7 ********')
print()

'''

print()
print('*****  start section 8 - using popitem ********')
print()

a = phonebook.popitem()
print(a)
print(phonebook)




print()
print('*****  end section 8 ********')
print()

'''

print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
random_key = random.choice(list_of_keys)
phone = phonebook(random_key)
print(f"the key is {random_key} and the phone number is {phone}")


phone = phonebook[random.choice(list(phonebook))]


print()
print('*****  end section 9 ********')
print()








