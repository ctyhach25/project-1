# Author: Caitlyn Tyhach
# Git ID: ctyhach25
# Date: 6/24/2026
# Description: This module uses the Levenshtein distance between strings to say how similar they are (in text, not in meaning).

from fuzzywuzzy import fuzz

def string_distance(string_list, target_string):
    results = {}
    for item in string_list:
        results[item] = fuzz.ratio(item, target_string)
    return results

# Note: I wasn't quite sure if my code was supposed to print something back, so I just kept it as a return. The assignment didn't specifically state a print, but it did include the term 'return', so I went off of that.
