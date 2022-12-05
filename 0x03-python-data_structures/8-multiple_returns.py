#!/usr/bin/python3
def multiple_returns(sentence):
    index = 0
    first = sentence[index]
    for length in sentence:
        count = len(sentence)
        if count == 0:
            first = None
            return count, first
        else:
            return count, first
