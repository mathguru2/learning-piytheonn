def factorial(arg1):
    tot=1
    if int(arg1)==arg1 and arg1>0:
        for i in range(arg1):
            tot=tot*i
        print(tot)
    else:
        print("You need to enter an integer")

    return tot;
factorial(3)