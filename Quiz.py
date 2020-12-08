# Quiz Game
# Author: Chloe Hsieh
# Date: Dec. 4, 2020

# Introduction:
print(f"Hi, thank you for taking this quiz today!")
print()

# Counter
counter = 0

# 1. Ask user what is 10+5?
# (A number as an answer)
number_answer = int(input(f"1. Please type your answer: 10 + 5 = "))

# Response
if number_answer == 15:
    print(f"You are correct!")
    counter += 1
    print(f"Your score is {counter}")
else:
    print(f"Unfortunately, that is incorrect.")
print()

# 2. What is the last word in British Columbia?
# (Text as an answer)
last_word_in_bc = (input(f"2. Please fill in the blank: B.C. is short for British ")).lower().strip(".,!")

# Response
if last_word_in_bc == "columbia":
    print(f"That's right!")
    counter += 1
    print(f"Your score is {counter}")
else:
    print(f"I'm afraid that is incorrect.")
print()

# 3. When does winter break begin?
# (Selction as an answer)
print("3. When does winter break begin?")
print("a = August | b = September | c = December")
month = (input(f"Please type the correct letter: ")).lower().strip("!.,")

# Response
if month == "c":
    print(f"Exactly! Winter break does start in December!")
    counter += 1
    print(f"Your score = {counter}")
else:
    print(f"Sorry, that is incorrect. Winter break starts in December.")
print()

# 4. What is Ca in chemistry?
element = (input("4. What element is 'Ca' in chemistry? ")).lower().strip("!.,")

# Response
if element == "calcium":
    print(f"That is correct, it is calcium!")
    counter += 1
    print(f"Your score is {counter}")
else:
    print(f"That's not quite right... it should be calcium.")
print()

# 5. Ask user what 15 x 2 is equal to.
number_answer = int(input(f"5. Please type your answer: 15 x 2 = "))

# Response
if number_answer == 30:
    print(f"Wow! You got it right, it's 30!")
    counter += 1
    print(f"Your score is {counter}")
else:
    print(f"No... sorry but it should be 30.")
print()

# Calculating Score
print("Thank you for doing this quiz!")
result = ((counter) / 5) * 100
print(f"You scored {counter}/5!")
print(f"Your final result is {result}%!")