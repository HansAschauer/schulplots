# Text


## Attribute der `Text` Struktur


| Attribut | Beschreibung | Default |
| -- | -- | -- |
| `x` |  x-Koordinate des Punkts  |   |
| `y` |  y-Koordinate des Punkts  |   |
| `text` | anzuzeigender Text   |   |
| `rotation` | Rotations-Winkel des Texts | 0 |
| `text_args` | Einstellungen zur Darstellung des Texts |  |

Die angegebenen Koordinaten beziehen sich standardmäßig auf die linke untere Ecke des Textfeldes. Beispiel 3 zeigt, wie das geändert werden kann.


Für die `text_args` siehe die [Dokumentation von Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html). 

#### Beispiel 1: Texte in verschiedenen Stilen
<img src="../images/text1.png" alt="Punkte" width="500"/>

```yaml
--8<-- "docs/input/text1.yaml"
```

#### Beispiel 2: Text mit mehreren Zeilen
Texte können sich über mehrere Zeilen erstrecken. Dazu wird in der YAML-Datei
eine spzeielle Syntax verwendet, die [hier](https://yaml-multiline.info/)
beschrieben wird.


<img src="../images/text2.png" alt="Punkte" width="500"/>

```yaml
--8<-- "docs/input/text2.yaml"
```

#### Beispiel 3: Bezugspunkte des Texts im Koordinatensystem

Textkoordinaten beziehen sich standardmäßig auf die linke untere Ecke des
Textfeldes (genauer: auf die linke Baseline). Manchmal ist das nicht gewünscht,
und es lassen sich andere Bezugspunkte einstellen. Eine Beschreibung der
Bezugspunkte ist
(hier)[https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html]
zu finden.

In Schulplots lässt sich der Bezugspunkt mit Hilfe der Angabe von `ha` (oder `horizontalalignment`) und `va` (oder `verticalalignment`) in den `text_args` einstellen. Die möglichen Werte für `ha` sind `baseline` (Default), `top`, `bottom`, `center` und `center_baseline`. Für `ha` sind die Werte `left` (Default), `right` und `center` möglich.

Beachte, dass bei Texten ohne Unterlängen (d.h., wenn keine Buchstaben wie p,q,g vorkommen), `bottom` und `baseline` zusammenfallen.

Bei mehrzeiligem Text bestimmen `ha` und `va` den Bezugspunkt für das gesamte Rechteck, das den Text umgibt. Die horizontale Ausrichtung der einzelnen Zeilen lässt sich mit `ma` (oder `multialignment`) einstellen (siehe Beispiel 2).

<img src="../images/text3.png" alt="Punkte" width="500"/>

```yaml
--8<-- "docs/input/text3.yaml"
```

#### Beispiel 4: Rotation des Textes

Bei der Rotation des Textes spielt die Reihenfolge des Alignements bzgl. des Bezugspunktes und der Rotation eine Rolle. Dies lässt sich mit `rotation_mode` einstellen:

<img src="../images/text4.png" alt="Punkte" width="500"/>

```yaml
--8<-- "docs/input/text4.yaml"
```



