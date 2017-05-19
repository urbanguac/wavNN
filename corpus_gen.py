from pydub import AudioSegment
import glob
filenames = glob.glob('./MP3/*.mp3')
for x in filenames:
    sound = AudioSegment.from_mp3(x)
    sound.export("./corpus/"+x[:-4]+".wav", format="wav")