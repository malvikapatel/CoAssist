import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            coassist_speak(ask)
        audio = r.listen(source)
        voice_data = ''
    try:
        voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
        coassist_speak('Sorry, I did not get that')
    except sr.RequestError:
        coassist_speak('Sorry, my speech service is down')
    return voice_data

def coassist_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        coassist_speak('My name is CoAssist')
    if 'what time is it' in voice_data:
        coassist_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        coassist_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is your location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        coassist_speak('Here is your location' + location)
    if 'covid cases' in voice_data:
        coassist_speak('Searching for covid cases today...')
        url = 'https://news.google.com/covid19/map?hl=en-CA&mid=/m/05kr_&gl=CA&ceid=CA:en'
        webbrowser.get().open(url)
        coassist_speak('Here are the Covid cases for today.')
    if 'not feeling good' in voice_data:
        coassist_speak('What are you feeling?')
        url = 'https://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/symptoms.html'
        webbrowser.get().open(url)
        coassist_speak('Here is a list of symptoms for Covid.')
    if 'doctor' in voice_data:
        coassist_speak('Do you need a virtual doctor?')
        url = 'https://www.google.com/search?q=virtual+doctors+near+me&sxsrf=AOaemvI31QtUDEKBfPIl84UaSuJrOkA6dQ%3A1642280961121&ei=ATjjYa_wBqa0qtsP-oGryAM&ved=0ahUKEwjv9Luq1bT1AhUmmmoFHfrACjkQ4dUDCA4&uact=5&oq=virtual+doctors+near+me&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEEMkDMgUIABCSAzIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BAgjECc6BQgAEJECOgUIABCABDoICAAQsQMQgwE6DgguEIAEELEDEMcBEK8BOgQIABBDOgcIABCxAxBDOhAILhCxAxCDARDHARDRAxBDOgcIIxCxAhAnOgcIIxDqAhAnOgQILhBDOggIABCABBCxAzoICAAQsQMQkQI6CwgAEIAEELEDEIMBOgcIABCABBAKOgcIABCxAxANOgQIABANOgoILhDHARCvARANOgYIABANEAo6BwgAEMkDEA06CggAEIAEEIcCEBQ6BwgAELEDEAo6BAgAEAo6CggAELEDEIMBEAo6CgguEMcBEK8BEAo6BQghEKABSgQIQRgASgQIRhgAUABY60pgmkxoFXACeACAAcYBiAGfGpIBBDI4LjiYAQCgAQGwAQrAAQE&sclient=gws-wiz'
        webbrowser.get().open(url)
        coassist_speak('Here are a few virtual doctors near your location')
    if 'sad' in voice_data:
        coassist_speak('How can I entertain you?')
    if 'song' in voice_data:
        coassist_speak('Rudolph the red nose reindeer had a very shiny nose and if you ever saw it, you would even'
                        'say it glows')
    if 'story' in voice_data:
        coassist_speak('Here is a story of the Hare and the Turtle:'
                        'One day a rabbit was boasting about how fast he could run. He was laughing at the turtle'
                        'for being so slow. Much to the rabbit’s surprise, the turtle challenged him to a race.'
                        'The rabbit thought this was a good joke and accepted the challenge. The fox was to be the'
                        'umpire of the race. As the race began, the rabbit raced way ahead of the turtle, just like'
                        'everyone thought. The rabbit got to the halfway point and could not see the turtle anywhere.'
                        'He was hot and tired and decided to stop and take a short nap. Even if the turtle passed'
                        'him, he would be able to race to the finish line ahead of him. All this time the turtle'
                        'kept walking step by step by step. He never quit no matter how hot or tired he got.'
                        'He just kept going. However, the rabbit slept longer than he had thought and woke up. He'
                        'could not see the turtle anywhere! He went at full speed to the finish line but found the'
                        'turtle there waiting for him.')
    if 'watch something' in voice_data:
        coassist_speak('Would you like to watch a movie, show or YouTube?')
    if 'YouTube' in voice_data:
        url = 'https://www.youtube.com/'
        webbrowser.get().open(url)
        coassist_speak('Here are things you can watch on Youtube')
    if 'movie' in voice_data:
        url = 'https://www.google.ca/search?q=list+of+movies+to+watch&sxsrf=AOaemvKvxbUZ6tNTlNFZTBPs3UeDnwoPaQ%3A1642281660396&source=hp&ei=vDrjYeSYFdittQas-5rwDw&iflsig=ALs-wAMAAAAAYeNIzPsgh4R15TePNOsuulqZ4jWyDdvP&ved=0ahUKEwjk5vH317T1AhXYVs0KHay9Bv4Q4dUDCAk&uact=5&oq=list+of+movies+to+watch&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCC4QgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgQIIxAnOggIABCABBCxAzoOCC4QgAQQsQMQxwEQowI6CwguEIAEELEDEIMBOgsIABCABBCxAxCDAToICAAQsQMQgwE6BwgjEOoCECc6DgguEIAEELEDEMcBENEDOgsILhCxAxDHARCjAjoNCC4QsQMQxwEQ0QMQQzoECC4QQzoKCAAQsQMQgwEQQzoECAAQQzoKCC4QsQMQgwEQQzoHCC4QsQMQQzoICC4QgAQQsQM6CggAEIAEEIcCEBQ6CwguEIAEEMcBEK8BOg0IABCABBCHAhCxAxAUOg0IABCABBCHAhDJAxAUUABYjCFghiNoAXAAeACAAWuIAcsPkgEEMjMuMZgBAKABAbABCg&sclient=gws-wiz'
        webbrowser.get().open(url)
        coassist_speak('Here are a list of movies to watch')
    if 'show' in voice_data:
        url = 'https://www.google.ca/search?q=list+of+shows+to+watch&sxsrf=AOaemvLbL9l-KvgfWkHFUBoXci8C8c7iCA%3A1642281665410&ei=wTrjYYC9GMy4tQb446HQAg&ved=0ahUKEwjAoab617T1AhVMXM0KHfhxCCoQ4dUDCA4&uact=5&oq=list+of+shows+to+watch&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBAgAEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB46BwgAEEcQsAM6BwgAELADEEM6CggAEOQCELADGAA6DAguEMgDELADEEMYAToGCAAQBxAeOggIABAIEAcQHkoECEEYAEoECEYYAVCSBFj-B2CACWgCcAJ4AIABY4gBsgOSAQE1mAEAoAEByAETwAEB2gEGCAAQARgJ2gEGCAEQARgI&sclient=gws-wiz'
        webbrowser.get().open(url)
        coassist_speak('Here are a list of shows to watch')
    if 'how to be healthy' in voice_data:
        coassist_speak('You should eat healthy food items such as fruits and vegetables, exercise regularly and be happy')
    if 'make me feel better' in voice_data:
        coassist_speak('You are amazing, awesome, kind, strong, healthy, marvelous and'
                       'supercalifragilisticexpialidocious')
    if 'exit' in voice_data:
        exit()

time.sleep(3)
coassist_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)