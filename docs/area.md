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
`==` (gleich), `!=` (ungleich) zur Verfügung. Einzelne Vergleiche können mit
`and` (und), `or` (oder) sowie mit `xor` (exklusiv oder) verknüpft werden.    



Beispiele für `condition`:

* `x > 0`: x > 0
* `(x<2) | (x>3)`: x < 2 or x >  3
* `y>0`: alles rechts von der y-Achse
* `y<x`: alle Punkte unterhalb der Geraden y=x

#### Beispiel 1:
Im linken Achsensystem wurde keine Bedingung angegeben -- es wird deshalb die gesamte von den beiden Funktionsgraphen eingeschlossene Fläche gezeichnet. Rechts wurde als Bedingung `y1 >= y2` angegeben, y1 >= y2so dass nur der Teil der Fläche dargestellt wird, in der die blaue Kurve oberhalb der orangenen liegt.

<img src="../images/area1.png" alt="Sinuskurve" width="600"/>

```yaml
--8<-- "docs/input/area1.yaml"
```
Dieses Beispiel lässt sich auch kürzer schreiben, unter Verwendung von YAML
Anchors. Das sind symbolische Namen, die an einer Stelle definiert werden
(`&my_axes`), und später wiederverwendet werden (`<<: *my_axes`). Dabei können
Attribute selektiv erneut angegeben werden, wodurch diese mit den neuen Werten
überschrieben werden. Beachte, dass dies keine Besonderheit von `schulplots`
ist, sondern eine Eigenschaft der YAML Sprache.

```yaml
--8<-- "docs/input/area_template.yaml"
```