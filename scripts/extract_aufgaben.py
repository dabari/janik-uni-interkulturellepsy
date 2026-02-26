#!/usr/bin/env python3
"""
extract_aufgaben.py
Extracts individual task descriptions from the Aufgabenstellung PDF
and creates entwurf/aufgabe_N.md files with the task text.

Usage:
    python scripts/extract_aufgaben.py <Kursname>              # Interactive mode
    python scripts/extract_aufgaben.py <Kursname> --yes        # Auto-confirm

    Kursname = Name des Unterordners in arbeiten/, z.B. InterkulturellePsy

Requirements:
    pdftotext (poppler-utils) must be installed.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def find_aufgabenstellung_pdf(eingang_dir):
    """Find the Aufgabenstellung PDF in eingang/."""
    candidates = list(eingang_dir.glob("*ufgabenstellung*"))
    if not candidates:
        print(f"Fehler: Keine Aufgabenstellungs-PDF in {eingang_dir} gefunden.")
        sys.exit(1)
    if len(candidates) > 1:
        print("Mehrere Aufgabenstellungs-PDFs gefunden:")
        for i, c in enumerate(candidates, 1):
            print(f"  {i}. {c.name}")
        print(f"Verwende: {candidates[0].name}")
    return candidates[0]


def extract_text(pdf_path):
    """Extract full text from PDF using pdftotext."""
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", str(pdf_path), "-"],
            capture_output=True, text=True, check=True,
        )
        return result.stdout
    except FileNotFoundError:
        print("Fehler: pdftotext nicht gefunden. Bitte poppler-utils installieren:")
        print("  sudo apt install poppler-utils")
        sys.exit(1)


def parse_aufgaben(text):
    """
    Split extracted text into individual task descriptions.
    Looks for patterns like 'Aufgabenstellung N:' or 'Aufgabe N:'.
    Returns list of (number, task_text) tuples.
    """
    pattern = re.compile(
        r"Aufgabe(?:nstellung)?\s+(\d+)\s*:\s*\n",
        re.IGNORECASE,
    )

    matches = list(pattern.finditer(text))
    if not matches:
        print("Warnung: Kein 'Aufgabenstellung N:' / 'Aufgabe N:' Muster gefunden.")
        return []

    aufgaben = []
    for i, match in enumerate(matches):
        num = int(match.group(1))
        start = match.end()
        # End = start of next match or end of text
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        raw = text[start:end]

        # Clean up: remove page footers, trim whitespace
        lines = []
        for line in raw.splitlines():
            stripped = line.strip()
            # Skip page footers like "Seite 1 von 2" or headers like "PRÜFUNGSAMT"
            if re.match(r"^Seite\s+\d+\s+von\s+\d+$", stripped):
                continue
            if stripped in ("PRÜFUNGSAMT", "IU.DE"):
                continue
            lines.append(line)

        # Trim leading/trailing blank lines
        task_text = "\n".join(lines).strip()
        # Collapse multiple blank lines into one
        task_text = re.sub(r"\n{3,}", "\n\n", task_text)

        aufgaben.append((num, task_text))

    return aufgaben


def main():
    parser = argparse.ArgumentParser(description="Aufgabenstellungen aus PDF extrahieren")
    parser.add_argument("kursname",
                        help="Ordnername unter arbeiten/, z.B. InterkulturellePsy")
    parser.add_argument("--yes", "-y", action="store_true",
                        help="Ohne Bestätigung direkt schreiben")
    args = parser.parse_args()

    kurs_dir = REPO_ROOT / "arbeiten" / args.kursname
    eingang_dir = kurs_dir / "eingang"
    entwurf_dir = kurs_dir / "entwurf"

    if not kurs_dir.exists():
        print(f"Fehler: Kursordner nicht gefunden: {kurs_dir}")
        sys.exit(1)

    pdf_path = find_aufgabenstellung_pdf(eingang_dir)
    print(f"PDF: {pdf_path.name}")

    text = extract_text(pdf_path)
    aufgaben = parse_aufgaben(text)

    if not aufgaben:
        print("Keine Aufgaben extrahiert. Bitte PDF-Format prüfen.")
        sys.exit(1)

    print(f"\n{len(aufgaben)} Aufgabenstellung(en) gefunden:\n")

    entwurf_dir.mkdir(exist_ok=True)

    for num, task_text in aufgaben:
        md_path = entwurf_dir / f"aufgabe_{num}.md"

        # Check if file already contains a bearbeitung (--- separator)
        if md_path.exists():
            existing = md_path.read_text(encoding="utf-8")
            if re.search(r"^---$", existing, re.MULTILINE):
                print(f"--- Aufgabe {num} ---")
                print(f"  ÜBERSPRUNGEN: {md_path.name} enthält bereits eine Bearbeitung (--- Trenner)")
                print()
                continue

        print(f"--- Aufgabe {num} ---")
        print(task_text)
        print()

        if not args.yes:
            answer = input(f"  → In {md_path.name} schreiben? [j/N] ").strip().lower()
            if answer not in ("j", "ja", "y", "yes"):
                print("  Übersprungen.")
                print()
                continue

        content = f"# Aufgabe {num}\n\n{task_text}\n"
        md_path.write_text(content, encoding="utf-8")
        print(f"  ✓ Geschrieben: {md_path.name}")
        print()

    print("Fertig.")


if __name__ == "__main__":
    main()
