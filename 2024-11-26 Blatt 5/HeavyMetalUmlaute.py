UMLAUTS = {"a": "ä", "A": "Ä", "o": "ö", "O": "Ö", "u": "ü", "U": "Ü"}

def rep2indep(text):
    return " ".join(map(lambda w,c=0: ''.join(UMLAUTS[l] if l in UMLAUTS and (c:=c+1)==2 else l for l in w),text.split()))

def rep2type(text):
    return " ".join(map(lambda w,c={"a":0,"o":0,"u":0}: ''.join(UMLAUTS[l] if l in UMLAUTS and (c.update({l.lower():
        c[l.lower()] + 1}) or c[l.lower()] == 2) and not any(c.values()) >= 2 else l for l in w), text.split()))

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
            if l in UMLAUTS:
                c[l.lower()] += 1
                if c[l.lower()] == 2 and not any(c.values()) >= 2:
                    l = UMLAUTS[l]
            res += l
        return res
    return " ".join(map(edit_word, text.split()))

if __name__ == "__main__":
    for x in ["Motorhead", "Heavy Metal Umlaute", "aaauuu oooo iii kukukuku", "Python super Programmiersprache"]:
        print(f"Unabhängig: '{x}' → '{rep2indep(x)}'")
        print(f"Nach Typ:   '{x}' → '{rep2type(x)}'")
