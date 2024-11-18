# Aufgabe Variable Swap

Gegeben:

```python
x = 5
y = 15
```

Ziel:

```python
x = 15
y = 5
```

### 1) Warum tauscht der folgende Programmcode die Werte der beiden Variablen nicht aus?

```python
x = y
y = x
```

In Python werden Befehle von oben nach unten ausgeführt.
Im ersten Schritt wird ``x`` der Wert von ``y`` (hier 15) zugewiesen, und der ursprüngliche Wert von ``x`` überschrieben.
Im zweiten Schritt erhält ``y`` den neuen Wert von ``x`` (auch 15, da ``x`` bereits modifiziert wurde).
Beide Werte sind nun 15, nicht getauscht.

### 2) Wie müsste der code aussehen, damit die Werte getauscht werden?

Um die Werte zu tauschen, muss der ursprüngliche Wert von ``x`` in einer weiteren Variable gespeichert werden.
Danach kann der Wert von ``y`` auf ``x`` und der gespeicherte Wert auf ``y`` gesetzt werden:

```python
temp = x
x = y
y = temp
```

Alternativ kann man die genannte Tuple-Assignment Syntax verwenden:

```python
x, y = y, x
```