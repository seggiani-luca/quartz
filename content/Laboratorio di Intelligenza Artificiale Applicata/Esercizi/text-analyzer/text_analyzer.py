# text_analyzer.py
"""
Module for analyzing text documents.
This demonstrates the use of Python's string and collections modules from the standard library,
applying fundamental Natural Language Processing (NLP) concepts such as tokenization,
frequency analysis, and readability evaluation.

"""
# Import required modules here
import string
import collections


# Common English stopwords (words that are very frequent but carry little meaning)
STOPWORDS_EN = {
    "the", "a", "an", "is", "in", "to", "and", "of", "it", "for",
    "on", "with", "that", "this", "at", "from", "or", "be", "are",
    "was", "were", "but", "not", "have", "has", "had", "do", "does",
    "did", "will", "would", "can", "could", "should", "may", "might"
}


# Common Italian stopwords
STOPWORDS_IT = {
    "il", "lo", "la", "i", "gli", "le", "un", "uno", "una", "un'", 
    "di", "a", "da", "in", "con", "su", "per", "tra", "fra", "e", "o", 
    "ma", "anche", "come", "se", "che", "è", "non", "più", "meno",
    "già", "ne", "li", "egli", "essi", "perché", "quindi", "allora"
}


# cumulated stopwords
STOPWORDS = STOPWORDS_EN | STOPWORDS_IT

# Language codes and their associated stopwords
LANGUAGES = [
    ("EN", STOPWORDS_EN),
    ("IT", STOPWORDS_IT)
]


# Punctuation to split sentences on
SENTENCE_PUNCTUATION = {
    "!", "?", "."
}


# Levels assigned to scores
LEVELS = {
    1: "Very Simple",
    2: "Simple",
    3: "Moderate",
    4: "Complex",
    5: "Very Complex"
}


# Feedbacks assigned to scores
WORD_FEEDBACKS = [
    "Simple words, indicating limited vocabulary.",
    "Slightly longer words.",
    "Words of moderate length.",
    "Average word length is high, indicating complex vocabulary"
]
SENTENCE_FEEDBACKS = [
    "Very short sentences.",
    "Sentences are short and easy to read.",
    "Sentences are long and complex."
]
VOCAB_FEEDBACKS = [
    "Vocabulary is simple.",
    "Vocabulary is moderately complex.",
    "Vocabulary is rich and complex."
]


# Parameters for scoring
MIN_WORD_LENGTH = 3
MAX_WORD_LENGTH = 8
MIN_SENTENCE_LENGTH = 6
MAX_SENTENCE_LENGTH = 20
MIN_VOCAB_RICHNESS = 0.3
MAX_VOCAB_RICHNESS = 0.9
MIN_WORDS = 10


def get_words(text, ignore_stopwords=True):
    """
    Extracts words from a text.

    Args:
        text (str): The text to analyze.
        ignore_stopwords (bool): Whether to exclude common stopwords.

    Returns:
        list: List of extracted words, in lowercase.
    """

    # remove all punctuations 
    text = text.translate(str.maketrans("", "", string.punctuation))
   
    # convert to lowercase
    text = text.lower()

    # split on whitespace
    words = text.split()
    
    # filter stopwords
    if ignore_stopwords:
        words = [word for word in words if word not in STOPWORDS]

    return words


def get_sentences(text):
    """
    Extracts sentences from a text.

    Args:
        text (str): The text to analyze.

    Returns:
        list: List of extracted sentences.
    """

    # translate all punctuations to "."
    sentence_map = {c: "." for c in SENTENCE_PUNCTUATION}
    sent_trans = text.translate(str.maketrans(sentence_map))

    # split on punctuations, removing empty sentences 
    sentences = [s.strip() for s in sent_trans.split(".") if s.strip()]

    return sentences


def count_statistics(text):
    """
    Count basic statistics about a text.

    Args:
        text (str): The text to analyze.

    Returns:
        tuple: A tuple containing (n_words, n_sentences, n_characters) where:
               - n_words is the number of words
               - n_sentences is the number of sentences
               - n_characters is the number of characters (excluding spaces)
    """
   
    # count words
    n_words = len(get_words(text, False))

    # count sentences
    n_sentences = len(get_sentences(text))
    
    # remove all spaces and count characters
    char_trans = text.translate(str.maketrans("", "", " ")) 
    n_characters = len(char_trans)

    return (n_words, n_sentences, n_characters)


