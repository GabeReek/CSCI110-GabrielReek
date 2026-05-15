my_text = """Python is a helpful language to learn.
It lets people write programs and solve problems.
Even small programs can become useful."""

def count_e_words(text):
    punctuation = ".,!?;:-'"

    for letter in punctuation:
        text = text.replace(letter, "")

    words = text.split()

    number_of_words = len(words)
    words_with_e = 0

    for word in words:
        if "e" in word:
            words_with_e = words_with_e + 1

    percent = words_with_e / number_of_words * 100

    print("Your text contains", number_of_words, "words, of which", words_with_e, "(" + str(round(percent, 1)) + "%) contain an 'e'.")


count_e_words(my_text)
