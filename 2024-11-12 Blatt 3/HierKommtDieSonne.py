# Aufgabe 1a:

for i in range(10):
    if i+1 != 10:
        print(i+1)
    else:
        print("aus")

print("----")

# Aufgabe 1b:

for i in range(4):
    if i+1 == 3:
        print(i+1,"sie ist der hellste Stern von allen")
    else:
        print(i+1,"hier kommt die Sonne")

print("----")

# Aufgabe 2:

gifts = [
    'partridge in a pear tree', 'turtle doves', 'French hens', 'calling birds', 'gold rings', 'geese a-laying',
    'swans a-swimming', 'maids a-milking', 'ladies dancing', 'lords a-leaping', 'pipers piping', 'drummers drumming'
]

cardinal = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
ordinal = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

for day in range(12): # Für jede Strophe
    print("On the", ordinal[day], "day of Christmas my true love sent to me")

    for n in range(day + 1): # Für jede "spezial" Zeile der Strophe
        gift_index = day - n
        if day > 0 and gift_index == 0:
            print("And a partridge in a pear tree.")
        elif gift_index == 0:
            print("A partridge in a pear tree.")
        else:
            print(cardinal[gift_index], gifts[gift_index]+",")
    print()
