"""
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence.
The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. 
If word is not a substring of sequence, word's maximum k-repeating value is 0.
Given strings sequence and word, return the maximum k-repeating value of word in sequence.
"""


def maxRepeating(sequence: str, word: str) -> int:
    """
    Args:
        sequence: The first parameter.
        str: The second parameter.

    Returns:
        int representing max repeating string
    """
    if(word not in sequence):
        return 0
    return sequence.count(word)