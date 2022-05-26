#Simple CLI calculator

is_running = True

while is_running:
    print("Lets Calculate")
    userInput = input("What operation would you like to perform?\nPick any of ['+','-','*','/','%'] : ")

    try:

        no1 = float(input("First number: "))
        no2 = float(input("Second number: "))

    except:
        print("Failed, Invalid entry")
        continue

    if userInput =="+":
       #perform addition
       print(no1 + no2)

    elif userInput =="-":
       #perform subtraction
       print(no1 - no2) 

    elif userInput =="*":
       #perform multiplication
       print(no1 * no2)

    elif userInput =="/":
       #perform division
       print(no1 / no2)
 
    elif userInput =="%":
       #perform modulus
       print(no1 % no2)

    else:
        #Invalid Operation
        print ("Invalid operation entered, try again...")

    choice = input("Would you like to run another calculation? [y,n] :")
    if choice == "y":
        pass
    if choice == "n":
        is_running = False

    print("Math is easy, don\'t you think so? Bye...")




