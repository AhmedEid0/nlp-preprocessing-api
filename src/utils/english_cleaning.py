import re
import string
import html
import unicodedata

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()


def remove_special_chars(text: str) -> str:

    re1 = re.compile(r'[  ]+')

    text = html.unescape(text)

    text = text.replace(' @.@ ', '.')
    text = text.replace(' @-@ ', '-')
    text = text.replace('\\', ' \\ ')

    return re1.sub(' ', text)


def remove_non_ascii(text: str) -> str:

    return unicodedata.normalize(
        'NFKD',
        text
    ).encode(
        'ascii',
        'ignore'
    ).decode(
        'utf-8',
        'ignore'
    )


def remove_punctuation(text: str) -> str:

    translator = str.maketrans('', '', string.punctuation)

    return text.translate(translator)


def remove_numbers(text: str) -> str:

    return re.sub(r'\d+', '', text)


def normalize_whitespace(text: str) -> str:

    return re.sub(r'\s+', ' ', text).strip()


def tokenize_text(text: str):

    return word_tokenize(text)


def remove_stopwords(words):

    return [
        word for word in words
        if word not in stop_words
    ]


def lemmatize_words(words):

    return [
        lemmatizer.lemmatize(word)
        for word in words
    ]


def clean_english(text: str) -> str:

    text = remove_special_chars(text)

    text = remove_non_ascii(text)

    text = text.lower()

    text = remove_punctuation(text)

    text = remove_numbers(text)
    
    text = text.replace("\\n", " ")

    text = normalize_whitespace(text)

    words = tokenize_text(text)

    words = remove_stopwords(words)

    words = lemmatize_words(words)

    return ' '.join(words)