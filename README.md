# Advanced Workbook System

Wiederverwendbares 3-Phasen-System zur Erstellung von Advanced Workbooks für die IU Internationale Hochschule. Funktioniert für jeden IU-Kurs mit diesem Prüfungsformat – Entwürfe, Zitierung und Word-Generierung sind vollständig kursübergreifend gehalten.

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
    │   ├── eingang/                  # Original-PDFs der Hochschule (nicht ändern)
    │   ├── entwurf/
    │   │   ├── config.json           # Persönliche Daten + Deckblatt → hier ausfüllen!
    │   │   ├── aufgabe_1.md          # Inhaltsentwurf Aufgabe 1
    │   │   ├── aufgabe_N.md          # ... weitere Aufgaben
    │   │   └── literaturverzeichnis.md
    │   └── ausgabe/                  # Generiertes Word-Dokument landet hier
    └── [NeuerKurs]/
        ├── eingang/
        ├── entwurf/
        └── ausgabe/
```

> **Beispiel (aktueller Kurs):** `DLBWPIPS01 – Interkulturelle Psychologie` mit 6 Aufgaben unter `arbeiten/InterkulturellePsy/entwurf/` (`aufgabe_1.md` bis `aufgabe_6.md`).

---

## Eingangsdokumente (`arbeiten/<Kursname>/eingang/`)

Die Hochschule stellt pro Kurs typischerweise diese Dokumente bereit:

| Typ | Inhalt |
|---|---|
| Aufgabenstellung | Die N Aufgaben des Workbooks |
| Prüfungsleitfaden | Formalia, Bewertungsschema, Abgaberegeln |
| Kursskript | **Einzige Inhaltsquelle** (inkl. Basis- und Weiterführende Literatur) |
| Plagiatsvermeidung | Zitierregeln der Hochschule |

> **Zitierstandard: APA 7 – ausschließlich.**

---

## Workflow: 3 Phasen

### Phase 1 – Inhaltsentwurf (einmalig, von Claude erledigt)

Claude liest alle Eingangsdokumente und schreibt für jede Aufgabe eine Markdown-Datei in `arbeiten/<Kursname>/entwurf/`. Inhalte stammen ausschließlich aus dem Kursskript und der dort gelisteten Literatur.

> **Beispiel:** Für DLBWPIPS01 wurden 6 Entwürfe erstellt – u.a. zur Anwendung des Hofstede-Modells (Aufgabe 1) und zum interkulturellen Marketing-Mix (Aufgabe 5).

### Phase 2 – Review & Anpassung (du + Claude, iterativ)

1. Öffne die Entwürfe in `arbeiten/<Kursname>/entwurf/aufgabe_N.md`
2. Lies jeden Entwurf durch
3. Gib Claude Feedback im Chat, z.B.:
   - „Aufgabe 3 – der zweite Absatz ist zu kurz, bitte ausführlicher"
   - „Aufgabe 1 – bitte auch die Dimension Langzeitorientierung erklären"
4. Claude passt die `.md`-Datei direkt an
5. Wiederhole bis du zufrieden bist

Die `.md`-Dateien können auch direkt bearbeitet werden (z.B. in VS Code oder Notepad).

### Phase 3 – Word-Dokument generieren

Wenn alle Entwürfe fertig sind:

```bash
python scripts/generate_workbook.py InterkulturellePsy
```

Das Script liest `config.json` + alle `aufgabe_N.md` + `literaturverzeichnis.md` aus `arbeiten/<Kursname>/entwurf/` und erzeugt:

```
arbeiten/<Kursname>/ausgabe/JJJJMMTT_Nachname_Vorname_MatNr_[Kurskürzel].docx
```

> **Beispiel:** `arbeiten/InterkulturellePsy/ausgabe/20260221_Baricevic_Janik_12345678_DLBWPIPS01.docx`

Danach: Word öffnen → **Datei → Exportieren → PDF** → bei Turnitin einreichen.

---

## config.json ausfüllen

Öffne `arbeiten/<Kursname>/entwurf/config.json` und trage die Kursdaten ein. Die flachen Felder dienen als Platzhalter im `titelblatt`-Array und werden für den Dateinamen verwendet.

```json
{
  "name_nachname": "Baricevic",
  "name_vorname": "Janik",
  "matrikelnummer": "12345678",
  "studiengang": "Bachelor Wirtschaftspsychologie",
  "kurs_bezeichnung": "DLBWPIPS01 – Interkulturelle Psychologie",
  "art_der_arbeit": "Advanced Workbook",
  "tutor": "Name des Tutors",
  "datum": "2026-02-21",
  "kurskuerzel": "DLBWPIPS01",
  "titelblatt": [
    { "text": "IU Internationale Hochschule", "size": 12, "bold": true, "space_after": 0 },
    { "text": "{studiengang}", "size": 11, "space_after": 30 },
    { "text": "{art_der_arbeit}", "size": 14, "bold": true, "space_after": 6 },
    { "text": "im Kurs", "size": 11, "space_after": 6 },
    { "text": "{kurs_bezeichnung}", "size": 12, "bold": true, "space_after": 60 },
    { "label": "Name", "value": "{name_vorname} {name_nachname}", "space_after": 3 },
    { "label": "Matrikelnummer", "value": "{matrikelnummer}", "space_after": 3 },
    { "label": "Tutor/in", "value": "{tutor}", "space_after": 3 },
    { "label": "Abgabedatum", "value": "{datum}", "space_after": 3 },
    { "text": "" }
  ]
}
```

Das `titelblatt`-Array definiert jede Zeile des Deckblatts. `{schlüssel}` wird durch den gleichnamigen Wert aus der config ersetzt. Zeilen können frei hinzugefügt, entfernt oder umsortiert werden – das Script hardcodet keinen Inhalt.

---

## Markdown-Format der Entwurfsdateien

```markdown
# Aufgabe 1

