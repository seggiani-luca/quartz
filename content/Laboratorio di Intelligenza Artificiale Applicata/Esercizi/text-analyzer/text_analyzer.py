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
STOPWORDS = {
    "the", "a", "an", "is", "in", "to", "and", "of", "it", "for",
    "on", "with", "that", "this", "at", "from", "or", "be", "are",
    "was", "were", "but", "not", "have", "has", "had", "do", "does",
    "did", "will", "would", "can", "could", "should", "may", "might"
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
FEEDBACKS = {
    1: "Text is very easy to read. Words and sentences are short, and vocabulary is simple.",
    2: "Text is easy to read. Words are fairly simple and sentences are short.",
    3: "Text has moderate complexity. Word length and sentence structure are balanced.",
    4: "Text is complex. Words are longer and sentences are more difficult to follow.",
    5: "Text is very complex. Vocabulary is advanced and sentences are long and dense."
}


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
    words = text.split()
    n_words = len(words)

    # count sentences
    n_sentences = sum(text.count(p) for p in ".!?")
    if n_sentences == 0 and text.strip():
        n_sentences = 1
    
    # count characters
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

    # remove all punctuations 
    text = text.translate(str.maketrans("", "", string.punctuation))
   
    # convert to lowercase
    text = text.lower()

    # split on whitespace
    words = text.split()
    
    # filter stopwords
    if ignore_stopwords:
        words = [word for word in words if word not in STOPWORDS]

    # count frequencies
    counts = collections.Counter(words)
    most_common = counts.most_common(top_n)

    return most_common


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

    def normalize(val, mn, mx):
        """
        Normalizes a value in [min, max] range to a [0, 1] range.

        Args:
            val (float): The value to normalize.
            mn (float): The minimum of the range.
            mx (float): The maximum of the range.
        Returns:
            float: The normalized value
        """

        # check if range is valid
        if mx == mn:
            return 0
        
        # normalize and return
        return max(min((val - mn) / (mx - mn), 1), 0)

    # get words
    words = text.split()

    # calculate average word length
    if len(words) != 0:
        avg_word_len = sum([len(word) for word in words]) / len(words)
    else:
        avg_word_len = 0

    # get sentences
    sentence_map = {c: "." for c in ".!?"}
    sent_trans = text.translate(str.maketrans(sentence_map))
    sentences = [s.strip() for s in sent_trans.split(".") if s.strip()]

    # get sentence words
    sent_words = [sent.split() for sent in sentences]
   
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

    # optional: don't interpret short text as really rich 
    # vocab_richness *= min(len(words) / MIN_WORDS, 1)

    # normalize parameters
    avg_word_len = normalize(avg_word_len, 5, 8) 
    avg_sent_len = normalize(avg_sent_len, 6, 20) 
    vocab_richness = normalize(vocab_richness, 0.3, 0.9)

    # calculate score
    score = (avg_word_len + avg_sent_len + vocab_richness) / 3
    score = int(min(score * 5 + 1, 5))

    return (score, LEVELS[score], FEEDBACKS[score])
