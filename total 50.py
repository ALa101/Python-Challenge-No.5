"""
Set the total to 0 to start with.
While the total is 50 or less,
ask the user to input a number.
Add that number to the total and print the message
“The total is… [total]”.
Stop the loop when the total is over 50.
Upload program to GitHub and past the link.

"""
total = 0 #
while total.__le__(50):
    try:
        num = int(input("Enter a number :-> "))
    except:
        print("Something went wrong\npleace sure input number")
        break
    total += num
    print("The total is...[" + str(total) + "]")
if total >= 50:
    print("the Tooal is over 50 ^_^ ".center(30))
print("Thank you ^_^".center(30))
