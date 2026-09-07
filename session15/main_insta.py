#Organize a package folder named insta_utils with an __init__.py file and two modules: filters.py (define a function apply_bw_filter(image_name)) and stories.py (define a function add_story(username, image_name)). Import both functions into a new script called main_insta.py and call them with sample values.
#task2.py
from insta_utils.filters import apply_bw_filter
from insta_utils.stories import add_story

print(apply_bw_filter("vacation.jpg"))
print(add_story("kavita123", "vacation.jpg"))