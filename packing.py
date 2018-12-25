# Create a list of all of the things I need to pack for SaS.
# Figure out a way to randomly generate one thing every time I hit enter.
# I pack whatever pops up. After it pops up, I enter True or False for whether I packed it or not.
# If True, have the item be taken off of the list. If False, have the item be shuffled back in.
import random

clothes = (['undergarments', 'pants','tshirts','hoodie','sweater','jacket','rain jacket','shoes','watch', 'belts','hats', 'scarf', 'swimwear','formal'])
electronics = (['camera', 'USB', 'charging adapter', 'headphones', 'flashlight', 'gopro', 'macbook', 'calculator',])
toiletries = (['shampoo', 'conditioner', 'toothbrush', 'toothpaste', 'mouthwash', 'deoderant', 'comb', 'pomade', 'anti-wrinkle spray','contacts', 'contact solution', 'glasses', 'razor'])
medical = (['prescriptions', 'tylenol', 'melatonin', 'first aid kid',])
miscellaneous = (['credit cards', 'debit cards', 'cash', 'water bottle', 'beach towel', 'thank you cards', 'packing organizer', 'laundry', 'snacks'])
everything = clothes + electronics + toiletries + medical + miscellaneous

item = random.choice(everything) 
print item
# I think i need to define function, return, and use a boolean 

def packed: 
	return everything.remove(item)
if item == True:
	everything.remove(item)
	print(len(everything))

if item == False:
	print ('shuffling item back into list')
	print(len(everything))

item = True
print(len(everything)) 
