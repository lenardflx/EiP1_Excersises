UMLAUTS = {'a': 'ä', 'o': 'ö', 'u': 'ü'}

def replace_second_vowel_independently(text):
    result = []
    for word in text.split():
        vowel_count = 0
        new_word = ""
        for char in word:
            if char.lower() in UMLAUTS:
                vowel_count += 1
                if vowel_count == 2:
                    char = UMLAUTS[char.lower()].upper() if char.isupper() else UMLAUTS[char.lower()]
            new_word += char
        result.append(new_word)
    return " ".join(result)

def replace_second_vowel_by_type(text):
    result = []
    for word in text.split():
        vowel_count = {'a': 0, 'o': 0, 'u': 0}
        new_word = ""
        for char in word:
            if char.lower() in UMLAUTS and vowel_count[char.lower()] < 2:
                vowel_count[char.lower()] += 1
                if vowel_count[char.lower()] == 2:
                    char = UMLAUTS[char.lower()].upper() if char.isupper() else UMLAUTS[char.lower()]
            new_word += char
        result.append(new_word)
    return " ".join(result)

if __name__ == "__main__":
    tests = ["Motorhead", "Heavy Metal Umlaute", "aaauuu oooo iii kukukuku", "Python super Programmiersprache"]
    for test in tests:
        print(f'Unabhängig: "{test}" → "{replace_second_vowel_independently(test)}"')
        print(f'Nach Typ:   "{test}" → "{replace_second_vowel_by_type(test)}"')