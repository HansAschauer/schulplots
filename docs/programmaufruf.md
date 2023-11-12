# Programmaufruf von `schulplots`


`schulplots` ist ein Programm, das auf der Kommandozeile gestartet wird; bei
einem Aufruf wird eine Abbildung, deren Beschreibung in einem Text-Dokument
abgelegt wurde, in eine Abbildung umgewandelt.

Der einfachste Aufruf von `schulplots` benötigt nur den Dateinamen der Beschreibungsdatei; es wird dann die Abbildung in einem Fenster angezeigt.

Gibt man die Option `-o <dateiname>` an, so wird das Bild direkt in der Datei `<dateiname`> abgespeichert. Folgende Formate sind möglich, und werden durch die Erweiterung des angegebenen Dateinamens ausgewählt:

- png
- pdf
- svg

Mit der Option `-h` wird eine kurze Hilfe angezeigt:

```
> schulplots --help
usage: schulplots.py [-h] [--output OUTPUT] [--show] filename

Create function plots styled similar to the conventions used in German schools. For documentation, see
https://schulplots.ch23.de

positional arguments:
  filename              Description of the figure, in YAML format

options:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Name out output file. If not provided (and --show is not given), store the figure in the
                        current working directory.
  --show, -s            Show plot in interactive window. May not be used with --output.
```