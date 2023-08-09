import requests

def number_of_subscribers(subreddit):
    user_agent = "Custom User Agent"
    headers = {"User-Agent": user_agent}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        elif response.status_code == 404:
            return 0
        else:
            return 0
    except requests.RequestException as e:
        return 0

subreddit_name = "python"
subscribers = number_of_subscribers(subreddit_name)
print(f"Subscribers of /r/{subreddit_name}: {subscribers}")
