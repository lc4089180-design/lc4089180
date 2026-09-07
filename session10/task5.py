#Use ChatGPT to generate a Python code snippet that finds all unique hashtags from a list of Instagram post captions, then copy and run the code in your IDE. Paste the output and the exact prompt you used.<br><br><em><strong>Hint:</strong> Your prompt should mention extracting hashtags from a list of strings using sets.</em>
captions = [
    "Enjoying my day! #happy #travel",
    "Beautiful sunset! #travel #nature",
    "Good vibes only! #happy #fun",
    "Exploring new places! #travel #adventure"
]

hashtags = set()

for caption in captions:
    words = caption.split()

    for word in words:
        if word.startswith("#"):
            hashtags.add(word)

print("Unique hashtags:", hashtags)