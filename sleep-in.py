weekday = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')
vacation = ('New Year\'s', 'Valentines', 'President\'s Day', 'Labor Day', 'Halloween', 'Christmas')
def sleep_in(weekday, vacation):
	if not weekday == False or vacation == True:
		return True
	else:
		return False
# you can also do:
def sleep_in(weekday, vacation):
	if not weekday or vacation:
		return True
	else:
		return False
# or
def sleep_in(weekday, vacation):
	if weekday == True and vacation == False:
		return False
	else: 
		return True

wake_up = False
if wake_up == False:
	print ('You can\'t sleep in today!')
elif wake_up == True:
	print ('Go back to sleep, you get to sleep in!')