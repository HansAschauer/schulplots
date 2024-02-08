# Tutorial: die erste Abbildung

Das Ziel dieses Tutorial ist es, folgendes Bild zu erzeugen:


<img src="../images/plot_gebrochen_rational.png" alt="Sinuskurve" width="900"/>

Dargestellt wird die Funktion

$$
f(x) \frac{x^3-2x^2-11x+12}{4x²+4x-48} = \frac{(x-4)(x-1)(x+3)}{4(x-3)(x+4)}
$$

mit sämtlichen Asymptoten, sowie eine Legende und erklärender Text.

## Das Zeichenblatt

Wir erstellen ein Zeichenblatt, das 22 cm breit und 16 cm hoch ist. Ohne weitere Angaben besitzt das Zeichenblatt ein 5 mm - Karo.

Dazu benötigen wir einen Texteditor, wie z.B.

- Notepad++ (Windows)
- kate (Linux mit KDE)
- gedit (Linux mit Gnome)
- Graviton (MAC)

Mit diesem Texteditor erstellen wir eine neue Datei und den folgenden Text:

```yaml
--8<-- "docs/input/tutorial1.yaml"
```

Diese Datei speichern wir als `tutorial.yaml` in einem geeigneten Verzeichnis ab. 

Als nächstes öffnen wir ein Terminal-Fenster (`cmd.exe` unter Windows, `konsole` unter Linux) und wechsel in dieses Verzeichnis (`cd <Verzeichnis>`). 

Danach können wir den Befehl `schulplots tutorial.yaml` in das Terminal-Fenster tippen und mit der Enter-Taste ausführen. Das erzeugt unsere Abbildung in einer neue Datei `tutorial.png` im aktuellen Verzeichnis:


<img src="../images/tutorial1.png" alt="Sinuskurve" width="900"/>

In jedem Schritt des Tutorial werden wir die Datei erweitern. Nach dem Abspeichern muss jeweils wieder das Kommando `schulplots tutorial.yaml` aufgerufen werden.

## Das Achsensystem

Jetzt kommt das Koordinatensystem; es soll 20 cm breit sein und 14 cm hoch (Zeile 6-7). Der Abstand zum unteren und zum linken Rand soll jeweils 1 cm betragen (Zeile 10-11). 

Der kleinste angezeigte x-Wert ist x=-10, und der kleinste angezeigte y-Wert ist y=-7 (Zeile 8-9). Die angaben sind in Längeneinheiten, die standardmäßig 1 cm lang sind.


```yaml  linenums="1" hl_lines="5-11"
--8<-- "docs/input/tutorial2.yaml"
```
<img src="../images/tutorial2.png" alt="Sinuskurve" width="900"/>

## Die erste Funktion

Alle weiteren sichtbaren Elemente in einem Achsensystem werden im Abschnitt `items` eingefügt (Zeile 12). Jeder Eintrage beginnt mit einem Spiegelstrich, und der Angabe des Typs des Elements, das eingefügt werden soll. Der Typ `Graph` steht für einen Funktionsgraph.

Die Funktion wird in Zeile 14 angegeben.


```yaml linenums="1" hl_lines="13-14"
--8<-- "docs/input/tutorial3.yaml"
```
<img src="../images/tutorial3.png" alt="Sinuskurve" width="900"/>

## Senkrechte Asymptoten

Die senkrechten Asymptoten sind vertikale Geraden. Diese können mit dem Typ `VLine` unter `items` unter Angabe des x-Werts eingefügt werden (Z. 15-18.)


```yaml linenums="1" hl_lines="15-18"
--8<-- "docs/input/tutorial4.yaml"
```
<img src="../images/tutorial4.png" alt="Sinuskurve" width="900"/>

## Die schräge Asymptote

Die schräge Asymptote hat die Funktionsgleichung $g(x) = \frac{1}{4}x- \frac{1}{2}$. Wir fügen ein sie unter `items` ein, indem wir wieder den Typ `Graph` wählen, und den Funktionsterm angeben.


```yaml linenums="1" hl_lines="15-16"
--8<-- "docs/input/tutorial5.yaml"
```
<img src="../images/tutorial5.png" alt="Sinuskurve" width="900"/>

## Eigenschaften der Linien

Asymptoten sollen gestrichelt gezeichnet werden. Das kann man bei den Typen `Graph` und `VLine` im Abschnitt `plot_args` angeben. `ls` ist eine Abkürzung für `linestyle`, und die Angabe von `--` erzeugt eine gestrichelte Linie. Der bei `alpha` angegebene Wert von 0.5 verringert die Deckkraft der Farben auf 50%.


```yaml linenums="1" hl_lines="17-19 22-24 27-29"
--8<-- "docs/input/tutorial6.yaml"
```
<img src="../images/tutorial6.png" alt="Sinuskurve" width="900"/>

## Legende

Standardmäßig wird eine Legende angezeigt; in den bisherigen Abbildungen war sie zwar sichtbar, aber leer. Wir können sie füllen, indem wir bei den Funktionen ein `label` angeben (Zeile 15 und 18).

Die Legende kann entweder ein beliebiger Text sein (Zeile 18), oder aber in LaTeX formatiert sein, wenn er zwischen `$` Zeichen eingeschlossen ist (Zeile 15).


```yaml linenums="1" hl_lines="15 18"
--8<-- "docs/input/tutorial7.yaml"
```
<img src="../images/tutorial7.png" alt="Sinuskurve" width="900"/>

## Text

Beliebiger Text kann unter `items` mit dem Typ `Text` angegeben werden.

```yaml linenums="1" hl_lines="32-49"
--8<-- "docs/input/tutorial8.yaml"
```
<img src="../images/tutorial8.png" alt="Sinuskurve" width="900"/>

## Letzte Einstellungen


```yaml linenums="1" hl_lines="10-15"
--8<-- "docs/input/tutorial9.yaml"
```
<img src="../images/tutorial9.png" alt="Sinuskurve" width="900"/>


