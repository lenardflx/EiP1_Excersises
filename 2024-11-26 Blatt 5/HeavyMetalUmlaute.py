UMLAUTS = {"a":"ä","A":"Ä","o":"ö","O":"Ö","u":"ü","U":"Ü"}

def replace_second_vowel_independently(text):
    def edit_word(word):
        c,res = 0, ""
        for l in word:
            if l in UMLAUTS:
                c += 1
                if c == 2:
                    l = UMLAUTS[l]
            res += l
        return res
    return " ".join(map(edit_word, text.split()))

def replace_second_vowel_by_type(text):
    def edit_word(word):
        c, res = {"a": 0, "o": 0, "u": 0}, ""
        for l in word:
            if l in UMLAUTS and not 2 in c.values():
                c[l.lower()] += 1
                if c[l.lower()] == 2 and 2 in c.values():
                    l = UMLAUTS[l]
            res += l
        return res
    return " ".join(map(edit_word, text.split()))

if __name__ == "__main__":
    for x in ["Motorhead", "Heavy Metal Umlaute", "aaauuu oooo iii kukukuku", "Python super Programmiersprache"]:
        print(f"Unabhängig: '{x}' → '{replace_second_vowel_independently(x)}'")
        print(f"Nach Typ:   '{x}' → '{replace_second_vowel_by_type(x)}'")