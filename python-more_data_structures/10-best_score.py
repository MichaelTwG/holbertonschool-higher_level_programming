#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = 0
    for key, value in a_dictionary.items():
        if value > score:
            highest_score_key = key
            score = value
    return highest_score_key
