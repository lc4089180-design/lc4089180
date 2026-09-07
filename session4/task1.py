#Write a Python script that takes the number of likes and comments on an Instagram post as input, and prints whether the post is 'Trending' if likes are more than 1000 and comments are more than 100, otherwise prints 'Not Trending'.
likes = int(input("Enter number of likes: "))
comments = int(input("Enter number of comments: "))

if likes > 1000 and comments > 100:
    print("Trending")
else:
    print("Not Trending")