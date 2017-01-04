from slackclient import SlackClient
import os
import sys

def send(message):
    sc = SlackClient(os.environ['SLACK_KEY'])
    sc.api_call('chat.postMessage', channel='#aoeu', text=message, as_user=True)

if __name__ == '__main__':
    send(sys.argv[1])
