
# schulplots - ein Tool zum Erzeugen von 2D-Plots im schul-üblichen Stil

`schulplots` ermöglicht es, 2D-Graphen von Funktionen zu erzeugen, die so aussehen, wie Schüler es kennen.

Die Abbildung wird hierbei mit einer Beschreibungs-Datei beschrieben, die von `schulplots`in eine Abbildung umgewandelt wird.

## Beispiel
<img src="images/plot_sinus.png" alt="Sinuskurve" width="500"/>

Dieses Bild wird durch die folgende Beschreibung im YAML-Format erzeugt:

```yaml
--8<-- "docs/input/plot_sinus.yaml"
```
Die Beschreibungsdatei hat Haupt-Sektionen:
1. `figure`: Diese Sektion enthält Informationen über die gesamte Abbildung. Im Beispiel werden die Höhe und die Breite der Abbildung angegeben.
2. `axes_descriptors`: Diese Sektion enthält eine Beschreibung von Axen-Systemen und Graphen/Flächen, die in diese Achsensysteme  eingezeichnet werden sollen.

Es ist auch möglich, mehrere Achsensysteme mit mehreren Graphen in eine Abbildung zu zeichnen:

<img src="images/plot_sinus2.png" alt="Sinuskurve" width="500"/>
