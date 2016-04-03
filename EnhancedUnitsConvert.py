def km_miles():
	km = float(input('Enter distance in kilometers: '))
	print km / 1.609

def miles_km():
	miles = float(input('Enter distance in miles: '))
	print miles * 1.609

def kgs_lbs():
	kgs = float(input('Enter mass in kilograms: '))
	print kgs * 2.20462

def lbs_kgs():
	lbs = float(input('Enter mass in pounds: '))
	print lbs * 0.453592

def c_f():
	c = float(input('Enter temperature in Celsius: '))
	print (c * 1.8) + 32

def f_c():
	f = float(input('Enter temperature in Fahrenheit: '))
	print (f - 32) * 0.5556 

def print_menu():

	print "1. Distance"
	print "2. Mass"
	print "3. Temperature"
	selection = input ('Which type of conversion do you want to do?')

	if selection == 1:
		print "1. Kilometers to Miles"
		print "2. Miles to Kilometers"
		choice = input("Which conversion would you like to do?")
		if choice == 1:
			km_miles()
		elif choice == 2:
			miles_km()

	elif selection == 2:
		print "1. Kilograms to Pounds"
		print "2. Pounds to Kilograms"
		choice = input("Which conversion would you like to do?")
		if choice == 1:
			kgs_lbs()
		elif choice == 2:
			lbs_kgs()

	elif selection == 3:
		print "1. Celsius to Fahrenheit"
		print "2. Fahrenheit to Celsius"
		choice = input("Which conversion would you like to do?")
		if choice == 1:
			c_f()
		elif choice == 2:
			f_c()

print_menu()