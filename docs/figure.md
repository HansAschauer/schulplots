# Abbildungen: `figure`

## Leeres Zeichenblatt
Die einfachste Abbildung, die mit `schulplots` erzeugt werden kann, besteht aus
einem leeren, karierten Zeichenbereich.

#### Beispiel 1: Kariertes Zeichenblatt

<img src="../images/figure1.png" alt="Sinuskurve" width="500"/>

Dies wird mit folgener Beschreibung erreicht:
```yaml
figure:
  height: 8cm
  width: 10cm
axes_descriptors: []
```

Die Breite und Höhe des Zeichenbereichs wird mit `width` und `height` angegeben.
Die Längenangaben können mit und ohne Angabe einer Einheit erfolgen; ohne
Einheit wird "inch" als Längeneinheit angenommen. Erlaubte Längeneinheiten sind
`cm`, `mm`, `in`.

Zur generellen Struktur der Beschreibungsdatei siehe [diese
Seite](description_file.md).

Neben `widht`und `height` gibt es noch weitere Attribute der `figure` Umgebung: 


| Attribut | Beschreibung | Default |
| ----------- | ----------- | --|
| `widht`        | Breite der Abbildung |  21.0cm  |
| `height`       | Höhe der Abbildung   |  29.7cm  |
| `grid`         | Größe der Karos      |   0.5cm |  
| `grid_options` | Einstellungen zur Darstellung des Karo |  (1)  |
| `output_file`  | Name der Ausgabedatei. Kann auch an der Kommandozeile gesetzt werden |  *nicht angegeben*  |
| `dpi` | Auflösung des erzeugten Bildes für Raster-Bildformate (z.B. png), in dpi |  300   |

`grid_options` ist ein Mapping von Linien-Eigenschaften auf zugehörige Werte.
Die nützlichsten Eigenschaften sind in der folgenden Tabelle aufgeführt. Eine
vollständige Liste findet sich in der [Dokumentation von
Matplotlib](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.lines.Line2D.html);
von diesen werden in `schulplots` nur diejenigen unterstützt, die als Wert einen
ein `bool`(`true` oder `false`), ein `float` oder `int` (Zahl) oder einen String
erwarten.

*Achtung*: Sofern `grid_options` angegeben werden, werden die Voreinstellungen,
insbesondere für `alpha` und `linewidth`, überschrieben, und müssen ggf.
explizit gesetz werden. 

| Eigenschaft | Beschreibung | Default | 
| --| --| --| 
|`lw` oder `linewidth` | Linienbreite   | 0.5 | 
| `color` | Farbe. Details finden sich in der [Matplotlib Doku](https://matplotlib.org/stable/users/explain/colors/colors.html#sphx-glr-users-explain-colors-colors-py)| schwarz | 
| `alpha` | Durchsichtigkeit, als Wert zwischen 0 und 1  | 0.2 |

## Einstellungen für das Karo
#### Beispiel 2: Karo 7mm, blau

<img src="../images/figure2.png" alt="Sinuskurve" width="500"/>

```yaml
figure:
  height: 8cm
  width: 10cm
  grid: 7mm
  grid_options:
    color: blue
    alpha: 0.2
    linewidth: 0.5
axes_descriptors: []
```
