import text_analyzer as ta

TOP_N = 10
SUMMARY_N = 3

while(True):
    text = input("$ ")
    print()

    n_words, n_sentences, n_characters = ta.count_statistics(text)
    top_n = ta.word_frequency(text, TOP_N)
    score, level, feedback = ta.evaluate_readability(text)
    summary = ta.extract_key_sentences(text, SUMMARY_N)
    lang= ta.detect_language(text)

    print("---- Language detection ----")
    print(f"Detected language: {lang}")
    print()

    print("---- Count statistics ----")
    print(f"Words: {n_words}")
    print(f"Sentences: {n_sentences}")
    print(f"Characters: {n_characters}")
    print()

    print(f"---- {TOP_N} most frequent words ----")
    for word, freq in top_n:
        print(f"\"{word}\" (frequency: {freq})")
    print()

    print("---- Readability evaluation ----")
    print(f"Score: {score} ({level})")
    print(feedback)
    print()

    print(f"---- {SUMMARY_N} sentence summarization ----")
    print(". ".join(summary) + ".")
    print()
