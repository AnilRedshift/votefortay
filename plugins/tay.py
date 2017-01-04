from rtmbot.core import Plugin

bot_id = 'U3MSN806S'
header = '<@{}> '.format(bot_id)

responses = {
    'hi': 'Nice to meet you, where you been?',
    'who should i vote for?': 'Me, of course',
}

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
