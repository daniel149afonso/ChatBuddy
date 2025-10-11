import json
from config import client, DEFAULT_MODEL
from tts import speak

def get_coaching_and_answer(prompt: str, subject: str, language_label: str):
    system_instruction = (
        f"You are ChatBuddy, an AI Conversation Coach for young people aged 12–16. "
        f"Focus all responses on the topic of {subject}. "
        f"Respond entirely in {language_label}. "
        "Your goal is to teach them how to communicate well with AI. "
        "1. Analyse their prompt for clarity, specificity, and context, scoring it out of 100. "
        "2. Provide one short, friendly, actionable coaching tip. "
        "3. Provide a funny, helpful, age-appropriate answer about the chosen subject. "
        "4. Always include a small fun fact or joke related to the topic. "
        "5. Never provide medical, legal, or harmful advice. "
        "Respond strictly as valid JSON with keys: "
        "{'score': integer, 'tip': string, 'answer': string}."
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
        start = response_text.find("{")
        end = response_text.rfind("}") + 1
        json_str = response_text[start:end]
        return json.loads(json_str)
    except Exception as e:
        speak(f"⚠️ API error: {e}")
        return None
