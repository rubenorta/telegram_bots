import os, glob, json
from pprint import pprint

class Donrobot:

	def __init__(self, voice, path = '/tmp/donrobot/'):

		self.work = path
		self.messages = []
		self.current_audio = ''
		self.robot_face = u'\U0001F916'
		self.effects = voice

		if not os.path.exists(path):
			os.makedirs(path)
			print "Creating Working Area.."

		else:
			for file in glob.glob(self.work + "*.json"):
				with open(file) as json_file:
					msg = json.load(json_file)
					#pprint(msg)
					file_id = msg['voice']['file_id']
					print('Loading file : ' + str(file_id))
					self.messages.append(msg)

	def prepare(self, msg):
		file_id = msg['voice']['file_id']
		file_dest = self.work + file_id
		with open(file_dest + '.json', 'w') as outfile:
			json.dump(msg, outfile)
		return file_id, file_dest

	def process_voice(self, file_path):	
		return self.effects.process(file_path)

	def clean_area(self, file_id):

		file = self.export + file_id + ".mp3"
		os.remove(file);
		file = self.work + file_id + ".json"
		os.remove(file);
		file = self.work + file_id
		os.remove(file);
		file = self.export + file_id + "-voc.mp3"
		os.remove(file);

	def get_wellcome_msg(self):
		return self.robot_face + 'Bienvenido al grupo de amigos de DonRobot' + self.robot_face

	def get_leave_msg(self):
		return 'Adios! Ya sabes donde andamos ' + self.robot_face

	def get_work_area(self,msg):
		return self.work + msg['voice']['file_id'] + ".ogg"