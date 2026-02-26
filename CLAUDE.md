# CLAUDE.md – Advanced Workbook System

## Was dieses Projekt ist

Dieses Repository enthält ein wiederverwendbares 3-Phasen-System zur Erstellung von Advanced Workbooks für die IU Internationale Hochschule. Das System funktioniert für jeden IU-Kurs mit diesem Prüfungsformat.

---

## Ordnerstruktur

```
Repo-Root/
├── CLAUDE.md
├── README.md
├── .gitignore
├── scripts/                          # Gemeinsame Scripts für alle Kurse
│   ├── generate_workbook.py
│   ├── extract_aufgaben.py
│   ├── template.docx
│   └── requirements.txt
└── arbeiten/
    ├── InterkulturellePsy/           # Ein Kurs pro Unterordner
    │   ├── eingang/                  # Original-PDFs der Hochschule (niemals ändern)
    │   ├── entwurf/
    │   │   ├── config.json           # Persönliche Daten + Kursinfos (User füllt aus)
    │   │   ├── aufgabe_N.md          # Inhaltsentwürfe (eine Datei pro Aufgabe)
    │   │   └── literaturverzeichnis.md
    │   └── ausgabe/                  # Generiertes Word-Dokument
    └── [NeuerKurs]/
        ├── eingang/
        ├── entwurf/
        └── ausgabe/
```

---

## Pflichtregeln – immer einhalten

**Quellen:**
- Inhalte ausschließlich aus dem Kurs-Skript sowie der dort aufgelisteten Basis- und Weiterführenden Literatur des Skripts benutzen
- Keine externen Quellen, keine Inhalte aus dem Internet, kein Allgemeinwissen
- Wenn eine Information nicht im Skript steht, nicht erfinden – stattdessen offen kommunizieren, was fehlt

**Zitieren:**

- Zitierstandard: **APA 7**, ohne Ausnahme:
  - **Inline-Zitat im Text**: `(Autor, Jahr)` – ohne Seitenangaben
    - Keine direkten Zitate – ausschließlich sinngemäße Paraphrasen in eigenen Worten daher ohne Seitenangabe
    - **Autor:**
      - Bei 2 Autoren die Namen mit "&" (und) verbinden
      - Bei mehr als 2 Autoren, nur den ersten Autor Schreiben und danach "et al." verwenden

  - **Literaturverzeichnis**:
    - Jede verwendete Quelle muss im `literaturverzeichnis.md` vollständig aufgeführt sein.
    - Das Literaturverzeichnis wird alphabetisch, nach den Nachnamen der Autoren, und bei
      gleicher Autorenschaft mehrerer Quellen chronologisch nach Erscheinungsjahr geordnet.


**Zitierpräzision – kritische Regel:**

Eine Seitenangabe darf NUR dort stehen, wo der zitierte Inhalt auf dieser Seite tatsächlich so steht.

Es gibt zwei klar zu trennende Texttypen:

1. **Theoriedarstellung** (zitierpflichtig): Definitionen, Modelle, Daten und Aussagen,
   die direkt aus einer Quelle stammen. Hier steht `(Autor, Jahr)` unmittelbar
   nach der paraphrasierten Aussage.

2. **Eigene Schlussfolgerung** (nicht zitierpflichtig): Die Anwendung einer Theorie auf
   einen konkreten Fall, eigene Argumentation oder Interpretation. Hier steht **kein
   Zitat** – der Satz ist als eigene Denkleistung kenntlich.

**Verbotenes Muster:**

> „[Eigene Schlussfolgerung], was [Behauptung] erklärt (Autor, Jahr, S. X)."
→ Die Seitenangabe deckt hier die eigene Schlussfolgerung ab – das ist ein Zitierfehler.

**Korrektes Muster:**

> „[Paraphrase der Theorie] (Autor, Jahr). [Eigene Schlussfolgerung ohne Zitat]."
→ Das Zitat belegt nur die Theorie; die Anwendung steht eigenständig daneben.

**Vor jedem Zitat innerhalb gedanklich prüfen:**
„Würde jemand, der diese Seite aufschlägt, genau diese Aussage dort finden?"
Wenn nein → kein Zitat an dieser Stelle setzen.

**Umfang pro Aufgabe:**

- 0,5 bis 1 DIN-A4-Seite Text (ca. 200–400 Wörter bei korrekter Formatierung)
- Klar strukturiert, argumentativ aufgebaut, auf die Aufgabenstellung bezogen

**Sprache:**

- Deutsch, akademischer Stil, keine umgangssprachlichen Formulierungen

---

## 3-Phasen-Workflow

### Phase 1 – Inhaltsentwurf (Claude arbeitet autonom)

0. Aufgabenstellungen extrahieren: `python scripts/extract_aufgaben.py <Kursname>` ausführen –
   erstellt pro Aufgabe eine `arbeiten/<Kursname>/entwurf/aufgabe_N.md` mit dem reinen Aufgabentext
