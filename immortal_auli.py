import os
import logging
import urllib
import random
from botocore.vendored import requests

# Grab the Bot OAuth token from the environment.
BOT_TOKEN = os.environ["BOT_TOKEN"]

# Define the URL of the targeted Slack API resource.
# We'll send our replies there.
SLACK_URL = "https://slack.com/api/chat.postMessage"


def lambda_handler(data, context):
    slack_event = data['event']
    print(slack_event)
    text = ''
    txt = slack_event.get('text')
    if "bot_id" not in slack_event:
        if 'alvin' in txt:
            emoji = ('bigmuscle',
                     'catchmeifucan',
                     'centcatchweifucan',
                     'muscle',
                     'popping',
                     'special',
                     'staring',
                     'strong',
                     'withmeim')
            text = f'禿驢 :alvin{random.choice(emoji)}:'
            print(text)
        elif 'auli' in txt:
            text = '都看看是誰來了'
        post_message(text, slack_event["channel"])
    return "200 OK"

def post_message(word, channel_id):
    print(word, channel_id)
    data = urllib.parse.urlencode(
        (
            ("link_names", 1),
            ("token", BOT_TOKEN),
            ("channel", channel_id),
            ("text", word)
        )
    )
    data = data.encode("ascii")

    request = urllib.request.Request(
        SLACK_URL,
        data=data,
        method="POST"
    )

    request.add_header(
        "Content-Type",
        "application/x-www-form-urlencoded"
    )

    urllib.request.urlopen(request).read()
