low = 1
high = 1000
print("please think of numbers between{} and {}".format(low,high))
input("Press Enter to Start")
guesses = 1
while True:
    guess = low + ( high - low ) // 2
    high_low = input("my guess is{}.should I gess high or lower?"
                     "enter h or l or c guess was correct".format(guess).casefold())
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print( " I got in {} guess")
        break
    else:
        print("please enter h, l or c")
    guesses = guesses + 1

