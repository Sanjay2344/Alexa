import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

  try:
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
  except:
    pass
  return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        today = datetime.date.today()
        date = today.strftime("%A, %B %d, %Y")
        print(date)
        talk('the time is' + date)
    elif 'fun' in command:
        talk('Sorry!, Please Stop your mouth I am a machine not a human')
    elif 'are you single' in command:
        talk('No I am relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'thank' in command:
        talk('You are most welcome')
    else:
        talk('Sorry I didn\'t understand please repeat again')


while True:
    run_alexa()

