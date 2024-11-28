UMLAUTS = {"a":"ä","A":"Ä","o":"ö","O":"Ö","u":"ü","U":"Ü"}
def rep2merged(text, indep):
    return " ".join(map(lambda w, c: ''.join(UMLAUTS[l] if l in UMLAUTS and ((indep and (c:=c+1)==2) or (not indep and
        not 2 in c.values() and (c.update({l.lower(): c[l.lower()]+1}) or c[l.lower()]==2))) else l for l in w),
        text.split(),[0 if indep else {"a": 0, "o": 0, "u": 0} for _ in text.split()]))
for x in ["Motorhead", "Heavy Metal Umlaute", "aaauuu oooo iii kukukuku", "Python super Programmiersprache"]:
    print(*(f"{t}:\t'{x}' → '{rep2merged(x, m)}'" for t, m in [["Unabhängig", True], ["Nach Typ", False]]), sep="\n")

# Alt
def rep2indep(text):
    return " ".join(map(lambda w,c=0: ''.join(UMLAUTS[l] if l in UMLAUTS and (c:=c+1)==2 else l for l in w),text.split()))
def rep2type(text):
    return " ".join(map(lambda w,c: ''.join(UMLAUTS[l] if l in UMLAUTS and not 2 in c.values() and (c.update({l.lower():
    c[l.lower()]+1}) or c[l.lower()]==2) else l for l in w),text.split(),[{"a":0,"o":0,"u":0} for _ in text.split()]))