def word_frequency(text, top_n=10, ignore_stopwords=True):
    """
    Analyze word frequency in a text.

    Args:
        text (str): The text to analyze.
        top_n (int): Number of most frequent words to return.
        ignore_stopwords (bool): Whether to exclude common stopwords.

    Returns:
        list: A list of tuples (word, count) sorted by frequency in descending order.
    """

    # get words
    words = get_words(text, ignore_stopwords)

    # count frequencies
    counts = collections.Counter(words)
    most_common = counts.most_common(top_n)

    return most_common


def normalize(val, mn, mx):
    """
    Normalizes a value in [min, max] range to a [0, 1] range.

    Args:
        val (float): The value to normalize.
        mn (float): The minimum of the range.
        mx (float): The maximum of the range
    """

    # check if range is valid
    if mx == mn:
        return 0
    
    # normalize and return
    return max(min((val - mn) / (mx - mn), 1), 0)


def evaluate_readability(text):
    """
    Evaluate the readability and complexity of a text.

    Args:
        text (str): The text to evaluate.

    Returns:
        tuple: A tuple containing (score, level, feedback) where:
               - score is an integer from 1-5 (1 = very simple, 5 = very complex)
               - level is a string like "Simple", "Moderate", "Complex", etc.
               - feedback is a string explaining the evaluation
    """

    # get words
    words = get_words(text)

    # calculate average word length
    if len(words) != 0:
        avg_word_len = sum([len(word) for word in words]) / len(words)
    else:
        avg_word_len = 0

    # get sentences
    sentences = get_sentences(text)

    # get sentence words
    sent_words = [get_words(sent, False) for sent in sentences]
   
    # calculate average sentence length
    if len(sentences):
        avg_sent_len = sum([len(words) for words in sent_words]) / len(sent_words)
    else:
        avg_sent_len = 0
 
    # find unique words
    unique_words = list(set(words))

    # calculate vocabulary richness
    if len(words) != 0:
        vocab_richness = len(unique_words) / len(words)
    else:
        vocab_richness = 0

    vocab_richness *= min(len(words) / MIN_WORDS, 1)

    # normalize parameters
    avg_word_len = normalize(avg_word_len, MIN_WORD_LENGTH, MAX_WORD_LENGTH) 
    avg_sent_len = normalize(avg_sent_len, MIN_SENTENCE_LENGTH, MAX_SENTENCE_LENGTH) 
    vocab_richness = normalize(vocab_richness, MIN_VOCAB_RICHNESS, MAX_VOCAB_RICHNESS)

    # calculate score
    score = (avg_word_len + avg_sent_len + vocab_richness) / 3
    score = int(min(score * 5 + 1, 5))

    # build feedback string
    word_fback_idx = int(min(len(WORD_FEEDBACKS) * avg_word_len, len(WORD_FEEDBACKS) - 1))
    word_fback = WORD_FEEDBACKS[word_fback_idx]
    
    sent_fback_idx = int(min(len(SENTENCE_FEEDBACKS) * avg_sent_len, len(SENTENCE_FEEDBACKS) - 1))
    sent_fback = SENTENCE_FEEDBACKS[sent_fback_idx]
    
    vocab_fback_idx = int(min(len(VOCAB_FEEDBACKS) * vocab_richness, len(VOCAB_FEEDBACKS) - 1))
    vocab_fback = VOCAB_FEEDBACKS[vocab_fback_idx]

    feedback = f"{word_fback} {sent_fback} {vocab_fback}"

    return (score, LEVELS[score], feedback)


def extract_key_sentences(text, n=3):
    """
    Summarizes a text by returning the n most important sentences.

    Args:
        text (str): The text to summarize.
        n (int): Number of sentences to take.

    Returns:
        list: The sentences that were extracted.

    """
    
    # get most common words
    most_common = word_frequency(text, 10)

    # get sentences
    sentences = get_sentences(text)

    # score sentences based on word frequency
    scored_sentences = []
    for sentence in sentences:
        score = 0
        
        for word, _ in most_common:
            score += sentence.count(word)

        scored_sentences.append((sentence, score))

    # sort sentences by score
    scored_sentences.sort(key=lambda x: -x[1])
    ext_sentences = [sent[0] for sent in scored_sentences[:n]] 

    return ext_sentences


def detect_language(text):
    """
    Detects the language (Italian or English) of a text based on word frequencies.

    Args:
        text (str): The text to analyze.
    
    Returns:
        tuple: A tuple, where:
        - code is the language code
        - stopwords is the set of stopwords for the language
    """

    # get words
    words = get_words(text, False)

    # score stopwords for each language
    scores = []
    for code, stopwords in LANGUAGES:
        score = sum(1 for w in words if w in stopwords)
        scores.append((code, score))

    # get most likely language
    pred, _ = max(scores, key=lambda x: x[1])

    return pred 
