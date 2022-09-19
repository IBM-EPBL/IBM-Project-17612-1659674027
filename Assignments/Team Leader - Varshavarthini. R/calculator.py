while(1):
    a=input("enter the expression (type c to exit) : ")
    if a=='c':
        break
    else:
        print("\n answer: {}".format(eval(a)))
