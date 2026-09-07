#Build a function remove_duplicates(usernames) that takes a list of Instagram usernames and returns a new list with duplicates removed, preserving the original order.<br><br><em><strong>Hint:</strong> Use a loop and a temporary list to track seen usernames.</em>
def remove_duplicates(usernames):
    seen = []
    result = []

    for username in usernames:
        if username not in seen:
            seen.append(username)
            result.append(username)

    return result


usernames = [
    "kavita123",
    "riya456",
    "kavita123",
    "neha789",
    "riya456"
]

print(remove_duplicates(usernames))