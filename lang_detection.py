from langdetect import detect, detect_langs
import sys

# Optional: Map language codes to full names
language_names = {
    'en': 'English', 'fr': 'French', 'es': 'Spanish',
    'de': 'German', 'hi': 'Hindi', 'te': 'Telugu',
    'zh-cn': 'Chinese (Simplified)', 'ar': 'Arabic',
    'sv': 'Swedish', 'no': 'Norwegian', 'it': 'Italian',
    'pt': 'Portuguese', 'ru': 'Russian', 'ja': 'Japanese', 'mk': 'Macedonian',
    'ko': 'Korean', 'ta': 'Tamil', 'bn': 'Bengali', 'da': 'Danish',
    'gu': 'Gujarati', 'ml': 'Malayalam', 'ur': 'Urdu', 'ca': 'Catalan'
}

def detect_language(text):
    try:
        code = detect(text)
        confidence = detect_langs(text)
        lang_name = language_names.get(code, "Unknown Language")
        return code, lang_name, confidence
    except Exception as e:
        return None, "Error", str(e)

def main():
    print("🔤 Language Detection using NLP")
    print("--------------------------------")
    user_text = input("Enter text in any language: ")

    code, lang_name, confidence = detect_language(user_text)

    if code:
        print(f"\n✅ Detected Language: {lang_name} ({code})")
        print(f"📊 Confidence: {confidence}")
    else:
        print(f"\n❌ Error in detection: {confidence}")

if __name__ == "__main__":
    main()
