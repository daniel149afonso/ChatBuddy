import os
import tempfile
import pyttsx3
from gtts import gTTS
import playsound

tts_engine = None
DEFAULT_VOICE_ID = None
LANGUAGE_VOICES = {}

def init_tts():
    """Initialize the local TTS engine and find voices for each language."""
    global DEFAULT_VOICE_ID, LANGUAGE_VOICES
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        if voices:
            DEFAULT_VOICE_ID = voices[0].id
            for voice in voices:
                voice_id_lower = voice.id.lower()
                voice_name_lower = voice.name.lower() if hasattr(voice, 'name') else ""

                if 'en' in voice_id_lower or 'english' in voice_name_lower:
                    LANGUAGE_VOICES.setdefault('en', voice.id)
                if 'fr' in voice_id_lower or 'french' in voice_name_lower or 'français' in voice_name_lower:
                    LANGUAGE_VOICES.setdefault('fr', voice.id)
                if 'de' in voice_id_lower or 'german' in voice_name_lower or 'deutsch' in voice_name_lower:
                    LANGUAGE_VOICES.setdefault('de', voice.id)
                if 'it' in voice_id_lower or 'italian' in voice_name_lower or 'italiano' in voice_name_lower:
                    LANGUAGE_VOICES.setdefault('it', voice.id)
                if 'ro' in voice_id_lower or 'romanian' in voice_name_lower:
                    LANGUAGE_VOICES.setdefault('ro', voice.id)

            print(f"Available local voices: {list(LANGUAGE_VOICES.keys())}")

        engine.stop()
    except Exception as e:
        print(f"TTS init failed: {e}")
        DEFAULT_VOICE_ID = None


def get_voice_for_language(lang_code):
    """Get the appropriate voice ID for a given language code."""
    return LANGUAGE_VOICES.get(lang_code, DEFAULT_VOICE_ID)


def speak(text, lang_code="fr"):
    """
    Speak the given text using:
    1. Google gTTS (online natural voice) if possible
    2. fallback to pyttsx3 (offline, robotic)
    """
    print(f"🎙️ ChatBuddy: {text}")

    # --- TRY gTTS (natural, online) ---
    try:
        # Nettoyer toutes les erreurs d'encodage Windows
        safe_text = text
        if not isinstance(safe_text, str):
            safe_text = str(safe_text)

        # Supprime ou remplace les caractères que gTTS ne supporte pas
        safe_text = safe_text.encode("ascii", "ignore").decode("ascii")

        # Création et lecture du fichier audio
        tts = gTTS(text=safe_text, lang=lang_code)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tts.save(tmp_file.name)
            playsound.playsound(tmp_file.name)
        os.remove(tmp_file.name)
        return
    except Exception as e:
        print(f"⚠️ gTTS failed (offline or network issue): {e}")

    # --- FALLBACK TO PYTTSX3 (offline) ---
    try:
        global tts_engine
        tts_engine = pyttsx3.init()
        tts_engine.setProperty("rate", 175)
        tts_engine.setProperty("volume", 1.0)

        voice_to_use = get_voice_for_language(lang_code)
        if voice_to_use:
            tts_engine.setProperty("voice", voice_to_use)

        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"⚠️ pyttsx3 fallback failed: {e}")
    finally:
        if tts_engine:
            tts_engine.stop()
            tts_engine = None
