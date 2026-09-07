#Given a list of strings representing Instagram usernames, write a function filter_invalid_usernames(usernames) that returns a new list containing only the usernames that are valid (use your validate_username function from Task 2).
def validate_username(username):
    if len(username) < 6:
        return False

    if not username.isalnum():
        return False

    if username[0].isdigit():
        return False

    return True


def filter_invalid_usernames(usernames):
    valid_usernames = []

    for username in usernames:
        if validate_username(username):
            valid_usernames.append(username)

    return valid_usernames


usernames = ["Kavita123", "abc", "Priya456", "123user", "Rahul789"]

print(filter_invalid_usernames(usernames))