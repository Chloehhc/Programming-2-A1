# Quiz Game
# Author: Chloe Hsieh
# Date: Dec. 4, 2020

# INTRODUCTION
print(f"Hi, thank you for taking this fun quiz today!")
print()

# COUNTER
counter = 0

# 1. ASK USER WHAT 10 + 5 IS EQUAL TO
# (A number as an answer)
number_answer = input(f"1. Let's start off with a simple question! 10 + 5 = ").strip("!.,").lower()

# Response to correct answer
if number_answer == "15" or number_answer == "fifteen":
    print(f"You are..... correct!!!!! Good job, it's 15!")
    counter += 1
    print(f"Your score is {counter}")
# Response to incorrect answer
else:
    print(f"Oh no! That is incorrect, but have no fear! There's more to come!")
    print(f"Your score is {counter}")
print()

# 2. ASK USER TO FILL IN THE BLANK FOR BRITISH COLUMBIA
# (Text as an answer)
last_word_in_bc = (input(f"2. Hmmm... let's see if you know this. B.C. is short for British ")).lower().strip(".,!")

# Response to correct answer
if last_word_in_bc == "columbia":
    print(f"Columbia is correct! Nice!")
    counter += 1
    print(f"Your score is {counter}")
# Response to incorrect answer
else:
    print(f"I'm afraid that is incorrect, but no worries! There are other questions!")
    print(f"Your score is {counter}")
print()

# 3. ASK USER WHEN WINTER BREAK BEGINS
# (Selection as an answer)
print("3. When does the best break (also known as winter break) begin?")
print("a = August | b = September | c = December")
month = (input(f"Please type the correct letter: ")).lower().strip("!.,")

# Response to correct answer
if month == "c":
    print(f"Exactly! Winter break does start in December!")
    counter += 1
    print(f"Your score = {counter}")
# Response to incorrect answer
else:
    print(f"Hmm... not quite. Winter break starts in December!")
    print(f"Your score is {counter}")
print()

# 4. ASK USER WHAT "Ca" STANDS FOR IN CHEMISTRY
element = (input("4. Let's throw in some chemistry for fun! Wha is 'Ca' in chemistry? ")).lower().strip("!.,")

# Response to correct answer
if element == "calcium":
    print(f"You're entirely correct, it is calcium! Good answer!")
    counter += 1
    print(f"Your score is {counter}")
# Response to incorrect answer
else:
    print(f"Unfortunately, that's wrong. It's actually supposed to be calcium! Good try though!")
    print(f"Your score is {counter}")
print()

# 5. ASK USER WHAT 15 x 2 IS EQUAL TO
multiplication_answer = input(f"5. Okay, let's end this quiz off with some math. 15 x 2 = ").strip("!.,").lower()

# Response to correct answer.
if multiplication_answer == "30" or multiplication_answer == "thirty":
    print(f"Wow! You got it right, it's 30! You're smart!")
    counter += 1
    print(f"Your score is {counter}")
# Response to incorrect answer.
else:
    print(f"Nice try, but that's incorrect. It should be 30!")
    print(f"Your score is {counter}")
print()

# END OF QUIZ
print("Thank you so much for doing this quiz! I hope you had fun!")
print()

# CALCULATE FINAL SCORE
result = ((counter) / 5) * 100
# Show user the number of questions correct over total questions
print("Now..... here is your final score!")
print(f"You scored {counter}/5!")
# Show user the final percentage score
print(f"Your final result is {result}%!")