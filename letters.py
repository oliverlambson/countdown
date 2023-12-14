import logging
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import json
from string import ascii_lowercase

from numpy.typing import NDArray
import numpy as np


def get_alphabet_representation(partial_representation: Counter) -> dict[str, int]:
    return {letter: partial_representation.get(letter, 0) for letter in ascii_lowercase}


@dataclass
class Word:
    word: str
    full_representation: dict[str, int]
    vector: NDArray

    def __init__(self, word: str):
        self.word = word
        characters = sorted(word)
        partial_representation = Counter(characters)
        self.full_representation = get_alphabet_representation(partial_representation)
        self.vector = np.array(list(self.full_representation.values()))


def get_matches(input_letters: str, words: list[Word]) -> list[str]:
    input_word = Word(input_letters)

    result_matrix = -word_matrix + input_word.vector
    non_negative_rows = np.all(result_matrix >= 0, axis=1)
    indices = list(np.where(non_negative_rows)[0])
    matches = sorted(
        [word.word for i, word in enumerate(words) if i in indices],
        key=lambda x: len(x),
        reverse=True,
    )

    return matches


if __name__ == "__main__":
    letters = input("Countdown letters: ")
    letters = letters.lower()
    if not all(letter in ascii_lowercase for letter in letters):
        logging.error("Letters must be in the alphabet.")
        exit(1)

    logging.basicConfig(level=logging.INFO)

    logging.info("Loading dictionary...")
    words_file = Path("words.json")

    with words_file.open() as f:
        words_tmp = json.load(f)
    all_words = list(words_tmp.keys())

    word_words = list(filter(lambda x: 3 <= len(x) <= 9, all_words))
    words = [Word(word) for word in word_words]
    word_matrix = np.array([word.vector for word in words])
    logging.info("Dictionary loaded.")

    logging.info("Calculating matches...")
    matches = get_matches(letters, words)
    logging.info("Matches calculated.")

    print(matches)
