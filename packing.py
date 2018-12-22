# Create a list of all of the things I need to pack for SaS.
# Figure out a way to randomly generate one thing every time I hit enter.
# I pack whatever pops up. After it pops up, I enter True or False for whether I packed it or not.
# If True, have the item be taken off of the list. If False, have the item be shuffled back in.
import random
clothes = (['undergarments', 'pants','tshirts','hoodie','sweater','jacket','rain jacket','shoes','watch','hats', 'scarf', 'swimwear','formal'])
electronics = (['camera', 'USB', 'charging adapter', 'headphones', 'flashlight', 'gopro', 'macbook'])
toiletries = (['shampoo', 'conditioner', 'toothbrush', 'toothpaste', 'mouthwash', 'deoderant', 'comb', 'pomade', 'contacts', 'contact solution', 'glasses', 'razor'])
medical = (['prescriptions', 'tylenol', 'melatonin', 'first aid kid',])
print clothes + electronics + toiletries + medical
print (len(clothes + electronics + toiletries + medical))