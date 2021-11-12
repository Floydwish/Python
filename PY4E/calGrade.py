def computeGrade(): 
    try:
        score = input("Enter Score: ")
        s=float(score)
        r=''
        if (s<0.0 or s>1.0):
            print("Error input, please enter a number between 0.0 to 1.0")
        elif s>=0.9:
            r='A'
        elif s>=0.8:
            r='B'
        elif s>=0.7:
            r='C'
        elif s>=0.6:
            r='D'
        elif s<0.6:
        	r='F'
        print(r)
    except:
        print("bad score")

computeGrade()