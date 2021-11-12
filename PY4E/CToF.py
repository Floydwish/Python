def convertCToF():
	try:
		C=input("Enter Celsius temperature: ")
		F=float(C)*1.8+32
		print("Fahrenheit: %.2f" % F)
	except:
		print("Please enter a number")

convertCToF()