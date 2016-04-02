def km_miles():
	km = float(input('Enter distance in kilometers: '))
	print km / 1.609
def miles_km():
	miles = float(input('Enter distance in miles: '))
	print miles * 1.609
def print_menu():
	print "1. Kilometers to Miles"
	print "2. Miles to Kilometers"
	choice = input("Which conversion would you like to do?")
	if choice == 1:
		km_miles()
	elif choice == 2:
		miles_km()

print_menu()