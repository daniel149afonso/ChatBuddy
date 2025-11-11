import pyttsx3

tts_engine = None
DEFAULT_VOICE_ID = None
LANGUAGE_VOICES = {}

def init_tts():
    """Initialize the TTS engine and find voices for each language."""
    global DEFAULT_VOICE_ID, LANGUAGE_VOICES
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        if voices:
            DEFAULT_VOICE_ID = voices[0].id
            
            # Map languages to voices by searching for language codes in voice IDs/names
            for voice in voices:
                voice_id_lower = voice.id.lower()
                voice_name_lower = voice.name.lower() if hasattr(voice, 'name') else ""
                
                # English voices
                if 'en' in voice_id_lower or 'english' in voice_name_lower:
                    if 'en' not in LANGUAGE_VOICES:
                        LANGUAGE_VOICES['en'] = voice.id
                
                # French voices
                if 'fr' in voice_id_lower or 'french' in voice_name_lower or 'français' in voice_name_lower:
                    if 'fr' not in LANGUAGE_VOICES:
                        LANGUAGE_VOICES['fr'] = voice.id
                
                # German voices
                if 'de' in voice_id_lower or 'german' in voice_name_lower or 'deutsch' in voice_name_lower:
                    if 'de' not in LANGUAGE_VOICES:
                        LANGUAGE_VOICES['de'] = voice.id
                
                # Italian voices
                if 'it' in voice_id_lower or 'italian' in voice_name_lower or 'italiano' in voice_name_lower:
                    if 'it' not in LANGUAGE_VOICES:
                        LANGUAGE_VOICES['it'] = voice.id
                
                # Romanian voices
                if 'ro' in voice_id_lower or 'romanian' in voice_name_lower:
                    if 'ro' not in LANGUAGE_VOICES:
                        LANGUAGE_VOICES['ro'] = voice.id
            
            print(f"Available voices found: {list(LANGUAGE_VOICES.keys())}")
        
        engine.stop()
    except Exception as e:
        print(f"TTS init failed: {e}")
        DEFAULT_VOICE_ID = None


def get_voice_for_language(lang_code):
    """Get the appropriate voice ID for a given language code."""
    return LANGUAGE_VOICES.get(lang_code, DEFAULT_VOICE_ID)


def speak(text, lang_code=None):
    """Speak the given text using the appropriate voice for the language."""
    global tts_engine
    print(f"🎙️ ChatBuddy: {text}")

    # Get voice based on language code
    if lang_code:
        voice_to_use = get_voice_for_language(lang_code)
    else:
        voice_to_use = DEFAULT_VOICE_ID
    
    if voice_to_use is None:
        return

    try:
        tts_engine = pyttsx3.init()
        tts_engine.setProperty("rate", 150)
        tts_engine.setProperty("voice", voice_to_use)
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"Speak failed: {e}")
    finally:
        if tts_engine:
            tts_engine.stop()
            tts_engine = None