UMLAUTS = {"a": "ä", "o": "ö", "u": "ü"}

def replace_second_vowel_independently(text):
    def edit_word(word):
        c,res = 0, ""
        for l in word:
            if l.lower() in UMLAUTS:
                c += 1
                if c == 2:
                    l = UMLAUTS[l.lower()].upper() if l.isupper() else UMLAUTS[l.lower()]
            res += l
        return res
    return " ".join(map(edit_word, text.split()))

def rep2indep(text):
    return " ".join(map(lambda word: (lambda c=0: ''.join(
            (UMLAUTS[l.lower()].upper() if l.isupper() else UMLAUTS[l.lower()]) if l.lower()
            in UMLAUTS and (c := c + 1) == 2 else l for l in word))(),text.split()))

def replace_second_vowel_by_type(text):
    def edit_word(word):
        c, done, res = {"a": 0, "o": 0, "u": 0}, False, ""
        for l in word:
            if l.lower() in UMLAUTS and not done:
                c[l.lower()] += 1
                if c[l.lower()] == 2:
                    l = UMLAUTS[l.lower()].upper() if l.isupper() else UMLAUTS[l.lower()]
                    done = True
            res += l
        return res
    return " ".join(map(edit_word, text.split()))

def rep2type(text):
    return " ".join(map(lambda word: (lambda c={"a": 0, "o": 0, "u": 0}, done=False: ''.join(
        (UMLAUTS[l.lower()].upper() if l.isupper() else UMLAUTS[l.lower()])
        if l.lower() in UMLAUTS and not done and (c.update({l.lower(): c[l.lower()] + 1}) or c[l.lower()] == 2)
        and (done := True) else l for l in word))(), text.split()))

if __name__ == "__main__":
    for x in ["Motorhead", "Heavy Metal Umlaute", "aaauuu oooo iii kukukuku", "Python super Programmiersprache"]:
        print(f"Unabhängig: '{x}' → '{rep2indep(x)}'")
        print(f"Nach Typ:   '{x}' → '{rep2type(x)}'")