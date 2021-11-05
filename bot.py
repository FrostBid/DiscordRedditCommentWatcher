import praw
from time import sleep
from datetime import datetime
import discord
import os

#Add Credentials below
discordtoken = ''
channelid = 

client = discord.Client()

print("Logging in Reddit...")
reddit = praw.Reddit(username='',
                     password='',
                     client_id='',
                     client_secret='',
                     user_agent='',
                     check_for_async=False)
print("Logged in Reddit!")

#End of creditentials

@client.event
async def on_ready():
    print('Logged in Discord as {0.user}'.format(client))


@client.event
async def on_message(message):
    subreddit = reddit.subreddit("4kto1m")  # subreddits
    channel = client.get_channel(channelid)
    print('Running')
    for comment in subreddit.stream.comments(skip_existing=True):
        if comment.link_id == 't3_o9jv3b':
            try:
                print('Added comment.')
                time = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
                await channel.send(f"{time} --- {comment.body}.")
                sleep(10)
            except:
                time = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
                await channel.send(f"{time} --- Failed. Error has occurred!!")

client.run(discordtoken)
