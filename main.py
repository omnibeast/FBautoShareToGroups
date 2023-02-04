import facebook
import time

# Facebook Access Token
ACCESS_TOKEN = "<INSERT_ACCESS_TOKEN>"

# Facebook Graph API client
graph = facebook.GraphAPI(access_token=ACCESS_TOKEN)

def get_groups():
    """Returns a list of all the groups the user has joined."""
    try:
        groups = graph.get_object("/me/groups")["data"]
        print("Successfully retrieved groups.")
        return groups
    except facebook.GraphAPIError as error:
        print("Failed to retrieve groups:", error)
        return []

def get_page_post():
    """Returns the latest post from the specific page."""
    try:
        page_post = graph.get_object("/PAGE_ID/posts?limit=1")["data"][0]
        print("Successfully retrieved page post.")
        return page_post
    except facebook.GraphAPIError as error:
        print("Failed to retrieve page post:", error)
        return None

def share_post(group_id, message, link):
    """Shares a post to a specific group."""
    try:
        graph.put_object(group_id, "feed", message=message, link=link)
        print("Successfully shared post to group:", group_id)
    except facebook.GraphAPIError as error:
        print("Failed to share post to group:", group_id, error)

# Get the list of groups the user has joined
groups = get_groups()

# Get the latest post from the specific page
page_post = get_page_post()

# Share the post to each group with a 5 second interval between each post
if page_post:
    for group in groups:
        share_post(group["id"], page_post["message"], page_post["link"])
        time.sleep(5)
