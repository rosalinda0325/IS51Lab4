
"""
This program will allow user 3 attempts to a question:
"What is the capital of California?" . The answer is Sacramento"

There will be a max of 3 tries, a loop will be created 3x.
For each user input it will check if it is a match to the correct answer, if the answer is correct
it will print "Correct!" and terminate the loop.

If user is unable to guess the correct answer within the 3 times it will print
"You have used up all of your guesses.", "The correct answer is California."
"""


"""
main
question "Capital of california"
answer = "sacramento"
ask(question, answer)


ask
tries =0
loop 3x
    tries increment
    ask user input
    answer= user input
    if true print correct
    brek
    elif
    print "you have used all your guesses the correct answer is sacramento"

call main function



"""


def main():
    question = "What is the capital of California?"
    answer = "Sacramento"
    ask(question, answer)


def ask(question, answer, max_tries=3):
    tries = 0
    while tries < max_tries:
        tries = tries + 1
        ans = input(question)
        if ans == answer:
            print ("Correct!")
            break
    if ans != answer:
        print("You have used all your guesses. The correct answer is Sacramento")
      
main()
