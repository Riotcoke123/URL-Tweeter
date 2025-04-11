import tweepy
import time

# Your Twitter API credentials
API_KEY = ''
API_KEY_SECRET = ''
BEARER_TOKEN = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Max number of requests allowed per day
MAX_TWEETS_PER_DAY = 50

# Create the client object (v2)
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Track the number of tweets sent
tweet_count = 0
start_time = time.time()

# Function to reset the count after 24 hours
def reset_count():
    global tweet_count, start_time
    elapsed_time = time.time() - start_time
    if elapsed_time >= 24 * 60 * 60:  # 24 hours in seconds
        tweet_count = 0
        start_time = time.time()

# Function to tweet a URL, with rate limiting
def tweet_url(url):
    global tweet_count
    reset_count()
    if tweet_count < MAX_TWEETS_PER_DAY:
        try:
            # Optional: Add a prefix or hashtag, e.g., "Check this out:"
            tweet_text = f"{url}"
            client.create_tweet(text=tweet_text)
            tweet_count += 1
            print(f"Tweeted URL successfully: \"{url}\" ({tweet_count}/{MAX_TWEETS_PER_DAY} tweets used)")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Tweet limit reached. Please wait until the 24-hour limit resets.")

# Function to read URLs from a text file
def read_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            return [url.strip() for url in urls if url.strip()]  # Remove empty lines
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    file_path = 'websites.txt'  # Change this to your list of URLs

    urls = read_urls_from_file(file_path)

    for url in urls:
        tweet_url(url)
        time.sleep(5)  # Optional: space out tweets

    current_count = tweet_count
    print(f"Total URLs tweeted in the current 24-hour period: {current_count}")
