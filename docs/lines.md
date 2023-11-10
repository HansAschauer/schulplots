# Linien und Pfeile

## Übersicht

| type | Beschreibung |
| ---- | ---|
| `VLine` | vertikale Linie |
| `HLine` | horizontale Linie |
| `VSpan` | farblich hervorgehobener Bereich zwischen zwei x-Werten |
| `HSpan` | farblich hervorgehobener Bereich zwischen zwei y-Werten |
| `Arrow` | Pfeil | 

## Einfache  Linien

####Vertikale Linien 

Attribute der `vline` Struktur:

| Attribut | Beschreibung | Default |
| -- | -- | -- |
| `x` |  x-Position der vertikalen Gerade  |   |
| `y_min` | Höhe in der die Line startet. Eine Zahl zwischen 0 (unten) und 1(oben)   | 0  |
| `y_max` | Höhe in der die Line endet. Eine Zahl zwischen 0 (unten) und 1(oben)   |  1 |
| `plot_args` | Einstellungen zur Darstellung des Graphen |  |

#### Horizontale Linien 

Attribute der `hline` Struktur:

| Attribut | Beschreibung | Default |
| -- | -- | -- |
| `y` |  x-Position der vertikalen Gerade  |   |
| `x_min` | x-Position, an der die Line startet. Eine Zahl zwischen 0 (unten) und 1(oben)   | 0  |
| `y_max` | x-Position, an der die Line endet. Eine Zahl zwischen 0 (unten) und 1(oben)   |  1 |
| `plot_args` | Einstellungen zur Darstellung des Graphen |  |


#### Beispiel 1: Vertikale Linien
<img src="../images/line1.png" alt="Sinuskurve" width="500"/>

```yaml
--8<-- "docs/input/line1.yaml"
```



## Farblich hervorgehobene Abschnitte
<img src="../images/line3.png" alt="Sinuskurve" width="500"/>

```yaml
--8<-- "docs/input/line3.yaml"
```

## Verwendung von Variablen
<img src="../images/line2.png" alt="Sinuskurve" width="500"/>

```yaml
--8<-- "docs/input/line2.yaml"
```