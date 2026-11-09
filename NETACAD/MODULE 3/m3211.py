word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word: ")

for letter in user_word:
    if letter.lower() not in "aeiou":
        word_without_vowels += letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)

