### Aufgabe 1:

**Vorteil:** Die Angabe von Typen bei Variablen macht den Code übersichtlicher und hilft dabei, Fehler (wie das Setzen eines String in eine Int-Variable zum beispiel) schneller zu erkennen. Besonders in großen Codes kann das nützlich sein, weil IDEs anhand des Typen Vorschläge machen. In Sprachen wie Rust ist das sogar verpflichtend, um Speicher effizient zu nutzen.

**Nachteil:** Immer den Typ anzugeben macht Code umfangreicher und manchmal etwas schwerer zu lesen. Außerdem können DataTypes die Flexibilität einschränken, da in Python z.B. die Möglichkeit besteht den Variablen-Typ zu ändern.

## Aufgabe 2

**(a)** `True`: Der Vergleich mit `==` ruft die Funktion `__eq__` von `Frac` auf, welche prüft, ob `x` und `y` dieselben Werte für die Attribute `num` und `denum` haben.

**(b)** `False`: Der Operator `is` prüft, ob zwei Variablen auf denselben Speicherort zeigen (dasselbe Objekt sind). Obwohl `x` und `y` inhaltlich gleich sind, sind sie zwei unterschiedliche Instanzen der Klasse `Frac`.

**(c)** `True`: `z` und `x` zeigen auf dasselbe Objekt, dadurch haben `num` und `denum` dieselben Werte.

**(d)** `True`: `z` zeigt auf dasselbe Objekt wie `x`, daher gibt der Operator `is` `True` aus.

### Aufgabe 3

In Programmiersprachen gibt es typischerweise **immutable** und **mutable** Daten.
Immutable Daten (z.B. `int` oder `NoneType`) können nicht direkt verändert werden.
In Python wird dann der alte Wert gelöscht und ein neuer Wert erstellt.
Mutable Typen wie `list` hingegen können direkt am selben Speicherort verändert werden.

- **`replace_nan1`**: `[None, 2, 3, None, 5]` Die Funktion iteriert über die Werte der Liste. `val` ist eine lokale, immutable Variable der Schleife, also wird der Wert der Liste nicht geändert.

- **`replace_nan2`**: `[0, 2, 3, 0, 5]` Hier wird der Index `i` der Liste verwendet. Da Listen mutable sind, wird der Wert direkt im Speicher an derselben Stelle überschrieben.

Dadurch ist `replace_nan2` die korrekte Funktion.