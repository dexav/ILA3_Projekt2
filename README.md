# Projekt-Dokumentation

Gruppe: Filip Mitrovic und Xavier Nursiwat

um projekt auszuführen muss man folgendes im terminal VSC eingeben: python app.py

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
|       | 0.0.1   | Wir haben den Projektantrag erstellt, Github Repository erstellt, Projektdokumentation begonnen, und Visual studio code eingerichtet                                                             |
|       | ...     |                                                              |
|       | 1.0.0   |                                                              |

## 1 Informieren

### 1.1 Ihr Projekt

Physhing Link Erkennungs Programm

In diesem Projekt entwickeln wir ein Tool, das Nutzer vor potenziellen Phishing-Links schützt, indem es verdächtige URLs automatisch erkennt. Dazu trainieren wir ein Machine-Learning-Modell mit Daten sicherer und unsicherer Links, sodass das Modell typische Phishing-Muster lernt. Nutzer können eine URL eingeben und erhalten eine schnelle Rückmeldung, ob diese sicher oder verdächtig ist. Das Tool analysiert die URL anhand von Merkmalen wie speziellen Zeichen und bestimmten Schlüsselwörtern. Durch regelmässiges Training bleibt das Modell aktuell und anpassungsfähig, sodass es effektiv auf neue Phishing-Bedrohungen reagieren kann.
Zudem programmieren ein Programm, welches eine Phishing-Mail generiert und später mir einem Skript per Email an eine Person gesendet wird. 

**🚨 WARNUNG:** Diese Mail wird nur mir oder an Xavier Nursiwat versendet, da wir es als Übung benutzen und niemanden in Gefahr bringen möchten. 🚨

Wir arbeiten in Visual studio code mit der Programmiersprache Python.

### 1.2 User Stories



| US-№ | Verbindlichkeit | Typ          | Beschreibung                                                 |
| ---- | --------------- | ------------ | ------------------------------------------------------------ |
| 1    | Muss            | Funktional   | Als Benutzer möchte ich eine URL eingeben, damit ich überprüfen kann, ob sie sicher oder verdächtig ist. |
| 2    | Muss            | Funktional   | Als Benutzer möchte ich eine klare Rückmeldung zur URL-Sicherheit erhalten, damit ich informiert entscheiden kann, ob ich den Link öffnen soll. |
| 3    | Soll            | Funktional   | Als Entwickler möchte ich, dass das Modell typische Phishing-Muster erkennt, damit die Analyse präzise und zuverlässig ist. |
| 4    | Soll            | Funktional   | Als Entwickler möchte ich das Modell regelmäßig mit neuen URLs trainieren können, damit es an aktuelle Phishing-Techniken angepasst bleibt. |
| 5    | Kann            | Funktional   | Als Benutzer möchte ich eine Liste der überprüften URLs sehen, damit ich meine bisherigen Überprüfungen in der Konsole nachvollziehen kann. |
| 6    | Muss            | Qualität     | Als Entwickler möchte ich eine Merkmalsextraktion für die URL umsetzen, damit das Modell die URL korrekt analysieren kann. |
| 7    | Soll            | Funktional   | Als Benutzer möchte ich schnell und einfach eine Rückmeldung zur URL-Sicherheit erhalten, damit ich die URL direkt in der Konsole auswerten kann. |
| 8    | Kann            | Funktional   | Als Benutzer möchte ich eine Warnmeldung in der Konsole erhalten, wenn eine verdächtige URL erkannt wird, damit ich sofort alarmiert bin. |
| 9    | Soll            | Qualität     | Als Entwickler möchte ich eine Schnittstelle zum Speichern und Laden des Modells, damit es ohne erneutes Training direkt nutzbar ist. |
| 10   | Kann            | Funktional   | Als Benutzer möchte ich, dass das Tool später eventuell als Google Pop-up verfügbar ist, um die Nutzung zu erweitern. |
| 11   | Muss            | Funktional   | Als Entwickler möchte ich ein Programm zur Generierung einer Phishing-Mail erstellen, damit ich die Sicherheit des Tools realistisch testen kann. |
| 12   | Muss            | Funktional   | Als Entwickler möchte ich ein Skript zum automatisierten Versenden von Phishing-Mails an eine Testperson implementieren, damit ich das Tool in einer realistischen Umgebung testen kann. |
| 13   | Soll            | Qualität     | Als Entwickler möchte ich sicherstellen, dass die Phishing-Mail realistisch aussieht, aber keine echten Personen gefährdet, damit die Tests sicher durchgeführt werden können. |




✍️ Jede User Story hat eine ganzzahlige Nummer (1, 2, 3 etc.), eine Verbindlichkeit (Muss oder Kann?), und einen Typ (Funktional, Qualität, Rand). Die User Story selber hat folgende Form: *Als ein 🤷‍♂️ möchte ich 🤷‍♂️, damit 🤷‍♂️*.

### 1.3 Testfälle

