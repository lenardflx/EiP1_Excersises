# Abgabe

## Aufgabe Wegbeschreibung

### Aufgabe a)

```
// Ausgangspunkt

Eine Person befindet sich im Fachschaftsraum der Informatik im 4. OG des Staudingerweg 9


// Zum Fachschaftskühlschrank gehen

Verlasse den Raum der Fachschaft
Gehe in das Zimmer mit der Aufschrift Fachschaftsküche


// Prüfen, ob Eistee im Kühlschrank ist

Öffne den Kühlschrank.
Wenn Eistee ∈ Kühlschrank:
    Nehme den Eistee heraus
    Trinke den Eistee
    Beende den gesamten Vorgang


// Zum Getränkeautomaten gehen

Schließe den Kühlschrank
verlasse die Fachschaftsküche.
Gehe zum Aufzug.
Fahre ins Erdgeschoss.
Gehe zum Getränkeautomaten.


// Getränk im Getränkeautomaten kaufen

Wenn Eistee ∈ Getränkeautomaten:
    Wähle Eistee am Automaten
    Bezahle den Eistee
    Nehme den Eistee aus dem Automaten
    Trinke den Eistee
    Beende den gesamten Vorgang
Sonst:
    Wähle Cola Zero am Automaten
    Bezahle den Cola Zero
    Nehme den Cola Zero aus dem Automaten
    Trinke den Cola Zero
    Beende den gesamten Vorgang
``` 

### Aufgabe b)

Ein Getränkeautomat ist ein rechteckiger Kasten. Er ist an der Vorderseite mit einer Glasscheibe ausgestattet, die es dir ermöglicht in das Innere des Automaten zu sehen, wo verschiedene Getränke in einzelnen Fächern in einem Raster angeordnet sind. 

Diese Getränke kannst du anhand ihrer Farben, Formen und Beschriftungen unterscheiden. Jedes Fach, in dem sich ein Getränk befindet, ist mit einer spezifischen Nummer versehen, die du benötigst, um das gewünschte Getränk auszuwählen.

Um dein Getränk zu wählen, musst du die entsprechende Nummer über ein Tastenfeld eingeben. Dieses befindet sich rechts mittig neben der Glasscheibe auf einem Bedienfeld.

Das Tastenfeld besteht aus 12 Tasten: den Nummerntasten 0-9, einer Abbruchtaste und einer Bestätigungstaste.

Jede Taste ist ein kleines Rechteck, welches du durch leichten Druck bedienen kannst, damit der Automat eine Aktion durchführt.

Um die Auswahl eines Getränks zu treffen, verwendest du die Tasten 0-9. Für jede Ziffer (von links nach rechts) der gewünschten Nummer wählst du die jeweilige Taste mit derselben Nummer.

Die Abbruchtaste kann verwendet werden, um die Eingabe zu beenden und die Auswahl abzubrechen.

Sobald Zahl vollständig eingegeben wurde, bestätigst du deine Auswahl, indem du die Bestätigungstaste drückst.


## Aufgabe Socken

### Aufgabe 1)
```
ungepaarter_stapel ist eine Menge aller Socken
gepaarter_stapel ist eine leere Liste

während ungepaarter_stapel nicht leer ist:
    entferne zwei zufällige Socken aus ungepaarter_stapel

    wenn beide Socken die gleiche Farbe und das gleiche Modell haben:
        füge beide Socken alls gruppe zu gepaarter_stapel hinzu
    else:
        füge beide Socken wieder zu ungepaarter_stapel hinzu
```
Auf unendliche Zeit gesehen, wird dieser Code garantiert terminieren. Zwar können dieselben Paare an Stapeln immer wieder gezogen werden, jedoch verringert sich die Menge von ``ungepaarter_stapel`` stetig.

### Aufgabe 2)

Im schlimmsten Fall muss jede  ``Referenzsocke`` alle anderen Socken von ``ungepaarter_stapel`` durchsuchen, bis sie ihr Paar findet.

In einer zufällgen $k$-ten Iteration sind noch $n-2\cdot(k-1)$ Socken da.

$$
\begin{split}
    It_1&: 100-2*(1-1)=100\\
    It_2&: 100-2*(2-1)=98\\
    It_n&: \space ...
\end{split}
$$

Dazu kommt, dass in dieser $k$-ten Interation eine Referenzsocke abgezogen wurde.
Die while Schleife läuft genau $n/2$ durch, da sie jeden Durchgang 2 Socken entfernt und ein Paar bildet.

Daraus folgt:

$$
\begin{split}
    \sum_{k=1}^{\frac n2} &= n-2\cdot(k-1)-1
    \\&=n-2k+2-1
    \\&=n-2k+1
\end{split}
$$

Im gegebenen Beispiel wäre dies dann:

