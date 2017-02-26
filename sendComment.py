import praw

# Subreddit to collect images and comments from
target_subreddit = 'RoastMe'

# create instance of Reddit
reddit = praw.Reddit(client_id='yk5ZPLB9OH3hbw',
                     client_secret='MKA2K7kLP5AOL1wsZytwMCfU1yw',
                     user_agent='HackIllini2017')
 # Get subreddit
subreddit = reddit.subreddit(target_subreddit)

# Print the first 10 subreddit titles
for submission in subreddit.top(limit=1):
    s = reddit.submission(submission.id)
    for comment in s.comments:
        try:
            print(comment.body)
            break
        except:
            pass


