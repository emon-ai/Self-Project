def calculator():
    import math
    pi = math.pi
    operation=input("Press 1 for Basic Operations\nPress 2 for Scientific Operations\n")
    if operation=="1":
        basic=input("Select operator:\nPress 1 for addition(+)\nPress 2 for subtraction(-)\nPress 3 for multiplication(×)\nPress 4 for division(÷)\n")
        if basic=="1":
            num1 = float(input("What is your first number: "))
            num2 = float(input("What is your second number: "))
            print(num1,"+",num2,"=",(num1+num2),"\n")
        elif basic=="2":
            num1 = float(input("What is your first number: "))
            num2 = float(input("What is your second number: "))
            print(num1,"-",num2,"=",(num1-num2),"\n")
        elif basic=="3":
            num1 = float(input("What is your first number: "))
            num2 = float(input("What is your second number: "))
            print(num1,"x",num2,"=",(num1*num2),"\n")
        elif basic=="4":
            num1 = float(input("What is your first number: "))
            num2 = float(input("What is your second number: "))
            print(num1,"÷",num2,"=",(num1/num2),"\n")
        else:
            print("Invalid!")
    elif operation == "2":
        scintific=input("Select operation:\nPress 1 for Power\nPress 2 for Root\nPress 3 for Trigonometric operation\nPress 4 for Logarithm\n")
        if scintific=="1":
            base=float(input("What is your base number: "))
            power=float(input("What is your power number: "))
            print(base,"^",power,"=",math.pow(base,power))
        elif scintific=="2":
            base =float(input("What is your base number: "))
            power =float(input("What is your root number: "))
            print(power,"√",base,"=",base**(1/power))
        elif scintific=="3":
            trigon=input("Select operation:\nPress 1 for Sine\nPress 2 for Cosine\nPress 3 for Tangent\nPress 4 for Anti-Sine\nPress 5 for Anti-Cosine\nPress 6 for Anti-Tangent\n")
            if trigon=="1":
                angle = float(input("What is your angle: "))
                print("sin(%f)="%angle,(math.sin((angle*pi)/180)))
            if trigon == "2":
                angle = float(input("What is your angle: "))
                print("cos(%f)=" % angle, (math.cos((angle * pi) / 180)))
            if trigon=="3":
                angle = float(input("What is your angle: "))
                print("tan(%f)="%angle,(math.tan((angle*pi)/180)))
            if trigon=="4":
                angle = float(input("What is your angle: "))
                print("sin^-1(%f)="%angle,(math.asin((angle*pi)/180)))
            if trigon=="5":
                angle = float(input("What is your angle: "))
                print("cos^-1(%f)="%angle,(math.acos((angle*pi)/180)))
            if trigon=="6":
                angle = float(input("What is your angle: "))
                print("tan^-1(%f)="%angle,(math.atan((angle*pi)/180)))
        elif scintific=="4":
            logarithm=input("Select operation:\nPress 1 for log\nPress 2 for ln\n")
            if logarithm=="1":
                num=float(input("What is your number: "))
                lbase=int(input("What is your base: "))
                print("log",num,"base",lbase,"=",math.log(num,lbase))
            if logarithm=="2":
                lnum=float(input("What is your number: "))
                print("ln",lnum,"=",math.log(lnum))
        else:
            print("Invalid!")
    else:
        print("Invalid!")
    again()
def again():
    confirm=input("\nDo you want to calculate again?\nPress Y for Yes\nPress N for No\n")
    conf=confirm.replace(" ","")
    if conf.lower()=="y":
        calculator()
    else:
     print("Thank you for using.\nCLOSED!")
calculator()