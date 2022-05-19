from Words import words

def get_valid_word(word):
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(word)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input('guess a letter').upper()
    if user_letter in alphabet - used_letter:
        used_letters.add(user_letters)
        if user_letters in  word_letters:
            word_letters.remove(user_letter)

el



user_input = input('guess a letter, type something')

