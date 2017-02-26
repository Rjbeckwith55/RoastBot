import praw
 
# Subreddit to collect images and comments from
target_subreddit = 'RoastMe'

# create instance of Reddit
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')
 # Get subreddit
subreddit = reddit.subreddit(target_subreddit)

# Print the first 10 subreddit titles
for submission in subreddit.top(limit=10):
    s = reddit.submission(submission.id)
    for comment in s.comments:
        try:
            print(comment.body)
        except:
            pass
