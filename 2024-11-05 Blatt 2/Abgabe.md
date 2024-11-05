# Abgage

## Aufgabe Wegbeschreibung

### Aufgabe a)

```
// Ausgangspunkt
Ich bin eine Person ohne gespeichertes Wissen über das Gebäude Staudingerweg 9.
Ich befinde mich im Raum der Mathe/Informatik Fachschaft im 4. OG des Staudingerweg 9.

// Zum Fachschaftskühlschrank gehen
Ich verlasse den Raum der Fachschaft und betrete damit den Flur.
Ich gehe geradeaus in das Zimmer gegenüber mit der Aufschrift Fachschaftsküche.
Ich betrete die Fachschaftsküche.
Ich gehe zum Kühlschrank.

// Prüfen, ob Eistee im Kühlschrank ist
Ich öffne den Kühlschrank.
Ich suche im Kühlschrank nach Eistee.
Wenn Eistee ∈ Kühlschrank:
    Ich nehme eine Flasche Eistee heraus.
    Ich schließe den Kühlschrank.
    Ich bezahle den Eistee.
    Ich trinke den Eistee.

    Ich beende den gesamten Vorgang.

Sonst:
    Ich schließe den Kühlschrank.

// Zum Getränkeautomaten gehen
Ich verlasse die Fachschaftsküche.
Ich gehe nach rechts bis zum Ende des Flurs.
Ich verlasse den Flur und gelange in das Foyer.
Ich gehe nach links zum Aufzug.
Ich drücke den Knopf, um den Aufzug zu rufen.
Während der Aufzug nicht da ist:
    Ich warte.
Ich betrete den Aufzug.
Ich drücke den Knopf für das Erdgeschoss (EG).
Solange der Aufzug nicht im EG ist:
    Ich warte.
Ich verlasse den Aufzug im Erdgeschoss.
Ich gehe zum Getränkeautomaten gegenüber des Aufzugs.

// Getränk im Automaten kaufen
Ich überprüfe die Auswahl am Getränkeautomaten auf Eistee.
Wenn Eistee ∈ Automaten:
    Ich wähle Eistee am Automaten aus.
    Ich bezahle den Eistee.
    Ich nehme den Eistee aus dem Automaten.
    Ich trinke den Eistee.

    Ich beende den gesamten Vorgang.
Sonst:
    Ich wähle Cola Zero am Automaten aus.
    Ich bezahle die Cola Zero.
    Ich nehme die Cola Zero aus dem Automaten.
    Ich trinke die Cola Zero.

    Ich beende den gesamten Vorgang.
``` 

### Aufgabe b) ""TO-DO

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

Die while schleife läuft genau $n/2$ durch, da sie jeden Durchgang 2 Socken entfernt und ein Paar bildet.

In einer zufällgen $k$-ten Iteration sind noch $n-2\cdot(k-1)$ Socken da.
$$ \begin{split} It_1&: 100-2*(1-1)=100\\It_2&: 100-2*(2-1)=98\\ It_n&:... \end{split}$$

Dazu kommt, dass in dieser $k$-ten Interation eine Referenzsocke abgezogen wurde. Daraus folgt:

$$
\begin{split}
    \sum_{k=1}^{\frac n2} &= n-2\cdot(k-1)-1\\
    &=n-2k+2-1
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

Da gegeben ist, dass alle $ n $ Socken, gleichmäßig auf $ f $ Farben verteilt sind, hat jede Farbe $ n/f $ Socken. 

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

Im Vergleich zum Algorithmus aus Aufgabe 2 reduziert sich die Laufzeit, da jede Socke nur mit den Socken ihrer eigenen Farbe verglichen wird und nicht mit allen $ n $ Socken. Dies sieht man, wenn man die gegebenen Werte einfügt (2500 vorher, 500 nachher).

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
