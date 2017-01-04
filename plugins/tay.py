from rtmbot.core import Plugin
import os

bot_id = 'U3MSN806S'
header = '<@{}> '.format(bot_id)

responses = {
    'hi': 'Nice to meet you, where you been?',
    'who should i vote for?': 'Me, of course',
}

directory = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

lyrics = []
with open(os.path.join(directory, 'lyrics.txt')) as fp:
    cur = ''
    for line in fp:
        if line.strip():
            cur += line
        else:
            lyrics.append(cur.strip())
            cur = ''


class Tay(Plugin):

    def process_message(self, data):
        print(data)
        if data['text'].startswith(header):
            message = data['text'][len(header):].strip().lower()
            print('winner winner {}'.format(message))
            if responses[message]:
                response = responses[message]
                print('chicken dinner {}'.format(response))
                self.outputs.append([data['channel'], response])
                self.outputs.append([data['channel'], ":tay::tay::tay:Don't forget to #votefortay :tay::tay::tay:"])
