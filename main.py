from books import dodaj_ksiazke, edytuj_ksiazke, usun_ksiazke
from students import (
    dodaj_studenta, Student,
    wybierz_studenta, wypozycz_ksiazke, zwroc_ksiazke
)
from storage import zapisz_ksiazki, wczytaj_ksiazki, zapisz_studentow, wczytaj_studentow
from datetime import datetime

ksiazki = wczytaj_ksiazki()
if not ksiazki:
    from data import get_books
    ksiazki = get_books()

studenci = wczytaj_studentow()

def wyswietl_ksiazki():
    print("\nDOSTĘPNE KSIĄŻKI:")
    for i, k in enumerate(ksiazki, 1):
        print(f"{i}. {k}")

def raport_studentow():
    print("\nRAPORT WYPOŻYCZEŃ:")
    if not studenci:
        print("Brak studentów w systemie.")
        return
    for student in studenci:
        print(f"- {student}")
        for item in student.wypozyczone:
            tytul = item["tytul"]
            data = item["data"]
            days = (datetime.now() - datetime.strptime(data, "%Y-%m-%d")).days
            info = f"{tytul} (od: {data})"
            if days > 14:
                info += f" – SPÓŹNIONA o {days - 14} dni"
            print("   " + info)

def main_menu():
    while True:
        print("\nMENU")
        print("1. Wyświetl książki")
        print("2. Dodaj książkę")
        print("3. Edytuj książkę")
        print("4. Usuń książkę")
        print("5. Dodaj studenta")
        print("6. Wypożycz książkę")
        print("7. Zwróć książkę")
        print("8. Raport wypożyczeń")
        print("9. Wyjście")

        wybor = input("Wybierz opcję (1-9): ")

        if wybor == "1":
            wyswietl_ksiazki()
        elif wybor == "2":
            dodaj_ksiazke(ksiazki)
        elif wybor == "3":
            edytuj_ksiazke(ksiazki)
        elif wybor == "4":
            usun_ksiazke(ksiazki)
        elif wybor == "5":
            dodaj_studenta(studenci)
        elif wybor == "6":
            s = wybierz_studenta(studenci)
            if s:
                wypozycz_ksiazke(s, ksiazki)
        elif wybor == "7":
            s = wybierz_studenta(studenci)
            if s:
                zwroc_ksiazke(s, ksiazki)
        elif wybor == "8":
            raport_studentow()
        elif wybor == "9":
            zapisz_ksiazki(ksiazki)
            zapisz_studentow(studenci)
            print("Koniec programu.")
            break
        else:
            print("Zły wybór.")

if __name__ == "__main__":
    main_menu()
