#Given a list of cricket scores: [45, 67, 23, 89, 100], use a for loop to calculate and print the total score.
scores = [45, 67, 23, 89, 100]

total_score = 0

for score in scores:
    total_score = total_score + score

print("Total Score:", total_score)