| TC-№  | Ausgangslage                                       | Eingabe                                 | Erwartete Ausgabe                                                   |
|-------|----------------------------------------------------|-----------------------------------------|----------------------------------------------------------------------|
| 1.1   | Benutzer startet das Tool                         | URL: `http://example.com`               | Rückmeldung: "Sicher" oder "Verdächtig"                             |
| 2.1   | URL wurde eingegeben                              | URL: `http://phishing-abc.com`          | Rückmeldung: "Verdächtig"                                           |
| 3.1   | Modell wurde initial trainiert                    | Neue URL-Datenbank                      | Erkennung neuer Phishing-Muster in Tests                            |
| 4.1   | Training wird regelmäßig ausgeführt               | Neue Daten zum Training hinzugefügt     | Verbesserte Genauigkeit der URL-Einschätzung                       |
| 5.1   | Mehrere URLs wurden überprüft                     | Keine neue Eingabe                      | Ausgabe: Liste der letzten 5 überprüften URLs mit Status            |
| 6.1   | Eine verdächtige URL wird analysiert              | URL: `http://ph1shing.xyz?data=abc`     | Merkmale wie ungewöhnliche Zeichen oder Subdomains werden erkannt   |
| 7.1   | URL wird überprüft                                | URL: `http://safe.com`                  | Schnelle Rückmeldung innerhalb von 1 Sekunde                       |
| 8.1   | Verdächtige URL eingegeben                        | URL: `http://fraudulent-site.com`       | Warnmeldung in Konsole: "ACHTUNG: URL könnte Phishing sein!"        |
| 9.1   | Modell ist gespeichert                            | Befehl: `python app.py`                 | Modell wird geladen, ohne dass ein erneutes Training notwendig ist |
| 11.1  | Programm generiert Phishing-Mail                 | Beispieltext für Phishing-Mail          | Mail enthält realistisch wirkenden Inhalt                          |
| 12.1  | Testperson ist definiert                          | E-Mail-Adresse: `testperson@example.com`| Mail wird an Testperson gesendet                                   |
| 13.1  | Phishing-Mail wurde generiert                    | Überprüfung des Inhalts                 | Mail enthält keine persönlichen Informationen oder Risiken          |

✍️ Die Nummer hat das Format `N.m`, wobei `N` die Nummer der User Story ist, die der Testfall abdeckt, und `m` von `1` an nach oben gezählt. Beispiel: Der dritte Testfall, der die zweite User Story abdeckt, hat also die Nummer `2.3`.

### 1.4 Diagramme
![MachineLearningPAP](https://github.com/user-attachments/assets/1b61e2f1-1f1e-4fd5-89ac-0a93717e6c77)


## 2 Planen

| AP-№  | Frist     | Zuständig        | Beschreibung                                                 | geplante Zeit |
|-------|-----------|------------------|-------------------------------------------------------------|---------------|
| 1.A   |    | Filip            | Implementierung der URL-Eingabe                              | 45 min        |
| 1.B   |    | Xavier           | Rückmeldung basierend auf URL-Analyse                        | 45 min        |
| 3.A   |    | Filip            | Training des Modells mit Phishing- und sicheren URLs         | 45 min        |
| 4.A   |   | Xavier           | Integration eines Skripts für regelmäßiges Training          | 45 min        |
| 6.A   || Beide            | Merkmalsextraktion von URLs implementieren                   | 90 min        |
| 8.A   |   | Filip            | Warnmeldung für verdächtige URLs                             | 45 min        |
| 9.A   |    | Xavier           | Speichern und Laden des Modells                              | 45 min        |
| 11.A  |    | Filip            | Erstellen eines Programms zur Phishing-Mail-Generierung      | 45 min        |
| 12.A  |   | Xavier           | Skript zum automatisierten Senden von Phishing-Mails         | 45 min        |
| 13.A  |   | Beide            | Sicherstellen der Sicherheit und Testen der Phishing-Mail    | 45 min        |

**Total geplante Zeit:** 540 Minuten (ca. 9 Stunden)

✍️ Die Nummer hat das Format `N.m`, wobei `N` die Nummer der User Story ist, auf die sich das Arbeitspaket bezieht, und `m` von `A` an nach oben buchstabiert. Beispiel: Das dritte Arbeitspaket, das die zweite User Story betrifft, hat also die Nummer `2.C`.

✍️ Ein Arbeitspaket sollte etwa 45' für eine Person in Anspruch nehmen. Die totale Anzahl Arbeitspakete sollte etwa Folgendem entsprechen: `Anzahl R-Sitzungen` ╳ `Anzahl Gruppenmitglieder` ╳ `4`. Wenn Sie also zu dritt an einem Projekt arbeiten, für welches zwei R-Sitzungen geplant sind, sollten Sie auf `2` ╳ `3` ╳`4` = `24` Arbeitspakete kommen. Sollten Sie merken, dass Sie hier nicht genügend Arbeitspakte haben, denken Sie sich weitere "Kann"-User Stories für Kapitel 1.2 aus.

## 3 Entscheiden

✍️ Dokumentieren Sie hier Ihre Entscheidungen und Annahmen, die Sie im Bezug auf Ihre User Stories und die Implementierung getroffen haben.

## 4 Realisieren

| AP-№ | Datum | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ----- | --------- | ------------- | ----------------- |
| 1.A  |       |           |               |                   |
| ...  |       |           |               |                   |

✍️ Tragen Sie jedes Mal, wenn Sie ein Arbeitspaket abschließen, hier ein, wie lang Sie effektiv dafür hatten.

## 5 Kontrollieren

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  |       |          |        |
| ...  |       |          |        |

✍️ Vergessen Sie nicht, ein Fazit hinzuzufügen, welches das Test-Ergebnis einordnet.

## 6 Auswerten

✍️ Fügen Sie hier eine Verknüpfung zu Ihrem Lern-Bericht ein.
