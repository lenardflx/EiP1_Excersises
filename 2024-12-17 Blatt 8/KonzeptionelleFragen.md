### Aufgabe 1:

**Vorteil:** Die Angabe von Typen bei Variablen macht den Code übersichtlicher und hilft dabei, Fehler (wie das Setzen eines String in eine Int-Variable zum beispiel) schneller zu erkennen. Besonders in großen Codes kann das nützlich sein, weil IDEs bessere Vorschläge machen und wissen, welche Art von Daten gegeben oder erfordert werden. In Sprachen wie Rust ist das sogar verpflichtend, um Speicher effizient zu nutzen.

**Nachteil:** Immer den Typ anzugeben macht Code umfangreicher und etwas schwerer zu lesen. Außerdem können sie die Flexibilität von Python einschränken, da in Python z. B. die Möglichkeit besteht den Typ einer Variable zu ändern.

## Aufgabe 2

**(a)** `True`: Der Vergleich mit `==` prüft, ob die Inhalte der Objekte gleich sind, indem er die Funktion `__eq__` von `Frac` aufruft. Da `x` und `y` dieselben Werte für die Attribute `num` und `denum` haben, wird `True` ausgegeben.

**(b)** `False`: Der Operator `is` prüft, ob zwei Variablen auf denselben Speicherort zeigen (dasselbe Objekt sind). Obwohl `x` und `y` inhaltlich gleich sind, sind sie zwei unterschiedliche Instanzen der Klasse `Frac`.

**(c)** `True`: `z` ist ein Zeiger auf `x`. Wenn `__eq__` aufgerufen wird, haben daher `num` und `denum` dieselben Werte.

**(d)** `True`: Da `z` wie gesagt auf `x` zeigt, wird `is` `True` ausgeben, da beide auf denselben Speicherslot zeigen.

### Aufgabe 3

In Programmiersprachen (wie Python) gibt es typischerweise zwei Arten von Daten: **immutable** und **mutable**. Immutable Daten (z. B. `int` oder `NoneType`) können nicht direkt verändert werden. Wenn sie in PY geändert werden, wird der alte Wert gelöscht und ein neuer Wert an einer neuen Speicherstelle erstellt. Mutable Typen wie `list` hingegen können direkt verändert werden, und die Änderungen wird im Speicher an derselben Stelle überschrieben.

- **`replace_nan1`**: `[None, 2, 3, None, 5]` Die Funktion iteriert über die Werte der Liste und überschreibt die Variable `val`. Jedoch ist `val` eine temporäre Variable innerhalb der Schleife (und immutable). Änderungen sind also nur Lokal und nicht in der Liste.

- **`replace_nan2`**: `[0, 2, 3, 0, 5]` Hier wird der Index `i` der Liste verwendet. Da Listen mutable sind, wird der Wert im Speicher überschrieben, und die Änderung ist in der Liste direkt.

`replace_nan2` ist die korrekte Funktion.