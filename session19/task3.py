#Given a string containing a mix of hashtags and usernames like an Instagram caption (e.g., 'Loving the vibes! #summer @friend1 #fun @friend2'), use Python's re module to extract all hashtags and all usernames separately and print them.<br><br><em><strong>Hint:</strong> Hashtags start with #, usernames start with @.</em>
import re

caption = "Loving the vibes! #summer @friend1 #fun @friend2"

hashtags = re.findall(r"#\w+", caption)
usernames = re.findall(r"@\w+", caption)

print("Hashtags:", hashtags)
print("Usernames:", usernames)