
# Achsensysteme: `axes`

Achsensysteme werden innerhalb von `axes_descriptors` angelegt. Dieses Feld ist
eine *Liste*, was an der Verwendung von Spiegelstrichen (`-`) erkennbar ist;
alternativ kann eine Liste auch mit `[...]` angegeben werden, was wir aber nur
für leere Listen empfehlen.

Jeder Listeneintrag hat mindestens drei weitere Einträge:
1. `axes`: eine Beschreibung des Achsensystems (s.u.)
2. `bottom`: Abstand der Achsen zum unteren Rand
3. `left`:  Abstand der Achsen zum linken Rand

Weitere mögliche Einträge sind `graphs` (für Funktionsgraphen), `areas` (für
ausgefüllte Flächen), `vlines` (für vertikale Linien), `vspans` (für farblich
ausgefüllte Bereiche zwischen vertikalen Linien). Diese werden in späteren
Kapiteln behandelt.

## Attribute der `axes` Struktur
Die `axes` Struktur besitzt folgende Attribute:

| Attribut | Beschreibung | Default |
| -- | -- | -- |
| `x_min` | Kleinster x-Wert (*) |  |
| `y_min` | kleinster y-Wert (*)|  |
| `width` | Breite der Achsen | 10cm |
| `height` | Höhe der Achsen | 8cm |
| `unit` | Längeneinheit | 1cm |
| `x_label` | Bezeichner der x-Achse | x |
| `y_label` | Bezeichner der y-Achse | y |
| `x_label_offset` | Verschiebung des x-Achsen-Bezeichners | x: 0cm, y: 0.5cm |
| `y_label_offset` | Verschiebung des y-Achsen-Bezeichners | x: 0.5cm, y: 0cm |
| `x_tick_distance` | Abstand der x-Achsenmarkierung | 1 |
| `y_tick_distance` | Abstand der y-Achsenmarkierung | 1 |
| `show_x_tick_labels` | Sollen die Zahlen unter der x-Achse angezeigt werden? | true |
| `show_y_tick_labels` | Sollen die Zahlen neben der y-Achse angezeigt werden? | true |
| `show_legend` | Soll die legende angezeigt werden? | true |
| `legend_options` | Weitere Optionen [(Other Parameters)](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend) für die Darstellung der Legende (**)| *keine* |
| `n_points` | Anzahl der Datenpunkte für die Darstellung von Graphen | 3000 |

(*) Der größte x-Wert kann durch folgende Formel berechnet werden:
`x_max = x_min + width / unit`. Entsprechend für den größten y-Wert.

(**) Eine interessante Option für die Legende ist `loc`. Wenn man diese Option beispielsweise auf `upper left` festlegt, kann man die automatische Platzierung der Legende abschalten und sie links oben platzieren. Siehe Beispiel 4 bei den [Graphen](graph.md#beispiel-4)

## Ein Achsensystem

#### Beispiel 1  
<img src="../images/axes1.png" alt="Sinuskurve" width="500"/>


```yaml
--8<-- "docs/input/axes1.yaml"
```

## Zwei Achsensysteme in einer Zeichnung
#### Beispiel 2
Zwei Achsensysteme mit unterschiedlichen Einheiten in der selben Abbildung.
<img src="../images/axes2.png" alt="Sinuskurve" width="600"/>

```yaml
--8<-- "docs/input/axes2.yaml"
```
Beachte, dass im linken Achsensystem die Legende ausgeschaltet wurde
(`show_legend: false`), wodurch das kleine, leere Quadrat verschwindet. Dieses ist die "leere" Legende.