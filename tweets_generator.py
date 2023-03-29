import openai
import requests
import pandas as pd

openai.api_key = ""

import openai

def generate_tweet(twitter_handle, background, topic):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate an informational tweet for {twitter_handle}. Here's some context about them: {background}. The tweet should cover one of these subjects: {topic}, and provide readers with helpful tips or insights related to the chosen topic. The content should be an informal writing style."}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=3000,
        n=1,
        temperature=0.7,
    )
    
    tweet = response.choices[0].message['content'].strip()
    print("----------------------------------------------------------------------------------------")
    print(tweet)
    return tweet

def main():
    num_tweets = int(input("How many tweets do you want to generate? "))
    twitter_handle = input("Enter your Twitter handle (do not include @): ")
    twitter_handle = f"@{twitter_handle}"
    background = input("Provide some background info about yourself:  ")
    topic = input("Enter topics you want to tweet about (comma-separated): ")

    tweets_df = pd.DataFrame(columns=["Tweet"])

    for i in range(num_tweets):
        tweet = generate_tweet(twitter_handle, background, topic)
        new_row = pd.DataFrame({"Tweet": [tweet]})
        tweets_df = pd.concat([tweets_df, new_row], ignore_index=True)
        tweets_df.to_csv("generated_tweets.csv", index=False)

    print("Tweets have been saved to generated_tweets.csv")


if __name__ == '__main__':
    main()
