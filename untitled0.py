import speech_recognition as sr
import pyttsx3 

engine=pyttsx3.init()

def speak(word):
    engine.setProperty('rate', 135)
    engine.setProperty('volume', 0.8)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(str(word))
    engine.runAndWait()
    engine.stop()
def parseCommand():
   
        listener = sr.Recognizer()
        print('Listening for a command')

        with sr.Microphone(sample_rate=16000) as source:
            listener.adjust_for_ambient_noise(source)
            listener.pause_threshold = 2
            input_speech = listener.listen(source)
        try:
            print('Recognizing speech...')
            query = listener.recognize_google(input_speech, language='en_gb')
            print(f'The input speech was: {query}')

        except Exception as exception:
            print('I did not quite catch that')
            print(exception)
            return 'None'
        return query


speak(parseCommand())

      
   
  


  
