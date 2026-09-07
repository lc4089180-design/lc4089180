#Create a function called format_follower_count that takes a follower count as an argument and returns the count formatted like Instagram (e.g., 1500 as '1.5K', 1200000 as '1.2M').<br><br><em><strong>Hint:</strong> Use conditional logic to determine which suffix to use based on the count.</em>
def format_follower_count(count):
    if count >= 1000000:
        return f"{count / 1000000:.1f}M"
    elif count >= 1000:
        return f"{count / 1000:.1f}K"
    else:
        return str(count)


print(format_follower_count(950))
print(format_follower_count(1500))
print(format_follower_count(1200000))