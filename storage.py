import json
from books import Book
from students import Student

def zapisz_ksiazki(ksiazki, filename="ksiazki.json"):
    with open(filename, "w", encoding="utf-8") as f:
        dane = [vars(k) for k in ksiazki]
        json.dump(dane, f, indent=4, ensure_ascii=False)

def wczytaj_ksiazki(filename="ksiazki.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            dane = json.load(f)
            return [Book(**d) for d in dane]
    except FileNotFoundError:
        return []

def zapisz_studentow(studenci, filename="studenci.json"):
    with open(filename, "w", encoding="utf-8") as f:
        dane = [vars(s) for s in studenci]
        json.dump(dane, f, indent=4, ensure_ascii=False)

def wczytaj_studentow(filename="studenci.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            dane = json.load(f)
            return [Student(**d) for d in dane]
    except FileNotFoundError:
        return []
