#Importando librerias
import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard
from pygame import mixer

#definiendo variables
name = 'Alex'
listener = sr.Recognizer()
engine = pyttsx3.init()

#dando valores a la voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#funcion para que Alex hable
def talk(text):
    engine.say(text)
    engine.runAndWait()
   
#funcion para que Alex Escuche 
def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
            print('Escuchando...')
            listener.adjust_for_ambient_noise(source)
            pc = listener.listen(source)
    try:
            rec = listener.recognize_google(pc, language='es')
            rec = rec.lower()
    except sr.UnknownValueError:
            print('No te entendi, intenta de nuevo')
            if name in rec:
                rec = rec.replace(name, '')
    return rec
            
#funcion de lo que alex puede hacer 
def run_alex():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            print('No te entendi, intenta de nuevo')
            continue
        #reproducir musica en youtube
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print('Reproduciendo' + music)
            talk('Reproduciendo' + music)
            pywhatkit.playonyt(music)
        #buscar cosas en google
        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang('es')
            wiki = wikipedia.summary(search, 1)
            print(search + ': '+ wiki)
            talk(wiki)
        #poner una alarma
        elif 'alarma' in rec:
            num = rec.replace('alarma', '')
            num = num.strip()
            talk('Alarma activada a las' + num + 'horas')
            while True:
                if datetime.datetime.now().strftime('%H:%M') == num:
                    print('Despierta')
                    mixer.init()
                    mixer.music.load('auronplay-alarma.mp3')
                    mixer.music.play()
                    if keyboard.read_key() == ' ':
                        mixer.music.stop()
                        break
            

if __name__ == '__main__':
    run_alex()