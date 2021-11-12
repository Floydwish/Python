def computepay(h, r):
    pay=0.0
    try:
        if (h>40):
            pay=40*r+(h-40)*1.5*r
        else:
            pay=h*r
    except:
        print("wrong input")
    return pay
    

hrs = input("Enter Hours:")
h=float(hrs)
p = computepay(h, 10.5)
print("Pay", p)