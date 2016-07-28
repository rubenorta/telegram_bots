import telepot
import re
from pprint import pprint

class Telerobot:

    def __init__(self, token, robot):
        self.token = token
        self.bot = telepot.Bot(token)
        self.robot = robot
        self.bot.message_loop({'chat': self.on_chat_msg, 'callback_query': self.on_callback_query})
        print ('Listening ...')

    def on_chat_msg(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)

        if content_type == 'voice':
            audio_file = self.robot.get_work_area(msg)     
            self.bot.download_file(msg['voice']['file_id'], audio_file )
            audio_processed = self.robot.process_voice(self.robot.work + msg['voice']['file_id'])
            self.bot.sendMessage(chat_id, 'Don Robot dice....')
            self.bot.sendVoice(chat_id, open(audio_processed, 'rb'))
            print("Sending..." + audio_processed)

        if content_type == 'text':
            finder = re.compile(ur'/debug (\d*)')
            result = re.search(finder, msg['text'])
            if result and (result.group(1) == '1234'):
                print "MODO DEBUG"   

        elif content_type == 'new_chat_member':
            self.bot.sendMessage(chat_id, self.bot.getWellcomeMsg())
        elif content_type == 'left_chat_member':
            self.bot.sendMessage(chat_id, self.bot.getLeaveMsg())        

    def on_callback_query(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print('Callback Query:', query_id, from_id, query_data)