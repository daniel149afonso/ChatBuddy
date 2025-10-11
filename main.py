from tts import speak, init_tts
from languages import select_language
from subjects import choose_subject
from stt import listen_for_voice_input
from chat_logic import get_coaching_and_answer

def run_coach():
    init_tts()
    selected_language = select_language()
    speak(f"Hello! I am ChatBuddy, your AI Conversation Coach in {selected_language['label']}.")

    while True:
        subject = choose_subject()
        speak(f"Today, we’ll focus on {subject}.")
        
        while True:
            speak("Ask me anything to start!")
            user_prompt = listen_for_voice_input(selected_language["stt"])
            if not user_prompt:
                continue

            stop_words = ["exit", "quit", "stop", "bye", "i'm done", "finished", "thank you"]
            if any(word in user_prompt.lower() for word in stop_words):
                speak("Goodbye! Keep asking great questions!")
                break

            print("Thinking about your question...")
            coach_data = get_coaching_and_answer(user_prompt, subject, selected_language["label"])

            if coach_data:
                speak(coach_data.get("answer", "No answer generated."))
                speak(f"Quick Tip: {coach_data.get('tip', 'No tip this time.')}")

if __name__ == "__main__":
    run_coach()
