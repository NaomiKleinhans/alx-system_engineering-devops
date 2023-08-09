import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    
    try:
        sub_info.raise_for_status()  # This will raise an exception for non-2xx status codes
        sub_data = sub_info.json().get("data")
        
        if sub_data and "subscribers" in sub_data:
            return sub_data["subscribers"]
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0

# Example usage
subreddit_name = "programming"
subscribers = number_of_subscribers(subreddit_name)
print(f"Subreddit '{subreddit_name}' has {subscribers} subscribers.")
