
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
question = "what is the capital of California"
answer = "sacramento"
ask(question, answer)

ask
tries =0
tries + 1
ask user input
user input = to answer
if true print "correct"
elif
print "you have used all your guesses. the correct answer is sacramento"


main
"""


def main():
    question = "What is the capital of California? "
    answer = "Sacramento"
    ask(question, answer)



def ask(question, answer, max_tries=3):
    tries = 0
    ans = ""
    while tries < max_tries:
        tries += 1
        ans = input(question)
        if ans == answer:
            print("Correct!")
            break
    if ans != answer:
        print("You have used all your guesses the correct answer is Sacramento")


main()

