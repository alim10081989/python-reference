import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv('nato_phonetic_alphabet.csv')
secret_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    user_input = input('Whats your word : ').upper()

    try:
        code_word = [secret_dictionary[letter] for letter in user_input]
    except KeyError:
        print('Sorry, only letter in the alphabets please.')
        generate_phonetic()
    else:
        print(code_word)


generate_phonetic()
