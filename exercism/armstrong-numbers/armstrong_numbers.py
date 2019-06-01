def is_armstrong_number(number):
	return sum((int(i) ** len(str(number)) for i in str(number))) == number


