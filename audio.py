
from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import invert_phase, compress_dynamic_range
from aubio import source, sink, pvoc
from pprint import pprint

class Audio:

	def vocoder(file_path):
		
		in_file = '/tmp/don_robot/output/' + file_id + ".mp3"
		out_file = '/tmp/don_robot/output/' + file_id + "-voc.mp3"

		samplerate = 44100
		f = source(in_file, samplerate, 256)
		g = sink(out_file, samplerate)
		total_frames, read = 0, 256

		win_s = 512                          # fft size
		hop_s = win_s // 2                   # hop size
		pv = pvoc(win_s, hop_s)              # phase vocoder

		while read:
			samples, read = f()
			spectrum = pv(samples)           # compute spectrum
			spectrum.norm *= .5             # reduce amplitude a bit .8
			spectrum.phas[:] = 0.            # zero phase
			new_samples = pv.rdo(spectrum)   # compute modified samples
			g(new_samples, read)             # write to output
	 		total_frames += read

		format_str = "read {:d} samples from {:s}, written to {:s}"
		print(format_str.format(total_frames, f.uri, g.uri))
		return out_file

	def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):

		trim_ms = 0
		while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold:
			trim_ms += chunk_size
		return trim_ms

	def clean_audio(filepath):

		print "Processing audio"
		file = origin_path + file_id
		sound = AudioSegment.from_ogg(file)

		start_trim = detect_leading_silence(sound)
		end_trim = detect_leading_silence(sound.reverse())
		duration = len(sound)    
		sound = sound[start_trim:duration-end_trim]
		sound = invert_phase(sound)

		output_file = file_path + "-clean.mp3"
		file_handle = sound.export( output_file, format="mp3")
		print("Output File....")
		pprint(file_handle)