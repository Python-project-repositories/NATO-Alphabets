
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

input_word = input("Enter a word: ").upper()
output_list = [data_dict[letter] for letter in input_word]
print(output_list)