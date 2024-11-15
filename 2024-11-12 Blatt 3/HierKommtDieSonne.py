# Aufgabe 1a:

n = 10
for i in range(1,n+1):
    if i != 10:
        print(i)
    else:
        print("aus")

print("\n----\n")

# Aufgabe 1b:

n = 4
for i in range(1,n+1):
    if i  == 3:
        print(f"{i}, sie ist der hellste Stern von allen")
    else:
        print(f"{i}, hier kommt die Sonne")

print("\n----\n")

# Aufgabe 2:

gifts = [
    'partridge in a pear tree', 'turtle doves', 'French hens', 'calling birds', 'gold rings', 'geese a-laying',
    'swans a-swimming', 'maids a-milking', 'ladies dancing', 'lords a-leaping', 'pipers piping', 'drummers drumming'
]

# Zahlen als Wörter
cardinal = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"]
ordinal = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh",
           "twelfth"]

for day in range(12):  # Für jede Strophe
    print("On the", ordinal[day], "day of Christmas my true love sent to me")

    for n in range(day + 1):  # Für jede Zeile der Strophe
        verse = day - n # rückwärts zählen
        if day > 0 and verse == 0: # Für Verse 2 bis 12
            print("And a partridge in a pear tree.")
        elif verse == 0: # Für Vers 1
            print("A partridge in a pear tree.")
        else:
            print(f"{cardinal[verse]} {gifts[verse]},")
    print()  # Leerzeile nach jeder Strophe
