#Build a function get_user_profile that takes a username and returns a fake profile dictionary. If the username is not found in a predefined list, handle the exception and print 'User not found on Instagram'.
def get_user_profile(username):
    profiles = {
        "amit123": {
            "name": "Amit",
            "followers": 1200
        },
        "riya456": {
            "name": "Riya",
            "followers": 2500
        },
        "kavita789": {
            "name": "Kavita",
            "followers": 1800
        }
    }

    try:
        return profiles[username]
    except KeyError:
        print("User not found on Instagram")


print(get_user_profile("amit123"))
print(get_user_profile("rahul999"))