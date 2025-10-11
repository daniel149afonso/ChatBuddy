import speech_recognition as sr
from tts import speak

def listen_for_voice_input(language_code):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("🎙️ Listening...")
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio, language=language_code)
            print(f"🗣️ You said: {text}")
            return text
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return None
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand. Please try again.")
            return None
        except sr.RequestError:
            speak("Speech recognition service unavailable.")
            return None
