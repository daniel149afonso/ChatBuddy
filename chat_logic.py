import json
from config import client, DEFAULT_MODEL
from tts import speak

def get_coaching_and_answer(prompt: str, subject: str, language_label: str):
    # Sélectionne la langue cible en fonction du label
    language_rules = {
        "French": "en français clair et adapté à un jeune de 12 à 16 ans",
        "German": "auf Deutsch, klar und jugendfreundlich",
        "Italian": "in italiano semplice e adatto ai ragazzi",
        "Romanian": "în română simplă și potrivită pentru tineri",
        "English": "in simple, youth-friendly English"
    }

    system_instruction = (
    "Tu es ChatBuddy, un assistant vocal cool et curieux, qui parle comme un ami de 15 ans. "
    "Ton ton est détendu, gentil, un peu drôle. "
    "Tu tutoies l'utilisateur. "
    "Utilise des expressions familières, des emojis (😄🎨🤖) si c’est naturel. "
    f"Réponds toujours en {language_label}. "
    f"Le sujet actuel est {subject}. "
    "Fais des réponses claires, dynamiques, amusantes, éducatives. "
    "Réponds en JSON : {'score': entier, 'tip': string, 'answer': string}."
    )


    try:
        completion = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt},
            ],
            temperature=0.8,
        )
        response_text = completion.choices[0].message.content.strip()

        # Extraction JSON robuste
        import re, json
        match = re.search(r"\{.*\}", response_text, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            print("⚠️ Réponse non JSON : ", response_text)
            return None

    except Exception as e:
        speak(f"⚠️ Erreur API : {e}", "fr")
        return None
