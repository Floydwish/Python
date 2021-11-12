def calpay():
	try:
		hours=input("Enter hours: ")
		h= float(hours)
		rate=input("Enter rate: ")
		r=float(rate)
		pay=0.0
		if h>40:
			pay=40*r+(h-40)*(r*1.5)
		else:
			pay=h*r
		print("Pay: %.2f" % pay)
	except:
		print("Error, please enter numeric input")
	
calpay()



