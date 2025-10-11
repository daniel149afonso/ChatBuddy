LANGUAGES = {
    "en": {"label": "English", "stt": "en-US"},
    "fr": {"label": "French", "stt": "fr-FR"},
    "de": {"label": "German", "stt": "de-DE"},
    "it": {"label": "Italian", "stt": "it-IT"},
    "ro": {"label": "Romanian", "stt": "ro-RO"},
}

def select_language():
    print("🌍 Available languages:")
    for code, info in LANGUAGES.items():
        print(f"  {code}: {info['label']}")

    lang_choice = input("Select your language (en/fr/de/it/ro): ").strip().lower()
    if lang_choice not in LANGUAGES:
        print("Invalid choice. Defaulting to English.")
        lang_choice = "en"
    selected = LANGUAGES[lang_choice]
    print(f"✅ Language set to {selected['label']}.")
    return selected
