"""The goal of this kata is to write a function that takes two inputs: a string and a character.
The function will count the number of times that character appears in the string.
The count is case insensitive."""

def count_char(string, character):
    return list(string.lower()).count(character.lower())

