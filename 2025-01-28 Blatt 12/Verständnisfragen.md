1a) Ja: Im schlimmsten Fall ist die richtige Lösung die letzte, die der Algorithmus findet oder
    keine gute Abbruchbedingung vorhanden ist. Er würde in jedem Node alle n Möglichkeiten durchgehen. (2^n)

1b) Nein: Ein jeder rekursive Algorithmus kann auch iterativ geschrieben werden,
    indem der Stand als Stack gespeichert wird.

1c) Ja: Backtracking läuft in einer Baumstruktur, daher eignet es sich für solche Probleme.

1d) Nein: Es kann immer sinnvoll sein, für Vergleiche o.ä. for-Schleifen zu verwenden.

1e) Ja: Im Bezug auf Backtracking prüft branch and bound zusätzlich, ob der aktuelle Pfad eine bessere
    Lösung als die bisher beste ist. Aber "lediglich" ist hier falsch, da der Algorithmus
    dadurch deutlich besser werden kann.