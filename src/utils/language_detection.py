import re

def contains_arabic(text: str) -> bool:

    arabic_pattern = re.compile(r'[\u0600-\u06FF]')

    return bool(arabic_pattern.search(text))
