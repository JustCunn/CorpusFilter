# Corpus Filter

A basic programme that filters out poor data for Neural Machine Translation systems. it is compatible with languages using the Roman Alphabet (including Diacritics like **_á_**)

It has the following filters:

__Copy -__ Checks the source and target sentences to make sure they don't match each other.

__Duplicate -__ Checks to make sure the sentence isn't repeated anywhere else.

__Sentence Ratio -__ Compares the lengths of the corresponding sentences.

__Character Ratio -__ Compares the amount of non-alphabetical symbols to alphabetical symbols.

__Length -__ Checks to make sure the sentences aren't too small or too large.
