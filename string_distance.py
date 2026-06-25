# Author: Caitlyn Tyhach
# Git ID: ctyhach25
# Date: 6/24/2026
# Description: This module uses the Levenshtein distance between strings to say how similar they are (in text, not in meaning).

from fuzzywuzzy import fuzz

def string_distance(string_list, target_string):
    results = {}
    for s in string_list:
        results[s] = fuzz.ratio(s, target_string)
    return results