$$
\begin{split}
    \sum_{k=1}^{50} &=100-2k+1\\&=2500
\end{split}
$$

### Aufgabe 3a)
```
gepaarter_stapel ist leer
ungepaarter_stapel enthält alle Socken

farben = liste aller Farben
farbgruppen = leeres Wörterbuch mit jeder Farbe als Schlüssel 

for(alle socken in ungepaarter_stapel):
    füge socke zur entsprechenden farbgruppe hinzu

for(jeden farb_stapel in farbgruppen):

while(farb_stapel ist nicht leer):
    nehme eine Referenzsocke vom farb_stapel
    for(alle restlichen Socken in farb_stapel):
        vergleiche die Socke mit der Referenzsocke
        if(die beiden Socken bilden ein Paar):
            falte beide Socken zusammen und lege sie auf gepaarter_stapel
            break (verlasse die for-schleife)

```

### Aufgabe 3b)

Im schlimmsten Fall muss jede ``Referenzsocke`` alle anderen Socken im ``farb_stapel`` durchsuchen, bis sie ihr Paar findet. Da die Socken nun nach Farben gruppiert sind, ist die Anzahl der Iterationen geringer.

Da gegeben ist, dass alle $n$ Socken, gleichmäßig auf $f$ Farben verteilt sind, hat jede Farbe $n/f$ Socken. 

Daraus ergibt sich:

$$
   f \cdot \sum_{k=1}^{\frac n{2\cdot f}} =\left(\frac{n}{f} - 2k + 1\right)
$$

In unserem Beispiel:

$$
\begin{split}
    5 \cdot \sum_{k=1}^{10} &=\left(20 - 2k + 1\right)\\&=500
\end{split}
$$

Im Vergleich zum Algorithmus aus Aufgabe 2 reduziert sich die Laufzeit, da jede Socke nur mit den Socken ihrer eigenen Farbe verglichen wird und nicht mit allen $n$ Socken. Dies sieht man, wenn man die gegebenen Werte einfügt (2500 vorher, 500 nachher).

## Aufgabe Quadratwurzel
### Aufgabe 1)
```
n ist eine beliebige positive rationale Zahl
x1 ist ein Startwert für die Näherung 
Genauigkeit = 0.00001  // die fünf Nachkommastellen

Wiederhole bis Schleife unterbrochen wird:

    h = n / x  //  x1 * h = n
    Wenn h == x1
        x (=x1) gefunnden
        beende programm und gebe x1 zurück

    xNeu = (x1 + h) / 2
    Wenn |xNeu - x1| < Genauigkeit
        x gefunden
        runde xNeu auf 5 Nachkommastellen
        beende programm und gebe xNeu zurück
    x1 = xNeu
```
### Aufgabe 2)
> Alle werte sind auf 5 Nachkommastellen gerundet
##### #1
- x1 = 0.2
- h = n/x1 = 2/0.2 = 10.0
- xNeu = (x1+h)/2 = 0.2 + 10.0/2 = 5.1
- |x1 - √2| = |0.2 - 1.41421| ≈ 1.21421

##### #2
- x1 = 5.1
- h = n/x1 = 2/5.1 = 0.39216
- xNeu = (x1+h)/2 = 5.1 + 0.39216/2 = 2.74608
- |x1 - √2| = |5.1 - 1.41421| ≈ 3.68579

##### #3
- x1 = 2.74608
- h = n/x1 = 2/2.74608 = 0.72831
- xNeu = (x1+h)/2 = 2.74608 + 0.72831/2 = 1.73719
- |x1 - √2| = |2.74608 - 1.41421| ≈ 1.33186

##### #4
- x1 = 1.73719
- h = n/x1 = 2/1.73719 = 1.15128
- xNeu = (x1+h)/2 = 1.73719 + 1.15128/2 = 1.44424
- |x1 - √2| = |1.73719 - 1.41421| ≈ 0.32298

##### #5
- x1 = 1.44424
- h = n/x1 = 2/1.44424 = 1.38481
- xNeu = (x1+h)/2 = 1.44424 + 1.38481/2 = 1.41453
- |x1 - √2| = |1.44424 - 1.41421| ≈ 0.03002

##### #6
- x1 = 1.41453
- h = n/x1 = 2/1.41453 = 1.4139
- xNeu = (x1+h)/2 = 1.41453 + 1.4139/2 = 1.41421
- |x1 - √2| = |1.41453 - 1.41421| ≈ 0.00031

##### #7
- x1 = 1.41421
- h = n/x1 = 2/1.41421 = 1.41421
- xNeu = (x1+h)/2 = 1.41421 + 1.41421/2 = 1.41421
- |x1 - √2| = |1.41421 - 1.41421| ≈ 0.0
