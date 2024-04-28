#Anthony Love
#04/28/2024
#P4HW1_LoveAnthony
#Loop to calulate scores



num_scores = int(input("How many scores do you want to enter: "))

scores = []

for i in range(num_scores):
    while True:
        score = float(input(f"Enter Score #{i+1}: "))

        if 0 <= score <=100:
             scores.append(score)
             break

        if score < 0:
            print()
            print("INVALID Score entered!!!!!!!!!!")
            print("Please enter a score between 0 and 100.")
            again = float(input(f"Enter Score #{i+1} again: "))
            scores.append(again)
            break

lowest_score = min(scores)

modified_scores = scores.copy()

modified_scores.remove(lowest_score)

average_score = sum(modified_scores) / len(modified_scores)

if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

print()
print("--------------Results-----------")
print(f"Lowest score  : {lowest_score}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {grade}")
print("-------------------------------------")

#Set up a way for the user to type in scores. Check each score as it's entered to see if it's less than 0.
#Should a negative score be detected, prompt the user for confirmation to re-enter the score
#Once all the scores are collected, continue with the rest of the program, which should be straightforward and similar to what we've done before.

