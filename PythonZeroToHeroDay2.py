''' Word = sentence
Index of characters assigned with prize are : 1,2,4,5,7.
You have to choose only above indices so you can get a prize otherwise not.
Only 'e', or 'n' assigned with prizes'''

Word = "sentence"
print("Choose the correct character of the word",Word,"to win the lottery")
inputs = input(" ")

if inputs == Word[1].lower() or inputs == Word[2].lower() or inputs == Word[4].lower() or inputs == Word[5].lower() or inputs == Word[7].lower():
    print('Congratulations you have entered the correct character so you win the lottery')
else: print('Sorry you have entered the wrong character so you did not win the lottery')