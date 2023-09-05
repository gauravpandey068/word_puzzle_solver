from itertools import permutations
from typing import Any

import enchant


def get_letter() -> list[str]:
	letters = input("Enter Your Letters:- ")
	if not letters:
		print("Input Must be a number")
		get_letter()
	letter_dict = []
	if len(letters) > 6:
		print("Letters Cannot be More than 6")
		get_letter()

	for letter in letters:
		letter_dict.append(letter)

	return letter_dict


def make_words(letters: list[str]) -> list[str]:
	length_of_letters = len(letters)

	words = []
	for r in range(1, length_of_letters):
		letter_permutations = permutations(letters, r + 1)
		word_by_length = [''.join(permutation) for permutation in letter_permutations]
		words.extend(word_by_length)

	return words


def check_valid_words(words: list[str]) -> list[str]:
	enchant_obj = enchant.DictWithPWL(
		tag="en_UK",
		pwl="dictionary.txt"
	)

	correct_words = []
	for word in words:
		is_correct = enchant_obj.check(word)
		if is_correct:
			correct_words.append(word)

	return correct_words


def format_words_by_length(words: list[str]) -> dict[str, list[Any]]:
	min_word_length = len(words[0])
	max_word_length = len(words[-1])

	formatted_words = {}

	for lent in range(min_word_length, max_word_length + 1):
		formatted_words[f"{lent}"] = []

	for word in words:
		length = len(word)
		formatted_words[f"{length}"].append(word)

	return formatted_words


def retry():
	is_retry = input("Do you want to Try Again. ? y/n :- ")

	if not is_retry:
		retry()

	if is_retry == "n" or is_retry == 'N':
		exit(1)

	if is_retry == "y" or is_retry == "Y":
		main()

	retry()


def main():
	letters = get_letter()
	possible_words = make_words(letters=letters)
	correct_words = check_valid_words(possible_words)
	formatted_words = format_words_by_length(correct_words)
	print(formatted_words)

	retry()


if __name__ == '__main__':
	main()
