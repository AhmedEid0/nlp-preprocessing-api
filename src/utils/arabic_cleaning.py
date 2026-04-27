import re


def remove_diacritics(text: str) -> str:

    arabic_diacritics = re.compile("""
        ّ    | # Shadda
        َ    | # Fatha
        ً    | # Tanwin Fath
        ُ    | # Damma
        ٌ    | # Tanwin Damm
        ِ    | # Kasra
        ٍ    | # Tanwin Kasr
        ْ    | # Sukun
        ـ      # Tatweel
    """, re.VERBOSE)

    return re.sub(arabic_diacritics, '', text)


def normalize_arabic(text: str) -> str:

    text = re.sub(r'[إأآا]', 'ا', text)

    text = re.sub(r'ى', 'ي', text)

    text = re.sub(r'ؤ', 'و', text)

    text = re.sub(r'ئ', 'ي', text)

    text = re.sub(r'ة', 'ه', text)

    return text


def remove_urls(text: str) -> str:

    return re.sub(r'http\S+|www\S+', '', text)


def remove_numbers(text: str) -> str:

    return re.sub(r'\d+', '', text)


def remove_punctuation(text: str) -> str:

    return re.sub(r'[^\w\s]', '', text)


def normalize_repeated_chars(text: str) -> str:

    return re.sub(r'(.)\1+', r'\1\1', text)


def normalize_whitespace(text: str) -> str:

    return re.sub(r'\s+', ' ', text).strip()


def clean_arabic(text: str) -> str:

    text = remove_urls(text)

    text = remove_diacritics(text)

    text = normalize_arabic(text)

    text = remove_numbers(text)

    text = remove_punctuation(text)

    text = normalize_repeated_chars(text)

    text = normalize_whitespace(text)

    return text