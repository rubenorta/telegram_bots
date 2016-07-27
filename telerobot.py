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
            self.bot.download_file(msg['voice']['file_id'], self.robot.work_area + file_id)
            self.robot.process_voice(msg)
            self.bot.sendMessage(chat_id, 'Don Robot dice....')
            self.bot.sendVoice(chat_id, open(self.robot.current_audio, 'rb'))
            print("Sending..." + self.robot.current_audio)

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

'''
    def on_chat_msg(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)

    	if content_type == 'voice':
    		file_id, file_dest = self.robot.prepare(msg)
    		self.bot.download_file(file_id, file_dest)
    		self.robot.process(msg)
			self.bot.sendMessage(chat_id, 'Don Robot dice....')
			self.bot.sendVoice(chat_id, open(self.robot.current_audio, 'rb'))
			print("Sending..." + self.robot.current_audio)

    	elif content_type == 'new_chat_member'
			self.bot.sendMessage(chat_id, self.bot.getWellcomeMsg())
		elif content_type == 'left_chat_member':
        	self.bot.sendMessage(chat_id, self.bot.getLeaveMsg())

    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        print('Callback Query:', query_id, from_id, query_data)
        
        self.bot.answerCallbackQuery(query_id, text='Calling....') 
'''
'''
    def send_audio(msg):
        self.bot.sendMessage(chat_id, 'Don Robot dice....')
        print("Sending..." + self.robot.current_audio)
        self.bot.sendVoice(chat_id, open(self.robot.current_audio, 'rb'))
'''

'''
    	if content_type == 'text':



    	finder = re.compile(ur'/debug')
        if (re.search(finder, msg['text'])):
        	DELETE = False

    	finder = re.compile(ur'/clean')
        if (re.search(finder, msg['text'])):
        	DELETE = False

    	finder = re.compile(ur'/list')
        if (re.search(finder, msg['text'])):
        	for my_msg in messages:
        		bot.sendMessage(chat_id, 'file_id: ' + my_msg['voice']['file_id'] + " size: " + str(my_msg['voice']['file_size']))

        finder = re.compile(ur'/process')
        if (re.search(finder, msg['text'])):
        	msg_to_process = messages.pop()
        	clean_audio(msg_to_process['voice']['file_id'])
        	result_file = vocoder(msg_to_process['voice']['file_id'])
        	bot.sendMessage(chat_id, 'Don Robot dice....')
        	print("Sending..." + result_file)
        	bot.sendVoice(chat_id, open(result_file, 'rb'))
        	Donrobot.clean_area(msg_to_process['voice']['file_id'])
'''

    #if content_type == 'new_chat_member':
    #    self.bot.sendMessage(chat_id, "Wellcome to this awesome group!")
    #if content_type == 'left_chat_member':
    #    self.bot.sendMessage(chat_id, "Sayonara baby")
