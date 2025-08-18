from gtts import gTTS
from playsound import playsound

file_path = 'etc\my_text.txt'
with open(file_path, 'rt', encoding='UTF8') as file:
    read_file = file.read()
    
tts = gTTS(text=read_file, lang='ko')

tts.save('etc\mytest.mp3')               

playsound('etc\mytest.mp3')


