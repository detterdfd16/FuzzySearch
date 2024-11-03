## Fuzzy Search based on Damerau–Levenshtein distance  

The string similarity calculation method is the Damerau-Levenstein distance (`edit_distance` function)
It calculates the number of deletions, insertions, substitutions and transpositions required to get from the first string to the second.  
This method was chosen for:
- Speed. The time complexity of DL distance calculation is O(N*M) where N, M - string lengths.
- Accuracy. In most cases, it provides a good distance estimate in the context of company names. Most typos, abbreviations, or punctuation variations can be expressed in a low amount of basic operations of DL distance.

