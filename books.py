class Book:
    def __init__(self, autor, tytul, rok, strony, egzemplarze):
        self.autor = autor
        self.tytul = tytul
        self.rok = rok
        self.strony = strony
        self.egzemplarze = egzemplarze

    def __str__(self):
        return f"\"{self.tytul}\" – {self.autor} ({self.rok}), {self.strony} stron, {self.egzemplarze} egz."

    def czy_dostepna(self):
        return self.egzemplarze > 0

    def wypozycz(self):
        if self.egzemplarze > 0:
            self.egzemplarze -= 1
            return True
        return False

    def zwroc(self):
        self.egzemplarze += 1


def dodaj_ksiazke(lista_ksiazek):
    print("\nDODAWANIE NOWEJ KSIĄŻKI")
    autor = input("Autor: ").strip()
    tytul = input("Tytuł: ").strip()
    rok = int(input("Rok wydania: "))
    strony = int(input("Liczba stron: "))
    egzemplarze = int(input("Liczba egzemplarzy: "))
    nowa = Book(autor, tytul, rok, strony, egzemplarze)
    lista_ksiazek.append(nowa)
    print(f"\nDodano książkę: {nowa}")


def edytuj_ksiazke(lista_ksiazek):
    print("\nEDYCJA KSIĄŻKI")
    if not lista_ksiazek:
        print("Brak książek.")
        return

    for i, ksiazka in enumerate(lista_ksiazek, start=1):
        print(f"{i}. {ksiazka}")

    try:
        index = int(input("Wybierz numer książki do edycji: ")) - 1
        ksiazka = lista_ksiazek[index]
    except (ValueError, IndexError):
        print("Nieprawidłowy numer.")
        return

    ksiazka.autor = input(f"Nowy autor ({ksiazka.autor}): ") or ksiazka.autor
    ksiazka.tytul = input(f"Nowy tytuł ({ksiazka.tytul}): ") or ksiazka.tytul
    try:
        ksiazka.rok = int(input(f"Nowy rok wydania ({ksiazka.rok}): ") or ksiazka.rok)
        ksiazka.strony = int(input(f"Nowa liczba stron ({ksiazka.strony}): ") or ksiazka.strony)
        ksiazka.egzemplarze = int(input(f"Nowa liczba egzemplarzy ({ksiazka.egzemplarze}): ") or ksiazka.egzemplarze)
    except ValueError:
        print("Błąd formatu danych – edycja anulowana.")


def usun_ksiazke(lista_ksiazek):
    print("\nUSUWANIE KSIĄŻKI")
    if not lista_ksiazek:
        print("Brak książek.")
        return

    for i, ksiazka in enumerate(lista_ksiazek, start=1):
        print(f"{i}. {ksiazka}")

    try:
        index = int(input("Wybierz numer książki do usunięcia: ")) - 1
        usunieta = lista_ksiazek.pop(index)
        print(f"Usunięto: {usunieta}")
    except (ValueError, IndexError):
        print("Niepoprawny numer.")
