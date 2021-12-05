import speech_recognition as sr


def speech_to_text(audioFilePath):
    r = sr.Recognizer()
    mlk = sr.AudioFile(audioFilePath)
    with mlk as source:
        audio = r.record(source)
    return r.recognize_google(audio)
