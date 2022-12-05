#!/usr/bin/python3
def multiple_returns(sentence):
    """Return the length of string and it's first string"""
    if sentence == "":
        return None
    return (len(sentence), sentence[0])
