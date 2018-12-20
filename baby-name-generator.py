import string
# print (help(string)) if you want to see what it does
print(string.ascii_letters)
print(string.ascii_lowercase)

import random
#print(random.choice('pull a letter from here'))
#print(random.choice(string.ascii_lowercase))

def generator():
	letter1 = random.choice(string.ascii_lowercase)
	letter2 = random.choice(string.ascii_lowercase)
	letter3 = random.choice(string.ascii_lowercase)
	letter4 = random.choice(string.ascii_lowercase)
	letter5 = random.choice(string.ascii_lowercase)
	name = letter1+letter2+letter3+letter4+letter5
	return(name)

print(generator())

letter_input_1 = input ('Choose a letter ... "v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_2 = input ('Choose a letter ... "v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_3 = input ('Choose a letter ... "v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_4 = input ('Choose a letter ... "v" for vowels, "c" for consonants, "l" for any other letter')
letter_input_5 = input ('Choose a letter ... "v" for vowels, "c" for consonants, "l" for any other letter')

vowel = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_lowercase

# letter 1
if letter_input_1 == "v": 
	letter1=random.choice(vowels)
elif letter_input_1 == "c":
	letter1=random.choice(consonants)
elif letter_input_1 =="l":
	letter1+random.choice(letter)
else:
	letter1=letter_input_1
# letter 2
if letter_input_2 == "v": 
	letter2=random.choice(vowels)
elif letter_input_2 == "c":
	letter2=random.choice(consonants)
elif letter_input_2 =="l":
	letter2=random.choice(letter)
else:
	letter2=letter_input_2
# letter 3 
if letter_input_3 == "v": 
	letter3=random.choice(vowels)
elif letter_input_3 == "c":
	letter3=random.choice(consonants)
elif letter_input_3 =="l":
	letter3=random.choice(letter)
else:
	letter3=letter_input_3
# letter 4
if letter_input_4 == "v": 
	letter4=random.choice(vowels)
elif letter_input_4 == "c":
	letter4=random.choice(consonants)
elif letter_input_4 =="l":
	letter4=random.choice(letter)
else:
	letter4=letter_input_4
# letter 5
if letter_input_5 == "v": 
	letter5=random.choice(vowels)
elif letter_input_5 == "c":
	letter5=random.choice(consonants)
elif letter_input_5 =="l":
	letter5=random.choice(letter)
else:
	letter5=letter_input_5
name = letter1+letter2+letter3+letter4+letter5
print (generator)

for babynames in range(20):
	print(generator())
