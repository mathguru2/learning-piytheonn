def factorial(arg1):
    sum=1
    if int(arg1)==arg1 and arg1>0:
        for i in range(arg1):
            sum=sum*i
    else:
        print("You need to enter an integer")
    print(sum)