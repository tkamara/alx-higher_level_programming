#!/usr/bin/python3
def multiple_returns(sentence):
    for length in sentence:
        count = len(sentence)
        if count == 0:
            return count, None
        else:
            return count, sentence[0]
