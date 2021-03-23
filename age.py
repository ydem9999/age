drive = input('Have you driven before?')
if drive != 'yes' and drive != 'no':
	print('Please answer with yes or no.')
	raise SystemExit
age = input('How old are you?')
age = int(age)
if drive == 'yes':
	if age >= 18:
		print('Ok, you passed.')
	else:
		print('Dude, you are not allowed to drive')
elif drive == 'no':
	if age >= 18:
		print('You can drive, please take the driving test.')
	else:
		print('Wait for couple more years.')