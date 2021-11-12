'''
Exercise 2: Write another program that prompts for a list of numbers as above and 
at the end prints out both the maximum and minimum of the numbers instead of the average.

'''

def MaxAndMin():
    maxNum=None
    minNum=None
    while(True):
        try:
            num=input("Enter a number:")
            if (num=="done"):
                break
            else:
                n=int(num)

                if maxNum == None or n>maxNum:
                    maxNum=n
                if minNum==None or n<minNum:
                    minNum=n
        except:
            print("bad data")
            continue
    print("max:%d min:%d" %(maxNum, minNum))


MaxAndMin()



maxNum=None
minNum=None
while(True):
    try:
        num=input("Enter a number:")
        if (num=="done"):
            break
        else:
            n=int(num)

            if maxNum == None or n>maxNum:
                maxNum=n
            if minNum==None or n<minNum:
                minNum=n
    except:
        print("bad data")
        continue