## Fuzzy Search based on Damerau–Levenshtein distance  

The string similarity calculation method is the Damerau-Levenstein distance (`edit_distance` function)
It calculates the number of deletions, insertions, substitutions and transpositions required to get from the first string to the second.  
This method was chosen for:
- Speed. The time complexity of DL distance calculation is O(N*M) where N, M - string lengths.
- Accuracy. In most cases, it provides a good distance estimate in the context of company names. Most typos, abbreviations, or punctuation variations can be expressed in a low amount of basic operations of DL distance.
There are a few edge cases for this algorithm:
- Company abbreviations, such as ones used on the stock market, may be hard to recognize via only DL distance, e.g. American Battery Technology Company is encoded as "ABAT"
- Companies that changed their names, e.g. Facebook -> Meta, Twitter -> X. DL distance cannot be applied in this case.
To address these issues, one of the solutions is to provide context, i.e. a stock abbreviation list.  
During the search look for matches for the corresponding abbreviation or company name:
`fuzzy_search("Apple")` should give `"AAPL"` a distance of 0, and vice versa.  
