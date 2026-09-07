#Build a nested dictionary named insta_profile to represent a user's Instagram profile with keys: 'username', 'followers', and 'posts' (where 'posts' is a list of dictionaries with 'caption' and 'likes'). Print the caption of the first post.
insta_profile = {
    "username": "kavita_chauhan",
    "followers": 1500,
    "posts": [
        {
            "caption": "Beautiful day!",
            "likes": 250
        },
        {
            "caption": "Enjoying the weekend!",
            "likes": 300
        }
    ]
}

print("First post caption:", insta_profile["posts"][0]["caption"])