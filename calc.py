import os 
while True:
    print("select a number")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Division")
    print("4.Modulo")
    print("5.Multiplication")
    print("6.Exit")
    match(input('enter your choice : ')):
     case '1':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(a+b)
     case '2':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(a-b)
     case '3':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(a/b)
     case '4':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(a%b)
        
     case '5':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(a*b)
     case '6':
        print('exiting')
        break
     case _ :
        print("Invalid choice")
    
    input("press enter to continue")
    os.system("clear")


    
    