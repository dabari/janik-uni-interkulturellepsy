# Advanced Workbook – DLBWPIPS01 Interkulturelle Psychologie

## Eingangsdokumente (`eingang/`)

| Datei | Inhalt |
|---|---|
| `Aufgabenstellung Advanced Workbook DLBWPIPS01_1.pdf` | Die 6 Aufgaben des Workbooks |
| `Prüfungsleitfaden Advanced Workbook.pdf` | Formalia, Bewertungsschema, Abgaberegeln |
| `Skript_InterkulturellePsy.pdf` | Kursskript – **einzige Inhaltsquelle** (inkl. Basis- und Weiterführende Literatur S. 7–9) |
| `Leitfaden Vermeidung Plagiat.pdf` | Plagiatsvermeidung, Zitierregeln |

> **Zitierstandard: APA 7 – ausschließlich.**

---

## Workflow: 3 Phasen

### Phase 1 – Inhaltsentwurf (einmalig, von Claude erledigt)

Claude liest alle Eingangsdokumente und schreibt die Entwürfe für alle 6 Aufgaben als Markdown-Dateien in `entwurf/`. Dies ist bereits geschehen.

### Phase 2 – Review & Anpassung (du + Claude, iterativ)

1. Öffne die Entwürfe in `entwurf/aufgabe_1.md` bis `aufgabe_6.md`
2. Lies jeden Entwurf durch
3. Gib Claude Feedback im Chat, z.B.:
   - „Aufgabe 3 – der zweite Absatz ist zu kurz, bitte ausführlicher"
   - „Aufgabe 1 – bitte auch die Dimension Langzeitorientierung für China erklären"
4. Claude passt die `.md`-Datei direkt an
5. Wiederhole bis du zufrieden bist

Du kannst die `.md`-Dateien auch selbst direkt bearbeiten (z.B. in VS Code oder Notepad).

### Phase 3 – Word-Dokument generieren

Wenn alle Entwürfe fertig sind:

```bash
python scripts/generate_workbook.py
```

Das Script liest `entwurf/config.json` + alle `aufgabe_N.md` + `literaturverzeichnis.md` und erzeugt:

```
ausgabe/JJJJMMTT_Nachname_Vorname_MatNr_DLBWPIPS01.docx
```

Danach: Word öffnen → **Datei → Exportieren → PDF** → bei Turnitin einreichen.

---

## Vor der ersten Abgabe: config.json ausfüllen

Öffne `entwurf/config.json` und trage deine persönlichen Daten ein:

```json
{
  "name_nachname": "Dein Nachname",
  "name_vorname": "Dein Vorname",
  "matrikelnummer": "Deine Matrikelnummer",
  "studiengang": "Bachelor Wirtschaftspsychologie",
  "kurs_bezeichnung": "DLBWPIPS01 – Interkulturelle Psychologie",
  "art_der_arbeit": "Advanced Workbook",
  "tutor": "Name deines Tutors",
  "datum": "2025-03-25",
  "kurskuerzel": "DLBWPIPS01"
}
```

---

## Ordnerstruktur

```
InterkulturellePsy/
├── eingang/                         # Original-PDFs der Hochschule (nicht ändern)
├── entwurf/
│   ├── config.json                  # Persönliche Daten → hier ausfüllen!
│   ├── aufgabe_1.md                 # Entwurf Aufgabe 1 (Hofstede-Modell)
│   ├── aufgabe_2.md                 # Entwurf Aufgabe 2 (Forschungsbereiche)
│   ├── aufgabe_3.md                 # Entwurf Aufgabe 3 (Unternehmenskultur)
│   ├── aufgabe_4.md                 # Entwurf Aufgabe 4 (Diversity Management)
│   ├── aufgabe_5.md                 # Entwurf Aufgabe 5 (7P-Marketing)
│   ├── aufgabe_6.md                 # Entwurf Aufgabe 6 (Kulturkonzept + Messung)
│   └── literaturverzeichnis.md      # Alle Quellen in APA 7
├── ausgabe/                         # Generiertes Word-Dokument landet hier
└── scripts/
    ├── generate_workbook.py         # Hauptskript: Markdown → Word
    └── requirements.txt             # Python-Abhängigkeiten (python-docx)
```

---

## Word-Formatierung (laut Prüfungsleitfaden)

Das Script setzt diese Formatierung automatisch:

| Einstellung | Wert |
|---|---|
| Schriftart Text | Arial 11 pt |
| Schriftart Überschriften | Arial 12 pt, fett |
| Zeilenabstand | 1,5 |
| Seitenränder | 2 cm rundum |
| Satzformat | Blocksatz |
| Absatzabstand nach | 6 pt |
| Seitenzahlen | Zentriert unten, arabisch ab Seite 1 |
| Titelblatt | Aus config.json generiert |

> **Silbentrennung:** In Word manuell aktivieren: `Layout → Silbentrennung → Automatisch`

---

## Voraussetzungen

- Python 3 installiert
- `python-docx` installiert (`pip install python-docx`)
- `poppler-utils` installiert (`sudo apt-get install poppler-utils`) – für das Lesen der PDFs durch Claude
