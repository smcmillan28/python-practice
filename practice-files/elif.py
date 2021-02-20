# num = 28
# guess = int(input("Enter an number: "))

# if guess == num:
#     print("Congrats!  You guessed it.")
# elif guess < num:
#     print("Oops... a little higher.")
# else:
#     print("Sorry!  You're too high.")

# print("Done.")

whileNum = 32
running = True

while running:
    newGuess = int(input("Enter a number: "))

    if newGuess == whileNum:
        print("Congrats!  You guessed it.")
        running = False
    elif newGuess < whileNum:
        print("Oops... a little higher.")
    else:
        print("Sorry!  You're too high.")

else:
    print("The while loop is over.")

print("Done.")

print("-----------")

for i in range(1, 5):
    print(i)
else:
    print("The for loop is over.")

        