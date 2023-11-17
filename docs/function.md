# Definition von Funktionen 

Wenn man komplexere Abbildungen mit Schulplots zeichnen will, stellt man häufig
fest, dass eine oder mehrere Funktionen an unterschiedlichen Stellen immer
wieder benötigt werden. 

Für diese Fälle kann man in `schulplots` Funktionen definieren und später an
unterschiedlichen Stellen wieder verwenden.

Funktionen werden im Abschnitt `functions` definiert, der sich im Abschnitt
`axes` befindet. Grundsätzlich können beliebig viele Funktionen definiert
werden.

### Beispiel 1: Graph und Fläche unter dem Graphen

<img src="../images/functions1.png" alt="Sinuskurve" width="500"/>


``` yaml linenums="1" hl_lines="12 13 28 20 16"
--8<-- "docs/input/functions1.yaml"
```


### Beispiel 2: Pfeil zeigt auf Graph
Hier zeigen wir, wie man einen Pfeil auf einen Punkt auf dem Funktionsgraphen zeigen lassen kann:

<img src="../images/functions2.png" alt="Sinuskurve" width="500"/>


``` yaml linenums="1" hl_lines="12-13 16 20 27 34"
--8<-- "docs/input/functions2.yaml"
```
