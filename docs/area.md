# Flächen: `area`

## Attribute der `area` Struktur
Die `area` Struktur besitzt folgende Attribute:

| Attribut | Beschreibung | Default |
| -- | -- | -- |
| `function` | Liste von Funktionstermen, z.B. `[sin(x), cos(x)]` |  |
| `label` | Label der Fläche in der Legende | *leer* |
| `plot_args` | Einstellungen zur Darstellung des Graphen |  |
| `condition` | Bedingung. Siehe Beschreibung unten |  |

Das Attribut `function` ist eine Liste, die zwei Funktionsterme enthält. Hier ein Ausschnitt aus einer Beschreibungsdatei:

```yaml
...
  areas:
  - function:
    - sin(x)
    - 0.25*x**2
    plot_args:
      alpha: 0.3
      color: green
    condition: y1 >= y2
...
```

## Bedingungen (`condition`)
Bedingungen für Flächen funktionieren ähnlich zu Bedingungen bei
[Graphen](graph.md#bedingungen-condition). Der wesentliche Unterschied besteht darin, dass in
Ausdrücken für die Bedingung nun die Variablen `y1` und `y2` verwendet werden.
Diese beziehen sich auf die beiden Funktionen, die im `function` Attribut
festgelegt wurden. 

Genau wie bei Graphen stehen die Vergleichs-Operatoren `<`, `>`, `<=`, `>=`,
`==` (gleich), `!=` (ungleich) zur Verfügung. Einzelne Vergleiche können mit `&`
(und), `|` (oder) sowie mit `^` (exklusiv oder) verknüpft werden. Dabei müssen
die Vergleichs-Operationen in Klammern gesetzt werden.  



Beispiele für `condition`:

* `x > 0`: x > 0
* `(x<2) | (x>3)`: x < 2 or x >  3
* `y>0`: alles rechts von der y-Achse
* `y<x`: alle Punkte unterhalb der Geraden y=x

#### Beispiel 1:
Im linken Achsensystem wurde keine Bedinung angegeben -- es wird deshalb die gesamte von den beiden Funktionsgraphen eingeschlossene Fläche gezeichnet. Rechts wurde als Bedingung `y1 >= y2` angegeben, y1 >= y2so dass nur der Teil der Fläche dargestellt wird, in der die blaue Kurve oberhalb der orangenen liegt.

<img src="../images/area1.png" alt="Sinuskurve" width="600"/>

```yaml
figure:
  height: 8cm
  width: 12cm
axes_descriptors:
- axes: 
    height: 6cm
    width: 4cm
    x_min: -1
    y_min: -2
    show_legend: false
  bottom: 1cm
  left: 1cm
  graphs:
  - function: sin(x)
  - function: 0.25*x**2
  areas:
  - &my_area
    function:
    - sin(x)
    - 0.25*x**2
    plot_args:
      alpha: 0.3
      color: green
- axes: 
    height: 6cm
    width: 4cm
    x_min: -1
    y_min: -2
    show_legend: false
  bottom: 1cm
  left: 7cm
  graphs:
  - function: sin(x)
  - function: 0.25*x**2
  areas:
  - function:
    - sin(x)
    - 0.25*x**2
    plot_args:
      alpha: 0.3
      color: green
    condition: y1 >= y2
```
Dieses Beispiel lässt sich auch kürzer schreiben, unter Verwendung von YAML
Anchors. Das sind symbolische Namen, die an einer Stelle definiert werden
(`&my_axes`), und später wiederverwendet werden (`<<: *my_axes`). Dabei können
Attribute selektiv erneut angegeben werden, wodurch diese mit den neuen Werten
überschrieven werden. Beachte, dass dies keine Besonderheit von `schulplots`
ist, sondern eine Eigenschaft der YAML Sprache.

```yaml
figure:
  height: 8cm
  width: 12cm
axes_descriptors:
- &my_axes
  axes: 
    height: 6cm
    width: 4cm
    x_min: -1
    y_min: -2
    show_legend: false
  bottom: 1cm
  left: 1cm
  graphs:
  - function: sin(x)
  - function: 0.25*x**2
  areas:
  - &my_area
    function:
    - sin(x)
    - 0.25*x**2
    plot_args:
      alpha: 0.3
      color: green
- <<: *my_axes
  left: 7cm
  areas:
  - <<: *my_area
    condition: y1 >= y2
```