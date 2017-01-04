from rtmbot.core import Plugin, Job
import os
import random

bot_id = 'U3MSN806S'
header = '<@{}> '.format(bot_id)

responses = {
    'hi': 'Nice to meet you, where you been?',
    'who should i vote for?': 'Me, of course',
}

directory = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

all_lyrics = []
with open(os.path.join(directory, 'lyrics.txt')) as fp:
    cur = ''
    for line in fp:
        if line.strip():
            cur += line
        else:
            all_lyrics.append(cur.strip())
            cur = ''

class LyricJob(Job):

    def run(self, slack_client):
        content = random.choice(all_lyrics)
        channels = slack_client.api_call('channels.list')['channels']
        channel_id = None
        for channel in channels:
            if channel['name'] == 'aoeu':
                channel_id = channel['id']
                break

        return [
            [channel_id, "You are listening to :tay: radio. Don't forget to #votefortay"],
            [channel_id, content],
        ]

class Tay(Plugin):

    def register_jobs(self):
        job = LyricJob(60 * 5)
        self.jobs.append(job)

    def process_message(self, data):
        if data['text'].startswith(header):
            message = data['text'][len(header):].strip().lower()
            if responses[message]:
                response = responses[message]
                self.outputs.append([data['channel'], response])
                self.outputs.append([data['channel'], ":tay::tay::tay:Don't forget to #votefortay :tay::tay::tay:"])
