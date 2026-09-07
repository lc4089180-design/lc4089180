#Use ChatGPT to generate Python code that finds the second highest number in a list of IPL scores, then test the code with the list [45, 120, 67, 120, 88, 67]. Paste the generated code and your test output.
def second_highest(scores):
    unique_scores = list(set(scores))
    unique_scores.sort(reverse=True)

    return unique_scores[1]


scores = [45, 120, 67, 120, 88, 67]

result = second_highest(scores)

print("Second Highest Score:", result)