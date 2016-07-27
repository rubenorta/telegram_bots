import os, glob, json
from pprint import pprint

class Donrobot:

	def __init__(self, path = '/tmp/donrobot/'):

		self.work = path
		self.export = path + 'export/'
		self.messages = []
		self.current_audio = ''
		self.robot_face = u'\U0001F916'

		if not os.path.exists(path):
			os.makedirs(path)
			os.makedirs(self.export)
			print "Creating Working Area.."
	
		elif not os.path.exists(self.export):
			os.makedirs(self.export)
			print "Creating Working Area.."

		else:
			for file in glob.glob(self.work + "*.json"):
				with open(file) as json_file:
					msg = json.load(json_file)
					pprint(msg)
					file_id = msg['voice']['file_id']
					print('Loading file : ' + str(file_id))
					self.messages.append(msg)

	def prepare(self, msg):

		file_id = msg['voice']['file_id']
		file_dest = self.work + file_id
		with open(file_dest + '.json', 'w') as outfile:
			json.dump(msg, outfile)
		return file_id, file_dest

	def process(self, msg):

		file_id = msg['voice']['file_id']
		Audio.clean_audio(file_id)
		self.current_audio = Audio.vocoder(file_id)

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

