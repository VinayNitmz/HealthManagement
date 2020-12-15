#Health mangement system
#currently for 3 but can be updated as required

def getdate():
    import datetime
    return datetime.datetime.now()

def inputdata():
    """
    For Updating data to files
    :return:
    """
    print("Welcome to Health Management System")
    name = input("Here is a list of our Members if your name is visible below, kindly enter your name to input your data else press 'No' to become a Member otherwise press any key to exit.:\n 1 Aman\n 2 Jon\n 3 Jay \n")
    if name == 'Aman':
        f = open("Aman.txt","a+")
        i = input("What would you like to do log a Exercise or Diet \n")

        if i == "Exercise":
            print("Enter your exercise \n")
            f.write('Exercise: \n')
            E = f.write(str([str(getdate())])+":"+input("Exercise: "))
            f.write('\n')
            print("Data updated\n")
            rd = input("Would you like to see your till date history if so press 'Y' else press any key\n")
            if rd == "Y":
                getdata()
            else:
                print("Thank You Have a Nice Day")



        elif i == "Diet":
            print("Enter your Diet \n")
            f.write('Diet: \n')
            D = f.write(str([str(getdate())]) + ":" + input("Diet: "))
            f.write('\n')
            print("Data updated")
            rd = input("Would you like to see your till date history if so press 'Y' else press any key\n")
            if rd == "Y":
                getdata()
            else:
                print("Thank You Have a Nice Day")

        else:
            print("Invalid Input")

        f.close()
    elif name == 'Jon':
        f = open("Jon.txt", "a+")
        i = input("What would you like to do log a Exercise or Diet \n")

        if i == "Exercise":
            print("Enter your exercise \n")
            f.write('Exercise: \n')
            E = f.write(str([str(getdate())]) + ":" + input("Exercise: "))
            f.write('\n')
            print("Data updated")
            rd = input("Would you like to see your till date history if so press 'Y' else press any key\n")
            if rd == "Y":
                getdata()
            else:
                print("Thank You Have a Nice Day")

        elif i == "Diet":
            print("Enter your Diet \n")
            f.write('Diet: \n')
            D = f.write(str([str(getdate())]) + ":" + input("Diet: "))
            f.write('\n')
            print("Data updated")
            rd = input("Would you like to see your till date history if so press 'Y' else press any key\n")
            if rd == "Y":
                getdata()
            else:
                print("Thank You Have a Nice Day")

        else:
            print("Invalid Input")

        f.close()

    elif name == 'Jay':
        f = open("Jay.txt", "a+")
        i = input("What would you like to do log a Exercise or Diet \n")

        if i == "Exercise":
            print("Enter your exercise \n")
            f.write('Exercise: \n')
            E = f.write(str([str(getdate())]) + ":" + input("Exercise: "))
            f.write('\n')
            print("Data updated")
            rd = input("Would you like to see your till date history if so press 'Y' else press any key\n")
            if rd == "Y":
                getdata()
            else:
                print("Thank You Have a Nice Day")

        elif i == "Diet":
            print("Enter your Diet \n")
            f.write('Diet: \n')
            D = f.write(str([str(getdate())]) + ":" + input("Diet: "))
            f.write('\n')
            print("Data updated")
            rd = input("Would you like to see your till date history if so press 'Y' else press any key\n")
            if rd == "Y":
                getdata()
            else:
                print("Thank You Have a Nice Day")

        else:
            print("Invalid Input")

        f.close()
    elif name== "No":
        print("Thank you for your interest we will get in touch with you soon kindly leave your details")
        name = input("Enter Your Name: ")
        mobile = input("Enter Your Phone Number: ")
        f3 = open("newmember.txt", "a+")
        f3.write("\n")
        f3.write(str([str(getdate())])+":"+name)
        f3.write("\n")
        f3.write(str([str(getdate())]) + ":" + mobile)
        f3.write("\n")
        print("\n Thank You for giving your time your data will be updated soon")
        f3.close()
    else:
        print("Thank you for visting \nHope to see you soon")



def getdata():
    """
    For retrieving data from files
    :return:
    """
    Dis = input("kindly enter your name \n")
    if Dis == "Aman":
        f1 = open("Aman.txt")
        f1data = f1.read()
        print(f1data)

    elif Dis == "Jay":
        f1 = open("Jay.txt")
        f1data = f1.read()
        print(f1data)
    elif Dis == "Jon":
        f1 = open("Jon.txt")
        f1data = f1.read()
        print(f1data)

    else:
        print("Currently no data available will get in touch with you shortly. \nThank You for your interest")


inputdata()
print("For any further assistant get in touch with us on 9999999999")

