# Quiz Game
# Author: Chloe Hsieh
# Date: Dec. 4, 2020

# INTRODUCTION
print(f"Hi, thank you for taking this quiz today!")
print()

# COUNTER
counter = 0

# 1. ASK USER WHAT 10 + 5 IS EQUAL TO
# (A number as an answer)
number_answer = input(f"1. Please type your answer: 10 + 5 = ").strip("!.,").lower()

# Response to correct answer
if number_answer == "15" or number_answer == "fifteen":
    print(f"You are correct!")
    counter += 1
    print(f"Your score is {counter}")
# Response to incorrect answer
else:
    print(f"Unfortunately, that is incorrect.")
print()

# 2. ASK USER TO FILL IN THE BLANK FOR BRITISH COLUMBIA
# (Text as an answer)
last_word_in_bc = (input(f"2. Please fill in the blank: B.C. is short for British ")).lower().strip(".,!")

# Response to correct answer
if last_word_in_bc == "columbia":
    print(f"That's right!")
    counter += 1
    print(f"Your score is {counter}")
# Response to incorrect answer
else:
    print(f"I'm afraid that is incorrect.")
print()

# 3. ASK USER WHEN WINTER BREAK BEGINS
# (Selection as an answer)
print("3. When does winter break begin?")
print("a = August | b = September | c = December")
month = (input(f"Please type the correct letter: ")).lower().strip("!.,")

# Response to correct answer
if month == "c":
    print(f"Exactly! Winter break does start in December!")
    counter += 1
    print(f"Your score = {counter}")
# Response to incorrect answer
else:
    print(f"Sorry, that is incorrect. Winter break starts in December.")
print()

# 4. ASK USER WHAT "Ca" STANDS FOR IN CHEMISTRY
element = (input("4. What element is 'Ca' in chemistry? ")).lower().strip("!.,")

# Response to correct answer
if element == "calcium":
    print(f"That is correct, it is calcium!")
    counter += 1
    print(f"Your score is {counter}")
# Response to incorrect answer
else:
    print(f"That's not quite right... it should be calcium.")
print()

# 5. ASK USER WHAT 15 x 2 IS EQUAL TO
number_answer = input(f"5. Please type your answer: 15 x 2 = ").strip("!.,").lower()

# Response to correct answer.
if number_answer == "30" or number_answer == "thirty":
    print(f"Wow! You got it right, it's 30!")
    counter += 1
    print(f"Your score is {counter}")
# Response to incorrect answer.
else:
    print(f"No... sorry but it should be 30.")
print()

# END OF QUIZ
print("Thank you for doing this quiz!")

# CALCULATE FINAL SCORE
result = ((counter) / 5) * 100
# Show user the number of questions correct over total questions
print(f"You scored {counter}/5!")
# Show user the final percentage score
print(f"Your final result is {result}%!")