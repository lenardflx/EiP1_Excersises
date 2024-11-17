Variable Swap
in der ersten Zeile wird x mit dem Wert von y belegt, dabei geht der ursprüngliche Wert von x verloren und in der zweite Zeile wird y mit dem Wert von x belegt, da aber der Wert von x in der Zeile davor schon geändert wurde, haben beide Variablen den Wert 15
2) 
a=x
x=y
y=a

Rammstein
for i in range (1, 11):
	if (i==10): 
		print(„aus“)
	else:
		print(i)


for i in range (1,5):
	if(i ==3):
		print(i + “sie ist der hellste Stern von allen“)
	else: 
		print(i + „hier kommt die Sonne“)







gifts = ['partridge in a pear tree', 'turtle doves', 'French hens', 'calling birds', 'gold rings','geese alaying',
\
'swans a-swimming', 'maids a-milking', 'ladies dancing', 'lords a-leaping', 'pipers piping', 'drummers
drumming',]
def song (a):
for i in range(0,11):
	if (i==0):
print(„on the“ + i + „. day of Christmas my true love sent to me
print(“gifts[0]”)
	els
rekursion methode in sich selbst aufrufen
kp mehr















Mittelwert
1)
summe=0
for i in range (0, len(test_list)):
	summe=summe+ test_list[i]
print( “Mittelwert:” + summe/len(test_list))


2)
summe=0
summeab=0
for i in range (0, len(test_list)):
	summe=summe+ test_list[i]
mittelwert= summe/len(test_list)
print( “Mittelwert:” + mittelwert)
for j in range (0, len(test_list)):
	summeab= summeab + (test_list[j]-mittelwert)**2
stabweichung=summeab/len(test_list)
print( “Standardabweichung:” + stabweichung)

