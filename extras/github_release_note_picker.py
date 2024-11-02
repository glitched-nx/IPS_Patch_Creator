"""
File: github_release_notes_picker.py
Author: glitched-nx
Description:
    This script retrieves the latest release information from a GitHub repository.
    It stores the details of the last five releases in a Markdown file
    and displays the filtered release information in the console.

"""

import requests
# API-URL für alle Releases
url = "https://api.github.com/repos/AK478BB/Sigpatches/releases"

# Abrufen der Daten
response = requests.get(url)
releases = response.json()

# Speichern der letzten fünf aktuellsten Releases
latest_releases = releases[:5]

# Erstellen und Schreiben der Markdown-Datei
with open("sigpatches_release_notes.md", "w", encoding="utf-8") as md_file:
    md_file.write("# Release Notes\n\n")
    for release in latest_releases:
        md_file.write(f"## {release['name']}\n")
        md_file.write(f"**Erstellt am:** {release['created_at']}\n\n")
        md_file.write(f"{release['body']}\n")
        md_file.write("\n" + "-" * 40 + "\n\n")

# Ausgabe der gefilterten Releases in der Konsole
for release in latest_releases:
    print(f"Tag: {release['tag_name']}")
    print(f"Name: {release['name']}")
    print(f"Beschreibung: {release['body']}")
    print(f"Erstellt am: {release['created_at']}")
    print("-" * 40)
