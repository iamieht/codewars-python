def anagrams(word, words):
    """
    Input: String:List of Strings
    produces a List with anagrams (words that contains the same letters)
    """
    sortedWord = ''.join(sorted(word))
    anagrams = []

    for word in words:
        if ''.join(sorted(word)) == sortedWord:
            anagrams.append(word)
    
    return anagrams


def anagrams_better(word, words):
    return [item for item in words if sorted(item)==sorted(word)]

#Tests
print("Expected results: ['aabb', 'bbaa']")
print("Actual results:", anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print("Expected results: ['carer', 'racer']")
print("Actual results:", anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))

#Tests with anagrams_better
print("Expected results: ['aabb', 'bbaa']")
print("Actual results:", anagrams_better('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print("Expected results: ['carer', 'racer']")
print("Actual results:", anagrams_better('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))