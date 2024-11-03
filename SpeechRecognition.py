import speech_recognition as sr
import os
import webbrowser

listener = sr.Recognizer()

Apps = {
    'Google':r"C:\Users\Harris\OneDrive\Desktop\Softwares\Google Chrome.lnk",
    'vs': r"C:\Users\Harris\OneDrive\Desktop\Softwares\Visual Studio Code.lnk",
    'file':r"C:\Users\Harris\OneDrive\Desktop\Softwares\This PC - Shortcut.lnk",
    'code': r"C:\Users\Harris\OneDrive\Desktop\Code"
}
Tabs = {
    'Netflix': "https://www.netflix.com/browse",
    'video': "https://www.youtube.com/",
    'mail' : "https://mail.google.com/mail/u/0/#inbox",
    'meet' : "https://meet.google.com/landing",
}
while True:
    with sr.Microphone() as source:
        print('Listening....')
        audio = listener.listen(source)
    try:
        text = listener.recognize_google(audio)
        print(f'you said: {text}')
        if text.lower() in ['stop','quit']:
            print('Thank You!')
            break
        if text in Apps:
            os.startfile(Apps[text])
        elif text in Tabs:
            webbrowser.open(Tabs[text])
        else:
            print('file not found!')

    except sr.UnknownValueError:
        print('no audio recieved!')
    except sr.RequestError as e:
        print('Error {e}')