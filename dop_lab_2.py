from pydub import AudioSegment
import os


file_name = "audio.wav"

audio = AudioSegment.from_wav(file_name)


speed = 1.5

changed_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': int(audio.frame_rate * speed)})


new_file_name = "1.5speed_" + file_name
changed_audio.export(new_file_name, format="wav")


os.replace(new_file_name, os.path.join(os.getcwd(), new_file_name))

speed = 0.1

changed_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': int(audio.frame_rate * speed)})


new_file_name = "0.1speed_" + file_name
changed_audio.export(new_file_name, format="wav")


os.replace(new_file_name, os.path.join(os.getcwd(), new_file_name))