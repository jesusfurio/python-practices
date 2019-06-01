def two_fer(name):
	if name == None:
		return 'One for you, one for me.'
	else:
		return 'One for {}, one for me.'.format(name)