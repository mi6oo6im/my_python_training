import math
import sys
most_powerful_word = ""
word_text = input()
word_power = 0
top_power = -sys.maxsize
word_length = 0
while word_text != "End of words":
    word_power = 0
    for letter in word_text:
        word_power += ord(letter)
        word_length = len(word_text)
    if str.lower(word_text[0]) in ("a", "e", "i", "o", "u", "y"):
        word_power *= word_length
    else:
        word_power = math.floor(word_power / word_length)
    if top_power < word_power:
        most_powerful_word = word_text
        top_power = word_power
    word_text = input()

print(f"The most powerful word is {most_powerful_word} - {top_power}")
