"""
Create a program that will allow the user to easily manage a list of names.
 You should display a menu that will allow them to
    add a name to the list,
    change a name in the list,
    delete a name from the list
    or view all the names in the list.
There should also be a menu option to allow the user to
    end the program.
If they select an option that is not relevant, then it should display a suitable message.
After they have made a selection to either
   add a name, change a name, delete a name or view all the names,
they should see the menu again without having to restart the program.
The program should be made as easy to use as possible.
Upload the program in word file

"""


def addName():
    clearConsole()
    try:
        num_of_add = int(input("How many do you want to add : ".rjust(20)))
    except:
        print('Something went wrong\npleace sure input number')
        enter()
    for i in range(num_of_add):
        names.append(input(str(i + 1) + "-Enter the name  (" + str(i + 1) + ") :"))
    print("-".center(80, "-"))
    view()
    print("\n" + "successful added ^_^".center(80))
    enter()


def changName():
    clearConsole
    view()
    print("chose name that do you want to chang ? ".center(50))
    namechang = input("Enter the id name or name :> ".rjust(20))
    if namechang.isnumeric():
        index = int(namechang) - 1
    else:
        try:
            index = names.index(namechang)
        except:
            print("This name not found -_- .")
            enter()
    newname = input("Enter the new name :>".rjust(20))
    names.pop(index)
    names.insert(index, newname)
    print(" ".center(80, "-"))
    print("successful chang ^_^".center(80))
    view()
    enter()


def delName():
    clearConsole
    view()
    print("chose name that do you want to Delete ? ".center(50))
    namechang = input("Enter the id name or name :> ")
    if namechang.isnumeric():
        index = int(namechang) - 1
    else:
        try:
            index = names.index(namechang)
        except:
            print("This name not found -_- .".center(80))
            enter()
    names.pop(index)
    print(" ".center(80, "-"))
    print("successful deleted ^_^".center(80))
    view()
    enter()


def view(e=0):
    print("list of the names".center(80, "-"))
    if len(names) == 0:
        print("empty list ...")
    else:
        for i in range(len(names)):
            print(str(i + 1) + "." + names[i], end="  ")
        print("\n")
    if e == 1:
        enter()


def enter():
    print(" ".center(80, "-"))
    ch = input("press [Enter] to back the menu or any character to [Exit]  ".center(100, '*'))
    if ch == "":
        clearConsole()
        menu()
    else:
        exit()


clearConsole = lambda: print('\n' * 10)


def easily_manage():
    global names
    names = []
    global clearConsole, enter
    print("Hello ,This program For you to easy manage".center(80, "^"))
    menu()


def menu():
    print("menu option :".rjust(20))
    print("""           1.add a name.
           2.change a name.
           3.delete a name.
           4.view all the names.
           5.End""")
    ch = int(input("Enter your chose  : "))
    if ch == 1:
        addName()
    elif ch == 2:
        changName()
    elif ch == 3:
        delName()
    elif ch == 4:
        view(1)
    elif ch == 5:
        print("Thank you ^_^")
        exit()
    else:
        print("Sorry, please choose from the menu")
        menu()


# Start program
easily_manage()
