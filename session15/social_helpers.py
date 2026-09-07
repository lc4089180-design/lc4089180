#Refactor an existing script that has helper functions for formatting follower counts and post timestamps (e.g., format_follower_count, format_post_time) into a separate module called social_helpers.py, then import and use them in your main script for displaying formatted data like YouTube or Instagram.
#task4.py
def format_follower_count(count):
    if count >= 1000000:
        return f"{count / 1000000:.1f}M"
    elif count >= 1000:
        return f"{count / 1000:.1f}K"
    else:
        return str(count)


def format_post_time(minutes):
    if minutes < 60:
        return f"{minutes} minutes ago"
    elif minutes < 1440:
        hours = minutes // 60
        return f"{hours} hours ago"
    else:
        days = minutes // 1440
        return f"{days} days ago"