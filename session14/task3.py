#Write a list comprehension that takes a list of cricket scores and produces a list of strings where each score above 50 is labeled as 'Half-century' and scores 50 or below are labeled as 'Below Fifty'.<br><br><em><strong>Hint:</strong> Use a conditional expression inside the list comprehension.</em>
scores = [45, 67, 32, 50, 89, 41, 55]

result = ["Half-century" if score > 50 else "Below Fifty" for score in scores]

print(result)