Fließtext mit paraphrasierten Inhalten. Inline-Zitat: (Autor, Jahr)

## Optionale Zwischenüberschrift

Weiterer Fließtext mit **Hervorhebung** oder *Kursivschrift*.
```

| Syntax | Bedeutung |
|---|---|
| `# Titel` | Aufgabentitel (Arial 12 pt, fett) |
| `## Zwischentitel` | Zwischenüberschrift (Arial 11 pt, fett) |
| `**text**` | Fettdruck |
| `*text*` | Kursiv (z.B. für Buchtitel im Literaturverzeichnis) |
| `(Autor, Jahr)` | APA 7 Inline-Zitat – keine Seitenangabe |

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
| Literaturverzeichnis | APA 7 hängender Einzug (1,27 cm) |
| Titelblatt | Vollständig aus `config.json → titelblatt` generiert |
| Silbentrennung | Aus `template.docx` |

### Template einmalig vorbereiten

`scripts/template.docx` in Word öffnen und folgendes einstellen:

1. `Layout → Silbentrennung → Automatisch`
2. `Überprüfen → Sprache → Deutsch (Deutschland)` als Standard setzen
3. Seitenränder nach Vorgabe der Hochschule setzen (i.d.R. 2 cm rundum)
4. Footer leer lassen (Script befüllt ihn automatisch)
5. Speichern

Das Template ist kursübergreifend wiederverwendbar.

---

## Neuen Kurs anlegen

1. Neuen Ordner unter `arbeiten/` anlegen: `arbeiten/NeuerKurs/` mit Unterordnern `eingang/`, `entwurf/`, `ausgabe/`
2. Eingangsdokumente in `arbeiten/NeuerKurs/eingang/` ablegen
3. `arbeiten/NeuerKurs/entwurf/config.json` mit neuen Kursdaten befüllen
4. `scripts/` bleibt unverändert – Scripts und Template sind kursübergreifend wiederverwendbar
5. Claude Phase 1 starten: `python scripts/extract_aufgaben.py NeuerKurs`

---

## Voraussetzungen

- Python 3
- `pip install python-docx`
- `poppler-utils` (`sudo apt-get install poppler-utils`) – für Claude zum Lesen der PDFs
