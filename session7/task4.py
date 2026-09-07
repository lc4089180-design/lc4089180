#Write a function that takes a Flipkart product title and returns the first 10 characters followed by '...' if the title is longer than 10 characters, otherwise returns the full title.<br><br><em><strong>Hint:</strong> Use string slicing and the len() function.</em>
def shorten_title(title):
    if len(title) > 10:
        return title[:10] + "..."
    else:
        return title


product_title = input("Enter product title: ")

print("Short Title:", shorten_title(product_title))