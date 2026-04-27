from src.utils.language_detection import contains_arabic
from src.utils.arabic_cleaning import clean_arabic
from src.utils.english_cleaning import clean_english

def preprocess_text(text: str) -> str:

    if contains_arabic(text):
        return clean_arabic(text)

    return clean_english(text)