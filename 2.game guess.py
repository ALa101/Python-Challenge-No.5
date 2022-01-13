"""
Define a subprogram that will ask the user to pick a low and a high number,
and then generate a random number between those two values
and store it in a variable called “comp_num”.
Define another subprogram that will give the instruction
“I am thinking of a number…”
and then ask the user to guess the number they are thinking of.
Define a third subprogram that
will check to see if the comp_num is the same as the user’s guess.
If it is, it should display the message “Correct, you win”,
otherwise it should keep looping,
telling the user if they are too low or too high and asking them to guess again
until they guess correctly. Upload the program in word file

"""
import random


def comp_num():  # the first subprogram pick a low and a high number,
    global comp_num
    print("pick a low and a high number :".center(80, "*"))
    try:
        num1 = int(input("Enter low number : ".rjust(50)))
        num2 = int(input("Enter high number: ".rjust(50)))
    except:
        print("Something went wrong\nplace sure input number")
    try:
        comp_num = random.randint(num1, num2)
    except:
        print(("You main Low: " + str(num2) + "  and High :" + str(num1)).center(80))
        num1, num2 = num2, num1
        comp_num = random.randint(num1, num2)


def guess(agin=0):  # the second subprogram guess the number they are thinking of.
    global guess_num
    if agin == 0:
        print("I am thinking of a number… *_*  ".center(80,"^"))
        print("Guess the number they are thinking of :".rjust(60), end="")
    else:
        print("Try Try ^_^ ,Enter another number :".rjust(60), end="")
    try:
        guess_num = int(input())
    except:
        print("Something went wrong\nplace sure input number")
        return


def check():  # Third subprogram :guess correctly or not
    while comp_num != guess_num:
        if comp_num > guess_num:
            print("too low -_-  guess again".center(80,"-"))
            guess(1)
        else:
            print("too high -_-  guess again".center(80))
            guess(1)
    else:
        print("Correct, you win ^_^".center(80))


def guessGame():  # Tha main function for the Game
    comp_num()
    guess()
    check()


guessGame()