1. Eingangsdokumente aus `arbeiten/<Kursname>/eingang/` lesen, WICHTIG ausschließlich nur nach Freigabe die Dateien lesen:
   - Aufgabenstellung (enthält alle N Aufgaben)
   - Prüfungsleitfaden (Formalia, Bewertung, Abgabe)
   - Kurs-Skript (Inhaltsquelle)
   - Leitfaden Plagiatsvermeidung (Zitierregeln)
2. Für jede Aufgabe die relevanten Kapitel im Skript identifizieren
3. Bearbeitung **unter** die bestehende Aufgabenstellung in jeder `arbeiten/<Kursname>/entwurf/aufgabe_N.md` schreiben (ab `# Aufgabe N`)
4. `arbeiten/<Kursname>/entwurf/literaturverzeichnis.md` mit allen verwendeten Quellen anlegen
5. Sicherstellen, dass jede Aufgabe die Aufgabenstellung vollständig beantwortet

**PDF-Lesen, nur nach Freigabe:** Das Skript mit `pdftotext` (poppler-utils) seitenweise extrahieren. Inhaltsverzeichnis zuerst lesen, dann kapitelweise die relevanten Seiten.

### Phase 2 – Review & Anpassung (User + Claude iterieren)

- User liest die Entwürfe und gibt Feedback im Chat
- Claude passt die betreffende `.md`-Datei direkt an
- Jederzeit: User kann `.md`-Dateien auch selbst bearbeiten
- Wiederholbar bis zur Zufriedenheit des Users

### Phase 3 – Word-Generierung (Script)

```bash
python scripts/generate_workbook.py <Kursname>
```

Liest `config.json` + alle `aufgabe_N.md` + `literaturverzeichnis.md` aus `arbeiten/<Kursname>/entwurf/` und erzeugt:
`arbeiten/<Kursname>/ausgabe/JJJJMMTT_Nachname_Vorname_MatNr_[Kurskürzel].docx`

---

## Markdown-Format der Entwurfsdateien

```markdown
# Aufgabe N

Aufgabenstellung als reiner Text (wird kursiv im Word gerendert).

---

Fließtext mit paraphrasierten Inhalten in eigenen Worten.
Inline-Zitat: (Autor, Jahr)

## Optionale Zwischenüberschrift

Weiterer Fließtext...
```

- `#` = Aufgabentitel (Arial 12 pt, fett im Word-Output)
- Text zwischen `# Aufgabe N` und `---` = Aufgabenstellung (Arial 11 pt, kursiv im Word-Output)
- `---` = Trenner zwischen Aufgabenstellung und Bearbeitung
- `##` = Zwischenüberschrift (Arial 11 pt, fett)
- `**fett**` = Hervorhebung innerhalb von Absätzen
- `*kursiv*` = Kursivschrift (z.B. für Buchtitel im Literaturverzeichnis)
- Keine Stichpunktlisten als Hauptstruktur – Fließtext bevorzugt

---

## Word-Formatierung (automatisch durch Script)

| Einstellung | Wert |
|---|---|
| Schriftart Text | Arial 11 pt |
| Schriftart Überschriften | Arial 12 pt, fett |
| Zeilenabstand | 1,5 |
| Seitenränder | Aus `template.docx` |
| Satzformat | Blocksatz |
| Absatzabstand nach | 6 pt |
| Seitenzahlen | Zentriert unten, arabisch ab Seite 2 (Titelblatt ohne Nummer) |
| Literaturverzeichnis | APA 7 hängender Einzug (1,27 cm) automatisch |
| Titelblatt | Vollständig aus `config.json → titelblatt` generiert |
| Silbentrennung | Aus `template.docx` (einmalig dort aktivieren) |

**Template `scripts/template.docx`** (einmalig in Word erstellen):
- `Layout → Silbentrennung → Automatisch`
- `Überprüfen → Sprache → Deutsch (Deutschland)` als Standard
- Footer leer lassen (Script befüllt ihn für den Inhaltsteil)
- Seitenränder nach Vorgabe setzen

---

## Wenn ein neuer Kurs beginnt

1. Neuen Ordner unter `arbeiten/` anlegen: `arbeiten/NeuerKurs/` mit Unterordnern `eingang/`, `entwurf/`, `ausgabe/`
2. Neue Eingangsdokumente in `arbeiten/NeuerKurs/eingang/` ablegen
3. `arbeiten/NeuerKurs/entwurf/config.json` mit neuen Kursdaten befüllen – insbesondere `titelblatt`-Array anpassen
4. `scripts/` bleibt unverändert – Scripts und Template sind kursübergreifend wiederverwendbar
5. Phase 1 starten: `python scripts/extract_aufgaben.py NeuerKurs` → Claude liest Skript und schreibt neue Entwürfe

---

## Kommunikation mit dem User

- Klar melden, welche Seiten des Skripts für welche Aufgabe relevant sind
- Bei unklaren Aufgabenstellungen nachfragen, nicht raten
- Änderungswünsche aus dem Feedback direkt in die betreffende `.md`-Datei schreiben,
  nicht nur im Chat antworten
- Nach jeder inhaltlichen Änderung kurz zusammenfassen, was geändert wurde
