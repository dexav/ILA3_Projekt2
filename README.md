# Projekt-Dokumentation

Gruppe: Filip Mitrovic und Xavier Nursiwat

**Um die Webseite auszuführen muss man folgendes im terminal VSC eingeben: python app.py**

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
| 8.11.2024       | 0.0.1   | Wir haben den Projektantrag erstellt, Github Repository erstellt, Projektdokumentation begonnen, und Visual studio code eingerichtet.  Filip Mitrovic hat bereits 3 Tests abgeschlossen und wir haben an der Planung weitergearbeitet. Wir haben uns über die Basics von Cyber Security informiert und Filip mitrovic hat mit seinem Online Kurs begonnen. |                                                             
| 15.11.2024      | 0.0.2  |Wir haben mit der Implementierung angefangen. |
| 22.11.2024     | 0.0.3   | Wir haben an der Implementierung wetier gearbeitet.           |
| 29.11.2024      | 0.0.4  | Wir haben an der Implementierung wetier gearbeitet.       |
|  06.12.2024       | 0.0.5   |  Wir haben an der Implementierung wetier gearbeitet. Dazu haben wir uns entschieden zum Programm eine Webseite zu bauen. Wir haben auch noch getestet.                                |
| 13.12.2024       | 1.0.0  | Webseite Fertiggestellt und ist funktionstüchtig|
| 20.12.2024       | 1.0.1  | Endspurt mit der Dokumentation                          |


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
| 12   | Muss            | Funktional   | Als Entwickler möchte ich ein Skript zum  Versenden von Phishing-Mails an eine Testperson implementieren, damit ich das Tool in einer realistischen Umgebung testen kann. |
| 13   | Soll            | Qualität     | Als Entwickler möchte ich sicherstellen, dass die Phishing-Mail realistisch aussieht, aber keine echten Personen gefährdet, damit die Tests sicher durchgeführt werden können. |




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



### 1.4 Diagramme
![MachineLearningPAP](https://github.com/user-attachments/assets/1b61e2f1-1f1e-4fd5-89ac-0a93717e6c77)


## 2 Planen

| AP-№  | Frist     | Zuständig        | Beschreibung                                                 | geplante Zeit |
|-------|-----------|------------------|-------------------------------------------------------------|---------------|
| 1.A |15.11.2024    | Filip            | Implementierung der URL-Eingabe                              | 45 min        |
| 1.B |15.11.2024    | Xavier           | Rückmeldung basierend auf URL-Analyse                        | 45 min        |
| 2.A |22.11.2024    | Filip            | Training des Modells mit Phishing- und sicheren URLs         | 45 min        |
| 3.A |22.11.2024   | Xavier           | Integration eines Skripts für regelmäßiges Training          | 45 min        |
| 4.A | 22.11.2024   | Beide            | Merkmalsextraktion von URLs implementieren                   | 90 min        |
| 5.A |29.11.2024   | Filip            | Warnmeldung für verdächtige URLs                             | 45 min        |
| 6.A |29.11.2024    | Xavier           | Speichern und Laden des Modells                              | 45 min        |
| 7.A |29.11.2024    | Filip            | Erstellen eines Programms zur Phishing-Mail-Generierung      | 45 min        |
| 8.A |29.11.2024   | Xavier           | Skript zum Senden von Phishing-Mails         | 70 min        |
| 9.A |06.12.2024   | Beide            | Sicherstellen der Sicherheit und Testen der Phishing-Mail    | 45 min        |
| 10.A|06.12.2024   | Beide            | Simple Webseite erstellen für das Phishinglinks erkennen | 90 min        |
| 11.A|13.12.2024   | Beide            | Webseite mit dem Python Prgramm verbinden.    | 45 min        |

**Total geplante Zeit:** 540 Minuten (ca. 9 Stunden)



## 3 Entscheiden
Wir haben uns entschieden zu unserem Python Programm eine Webseite zu erstellen, damit es einfacher ist zu bedienen.

## 4 Realisieren

| AP-№  | Datum  | Zuständig | geplante Zeit | tatsächliche Zeit |
|-------|--------|-----------|---------------|-------------------|
| 1.A   |15.11.2024        | Filip     | 45 min        | 50 min                  |
| 1.B   |   15.11.2024     | Xavier    | 45 min        |   45 min                |
| 2.A   | 22.11.2024      | Filip     | 45 min        |  45 min                 |
| 3.A   |22.11.2024        | Xavier    | 45 min        |  45 min                 |
| 4.A   |22.11.2024        | Beide     | 90 min        |  100 min                 |
| 5.A   |29.11.2024         | Filip     | 45 min        |   45 min                |
| 6.A   |29.11.2024         | Xavier    | 45 min        |  45 min                 |
| 7.A  | 29.11.2024        | Filip     | 45 min        |     50 min              |
| 8.A  | 29.11.2024        | Xavier    | 70 min        |    90 min                  |
| 9.A  |06.12.2024          | Beide     | 45 min        |   50 min                   |
| 10.A  | 06.12.2024         | Beide     | 90 min        |   90 min                   |
| 11.A  |13.12.2024        | Beide     | 45 min        |   50 min                   |




## 5 Kontrollieren



| TC-№  | Datum       | Resultat                | Tester  |
|-------|-------------|-------------------------|---------|
| 1.1   | 2024.12.06  | Erfolgreich: Rückmeldung korrekt ("Sicher") | Xavier  |
| 2.1   | 2024.12.06  | Erfolgreich: Rückmeldung korrekt ("Verdächtig") | Filip   |
| 3.1   | 2024.12.06  | Erfolgreich: Neue Muster wurden erkannt | Xavier  |
| 4.1   | 2024.12.06  | Erfolgreich: Genauigkeit verbessert | Filip   |
| 5.1   | 2024.12.06  | Erfolgreich: Liste der letzten 5 URLs korrekt angezeigt | Xavier  |
| 6.1   | 2024.12.06  | Erfolgreich: Ungewöhnliche Merkmale korrekt erkannt | Filip   |
| 7.1   | 2024.12.06  | Erfolgreich: Rückmeldung innerhalb von 1 Sekunde | Xavier  |
| 8.1   | 2024.12.06  | Erfolgreich: Warnmeldung korrekt ausgegeben | Filip   |
| 9.1   | 2024.12.06  | Erfolgreich: Modell wurde korrekt geladen | Xavier  |
| 11.1  | 2024.12.06  | Erfolgreich: Phishing-Mail realistischer Inhalt | Filip   |
| 12.1  | 2024.12.06  | Erfolgreich: Mail an Testperson gesendet | Xavier  |
| 13.1  | 2024.12.06  | Erfolgreich: Keine persönlichen Informationen enthalten | Filip   |

### Fazit:
Alle Testfälle wurden erfolgreich ausgeführt, und das Tool hat in jeder getesteten Situation wie erwartet funktioniert. Die Testergebnisse zeigen, dass das System stabil ist und sowohl URLs zuverlässig analysiert als auch Phishing-Mails korrekt generiert. Besonders hervorzuheben sind die schnelle Verarbeitung der URLs und die Genauigkeit des Modells. Weitere Tests könnten sich darauf konzentrieren, wie das Tool mit einer größeren Anzahl an Daten umgeht und ob es unter Last stabil bleibt.

## 6 Auswerten 
Mahara Portfolio
