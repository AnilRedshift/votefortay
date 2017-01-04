from slackclient import SlackClient
import os
import sys

def send(message, channel):
    sc = SlackClient(os.environ['SLACK_TOKEN'])
    sc.api_call('chat.postMessage', channel=channel, text=message, as_user=True)

if __name__ == '__main__':
    channel = '#emoji'
    if len(sys.argv) >= 3:
        channel = '#' + sys.argv[2]
    send(sys.argv[1], channel)
