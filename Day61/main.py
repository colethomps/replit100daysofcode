import datetime
import os

tweets = []

def add_tweet():
    tweet = input("Enter your tweet: ")
    timestamp = datetime.datetime.now()
    tweets.append((timestamp, tweet))
    print("Tweet added successfully!")

def view_tweets():
    tweets.sort(reverse=True)
    start = 0
    while start < len(tweets):
        end = min(start + 10, len(tweets))
        for i in range(start, end):
            timestamp, tweet = tweets[i]
            print(f"{timestamp}: {tweet}")
        choice = input("Show another 10 tweets? (yes/no): ").lower()
        if choice != "yes":
            break
        start = end
        os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("\nTwitter for One Menu:")
    print("1. Add Tweet")
    print("2. View Tweets")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_tweet()
    elif choice == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        view_tweets()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
