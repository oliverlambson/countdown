# Countdown

I'm bad at the letters on countdown, so I've developed a cheat.

## Letters

### The aLgoRiThM

- Represent a word as an ordered vector of the count of each letter in the word.
- Stack all word vectors to form a matrix that represents the dictionary.
- `-dictionary_matrix + countdown_letters_vector` --> all rows that don't contain any negatives are valid solutions

```py
all_words = ...

# e.g.
word = "reader"
word_representation = [
  # a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
    1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0
]

letters = "ditrlerae"
letters_representation = [
  # a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
    1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0
]

word_is_valid = min([l - w for l, w in zip(letters_representation, word_representation)]) >= 0
```

## References

words.json: https://github.com/dwyl/english-words
