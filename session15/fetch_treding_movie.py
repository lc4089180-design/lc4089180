#Install the requests package using pip and write a script called fetch_trending_movies.py that fetches data from https://jsonplaceholder.typicode.com/posts and prints the titles of the first 3 posts.<br><br><em><strong>Hint:</strong> Use pip install requests in your terminal before running the script.</em>
#Create fetch_trending_movies.py
#task3.py
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()

    for post in posts[:3]:
        print(post["title"])
else:
    print("Failed to fetch data")