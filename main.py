import praw, json

f = open("keys.json","r")
keys = json.load(f)


reddit = praw.Reddit(
    client_id=keys["client_id"],
    client_secret=keys["client_secret"],
    user_agent=keys["useragent"],
    username=keys["username"],
    password=keys["password"]
)


selected_subreddits = []
passed_subreddits = []

selected_user = reddit.redditor(keys["username"])

for comment in selected_user.comments.new():
    subreddit = comment.subreddit
    if(subreddit not in passed_subreddits):
        print(f"Delete comments in {subreddit.display_name}? [y/n] respond [run] for program to run now")
        response = input("")
        if response == "y":
            selected_subreddits.append(subreddit)
            passed_subreddits.append(subreddit)
        elif response == "n":
            passed_subreddits.append(subreddit)
        elif response == "run":
            break;
        else:
            exit(0)


for comment in selected_user.comments.new():
    subreddit = comment.subreddit
    if subreddit in selected_subreddits:
        comment.delete()
        print(f"Deleted a comment with id {comment} on {comment.subreddit.display_name}")