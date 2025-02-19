
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}



def Generate_phonetic_alphabet():
    input_word = input("Enter a word: ").upper()
    try:
        output_list = [data_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        Generate_phonetic_alphabet()
    else:
        print(output_list)

Generate_phonetic_alphabet()