import random
number = random.randint(1,10)
tries = 0
win = False # setting a win flag to false

name = input ("hello, what is your name?")
print ('hello' + name)

question = input('Would you like to play a game? [Y/N]')
if question.lower() == 'n':
	print ("You are a loser by default")
if question.upper() == 'N':
	print ('You are a loser by default')
if question.lower() == 'y':
	print ('I am thinking of a number between 1 and 10')
if question.upper() == 'Y':
	print ('I am thinking of a number between 1 and 10')

while not win:
	guess = int(input('Have a guess'))
	tries = tries + 1 
	if guess == number:
		win = true
		print ('Congrats, You guessed the number correctly.')
	elif guess < number:
		win = false
		print ('Close! Guess higher')
	elif guess > number:
		win = false
		print ('Close! Guess lower')
	# for some reason, everything from this point doesn't work. an error on line 31 pops up at 2
	# and I think that it will pop up on each one after so on 3,4, and 4. not sure why.
	elif tries < 2:
		print ('You won $100,000!')
	elif tries < 3:
		print ('You won $50,000!')
	elif tries < 4:
		print ('You won $25,000!')
	elif tries > 4:
		print ('You didn\'t win any money. Better luck next time!')
