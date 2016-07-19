import sys
import time
import telepot
import re

import glob, os, json

from pydub import AudioSegment
from pydub.playback import play

from pprint import pprint
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


def on_voice_msg(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Calling....') 

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Calling....') 

def on_chat_msg(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    robot = u'\U0001F916'

    print(content_type, chat_type, chat_id)

    if content_type == 'voice':

		print('Processing....')
		
		file_id = msg['voice']['file_id']
		file_dest = origin_path + file_id
		print('Creating file: ' + file_dest)
		bot.download_file(file_id, file_dest)
		with open(file_dest + '.json', 'w') as outfile:
			json.dump(msg, outfile)
		print('Json Data: ')
		pprint(outfile)
		messages.append(msg)

    if content_type == 'text':
    	finder = re.compile(ur'/list')
        if (re.search(finder, msg['text'])):
        	for my_msg in messages:
        		bot.sendMessage(chat_id, 'file_id: ' + my_msg['voice']['file_id'] + " size: " + str(my_msg['voice']['file_size']))
				#bot.sendMessage(chat_id, 'file_id: ' + my_msg['voice']['file_id'])
				#print(my_msg['voice']['file_size']);

        finder = re.compile(ur'/process')
        if (re.search(finder, msg['text'])):
        	msg_to_process = messages.pop()
        	file = origin_path + msg_to_process['voice']['file_id']
        	print("Processing: " + file)
        	song = AudioSegment.from_ogg(file)
        	play(song)
        	bot.sendMessage(chat_id, 'Playing....' + file)

    	finder = re.compile(ur'/nariz')
        if (re.search(finder, msg['text'])):
        	bot.sendMessage(chat_id, 'El afiladoooooooooooooooooooooor')
        	result = bot.sendVoice(chat_id, open('afilador.mp4', 'rb'))
        	pprint(result)

    	finder = re.compile(ur'llamamos')
        if (re.search(finder, msg['text'])):
    		keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Call Afilador', callback_data='press')],
            ])

    if content_type == 'new_chat_member':
        bot.sendMessage(chat_id, "Wellcome to this awesome group!")
    if content_type == 'left_chat_member':
        bot.sendMessage(chat_id, "Sayonara baby")


#TOKEN = '252185183:AAG6-PqZKv0UE_ITFyCr2PLNGG6F6G77qjQ'
TOKEN = sys.argv[1] 

origin_path = '/tmp/don_robot/' 
os.chdir(origin_path)

messages = []

for file in glob.glob("*.json"):

	with open(file) as json_file:
		msg = json.load(json_file)

	print(msg)
	file_id = msg['voice']['file_id']
	print('Loading file : ' + str(file_id))
	messages.append(msg)
	
bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_msg,
                  'callback_query': on_callback_query})
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
