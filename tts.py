import pyttsx3

tts_engine = None
SELECTED_VOICE_ID = None

def init_tts():
    global SELECTED_VOICE_ID
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if voices:
            SELECTED_VOICE_ID = voices[0].id
        engine.stop()
    except Exception as e:
        print(f"TTS init failed: {e}")
        SELECTED_VOICE_ID = None

def speak(text):
    global tts_engine
    print(f"🎙️ ChatBuddy: {text}")
    if SELECTED_VOICE_ID is None:
        return
    try:
        tts_engine = pyttsx3.init()
        tts_engine.setProperty("rate", 150)
        tts_engine.setProperty('voice', SELECTED_VOICE_ID)
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"Speak failed: {e}")
    finally:
        if tts_engine:
            tts_engine.stop()
            tts_engine = None
