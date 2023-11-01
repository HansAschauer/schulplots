# Linien
## Einfache vertikale Linien
Vertikalie Linien werden im Abschnitt `vlines` in der Struktur
`axes_descriptors` angelegt.

Attribute der `vline` Struktur:

| Attribut | Beschreibung | Default |
| -- | -- | -- |
| `x` |  x-Position der vertikalen Gerade  |   |
| `x_var`  | variable, in der die x-Position der vertikalen Gerade abgelegt wurde. Überschreibt den angegeben Wert von `x`. |
| `y_min` | Höhe in der die Line startet. Eine Zahl zwischen 0 (unten) und 1(oben)   | 0  |
| `y_max` | Höhe in der die Line endet. Eine Zahl zwischen 0 (unten) und 1(oben)   |  1 |
| `plot_args` | Einstellungen zur Darstellung des Graphen |  |


#### Beispiel 1: Vertikale Linien
<img src="../images/line1.png" alt="Sinuskurve" width="500"/>

```yaml
figure:
  height: 8cm
  width: 10cm
axes_descriptors:
- axes:
    height: 6cm
    width: 8cm
    x_min: -3
    y_min: -2
  bottom: 1cm
  left: 1cm
  vlines:
  - x: -1
  - x: 1
    plot_args:
      color: green
      alpha: 0.4
      linestyle: --
  - x: 2
    plot_args:
      color: darkblue
      alpha: 0.4
      linestyle: 
      linewidth: 3
```



## Farblich hervorgehobene Abschnitte
<img src="../images/line3.png" alt="Sinuskurve" width="500"/>

```yaml
figure:
  height: 8cm
  width: 10cm
axes_descriptors:
- axes:
    height: 6cm
    width: 8cm
    x_min: -3
    y_min: -2
  bottom: 1cm
  left: 1cm
  vspans:
  - x0: -1
    x1: 1
```

## Verwendung von Variablen
<img src="../images/line2.png" alt="Sinuskurve" width="500"/>

```yaml
figure:
  height: 8cm
  width: 10cm
axes_descriptors:
- axes:
    height: 6cm
    width: 8cm
    x_min: -3
    y_min: -2
  bottom: 1cm
  left: 1cm
  graphs:
  - function: 3*sin(x)
    plot_args:
      alpha: 0.1
      color: black
  - function: 1 + 0*x
    plot_args:
      alpha: 0.1
      color: black
  areas:
  - function:
    - 3*sin(x)
    - 1 + 0*x
    plot_args:
      alpha: 0 # do not show, only for calculating the intersections
  vspans:
  - x0: sect_x_0
    x1: sect_x_1
```