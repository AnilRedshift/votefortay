from rtmbot.core import Plugin, Job
import os
import random

bot_id = 'U3MSN806S'
header = '<@{}> '.format(bot_id)

responses = {
    'hi': 'Nice to meet you, where you been?',
    'who should i vote for?': 'Me, of course',
    'who are you': '@swiftonsecurity',
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

videos = []
with open(os.path.join(directory, 'videos.txt')) as fp:
    for line in fp:
        videos.append(line.strip())

class LyricJob(Job):

    def run(self, slack_client):
        content = random.choice(all_lyrics)
        channels = slack_client.api_call('channels.list')['channels']
        channel_id = None
        for channel in channels:
            if channel['name'] == 'emoji':
                channel_id = channel['id']
                break

        return [
            [channel_id, "You are listening to :tay: radio. Don't forget to #votefortay"],
            [channel_id, content],
        ]

class VideoJob(Job):
        def run(self, slack_client):
            channels = slack_client.api_call('channels.list')['channels']
            channel_id = None
            for channel in channels:
                if channel['name'] == 'random':
                    channel_id = channel['id']
                    break

            messages = [
                'This is so much better than a rickroll',
                'There are 10 reasons why you should click this video. #4 will shock you',
                'You must watch this video. @corey said so in #rubrics',
                'Imma let you finish, but I am the greatest of all time, actually',
                'I promise to stop posting videos if you vote for me',
            ]

            content = '{} {}'.format(random.choice(messages), random.choice(videos))

            return [
                [channel_id, content],
            ]

class Tay(Plugin):

    def register_jobs(self):
        self.jobs.append(LyricJob(60 * 30))
        self.jobs.append(VideoJob(60 * 30))

    def process_message(self, data):
        if data['text'].startswith(header):
            message = data['text'][len(header):].strip().lower()
            if message in responses:
                response = responses[message]
                self.outputs.append([data['channel'], response])
                self.outputs.append([data['channel'], ":tay::tay::tay:Don't forget to #votefortay :tay::tay::tay:"])
            elif 'devops' in message:
                self.outputs.append([data['channel'], "@tay loves devops. Even more than :max:"])
            elif 'bobby' in message:
                self.outputs.append([data['channel'], ":bobby: :heart: :tay:"])
            elif 'win' in message:
                self.outputs.append([data['channel'], "I believe in me"])
            elif 'apple' in message or 'ios' in message:
                self.outputs.append([data['channel'], "If you think Swift is the best programming language then you should #votefortay"])

            else:
                self.outputs.append([data['channel'], "I'm sorry, I'm afraid I can't answer that until you vote for me"])
