1a) Ja: Im schlimmsten Fall muss der Algorithmus alle möglichen Lösungen durchprobieren,
    was oft zu einer exponentiellen Laufzeit führt. Dadurch prüft er jede Kombination, was zu O(2^n) führt.

1b) Nein: Theoretisch kann JEDER rekursive Algorithmus iterativ geschrieben werden.
    Bei Backtracking kann der Zwischenstand in einem Stack gespeichert und später wieder aufgerufen werden.

1c) Ja: Der Ablauf von Backtracking findet selbst in einer Baumstruktur statt,
    da er schrittweise alle Möglichkeiten durchgeht. Daher eignet er sich für solche Probleme.

1d) Nein: Vor allem für das iterieren durch verschiedene Möglichkeiten oder
    Datenvergleich kann eine for schleife sinnvoll sein.

1e) Ja: Durch Branch-and-Bound bleibt die Struktur des Algorithmus gleich. Es wird zusätzlich geprüft,
    ob die aktuelle Lösung besser ist als die anderen. Das kann die Laufzeit aber start verbessern.