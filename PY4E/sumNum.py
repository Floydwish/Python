'''
Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. 
Once “done” is entered, print out the total, count, and average of the numbers. 
If the user enters anything other than a number, 
detect their mistake using try and except and print an error message and skip to the next number.

example:
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
'''
'''
def sumNum():
    try:
        count=0
        sum=0
        while(True):
            num=input("Enter a number:")
            if (num=="done"):
                break
            else:
                count+=1
                n=int(num)
                sum+=n
        print("%d %d %f" %(sum, count, sum/count))
    except:
        print("bad data")
'''

def sumNum():
    count=0
    sum=0
    while(True):
        try:
            num=input("Enter a number:")
            if (num=="done"):
                break
            else:
                n=int(num)
                count+=1
                sum+=n
        except:
            print("bad data")
            continue
    print("%d %d %f" %(sum, count, sum/count))
    
       

sumNum()


