PATH = "."
FILE = "Esercizi di Laboratorio di Intelligenza Artificiale Applicata.md"

INTRO = "Questi sono gli esercizi presi per il corso di \"Laboratorio di Intelligenza Artificiale Applicata\":\n\n"

from pathlib import Path

# get files
directory = Path(PATH)
files = [f for f in directory.iterdir() if f.is_file()]
files.sort(key=lambda f: f.name)

# put them in .md 
with open(FILE, "w") as md:
    md.write(INTRO)
    for i, f in enumerate(files):
        if f.name == FILE: 
            continue
        md.write(f"- Esercizio {i}: [{f.stem}]({f.name})\n")

