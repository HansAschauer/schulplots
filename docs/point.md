# Punkte


## Attribute der `point` Struktur


| Attribut | Beschreibung | Default |
| -- | -- | -- |
| `x` |  x-Koordinate des Punkts  |   |
| `y` |  y-Koordinate des Punkts  |   |
| `label` | Text-Label des Punktes   |   |
| `angle` | Winkel (in Grad) zwischen Punkt und Label; 0 entspricht rechts, 90 entspricht oben etc. | 90 |
| `distance` | Abstand zwischen Punkt und Label. Wird mit Einheit angegeben. | 0.5cm |
| `marker` | Marker-Symbol. Siehe [matplotlib Dokumentation](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html) | x | 
| `plot_args_point` | Einstellungen zur Darstellung des Punktes |  |
| `plot_args_label` | Einstellungen zur Darstellung des Labels |  |

#### Beispiel 1: Punkte in verschiedenen Stilen
<img src="../images/point1.png" alt="Punkte" width="500"/>

```yaml
--8<-- "docs/input/point1.yaml"
```

#### Beispiel 2: Punkte auf einem Graphen
Die Koordinaten können auch mathematische Ausdrücke sein. Insbesondere können auch definierte [Funktionen](function.md) verwendet werden, um Punkte zu zeichnen, die auf einem Graphen liegen:

<img src="../images/point2.png" alt="Punkte" width="500"/>

```yaml
--8<-- "docs/input/point2.yaml"
```
