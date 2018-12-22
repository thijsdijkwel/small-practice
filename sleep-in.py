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
		
