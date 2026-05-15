import string

book_file = open("alice_in_wonderland.txt", "r")

book_text = book_file.read()

book_file.close()

book_text = book_text.lower()

for mark in string.punctuation:
    book_text = book_text.replace(mark, " ")

words = book_text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

words_list = list(word_count.keys())

words_list.sort()

new_file = open("alice_words.txt", "w")

new_file.write("Word              Count\n")
new_file.write("=======================\n")

for word in words_list:
    new_file.write(word + "              " + str(word_count[word]) + "\n")

new_file.close()

print("The word alice appears", word_count["alice"], "times.")
