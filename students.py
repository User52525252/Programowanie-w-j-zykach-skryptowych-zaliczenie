from datetime import datetime

class Student:
    def __init__(self, imie, nazwisko, indeks, wypozyczone=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.indeks = indeks
        self.wypozyczone = wypozyczone if wypozyczone else []

    def __str__(self):
        return f"{self.imie} {self.nazwisko} (ID: {self.indeks}) – {len(self.wypozyczone)} książek"

    def moze_wypozyczyc(self):
        return len(self.wypozyczone) < 5

    def wypozycz(self, tytul):
        if self.moze_wypozyczyc():
            dzis = datetime.now().strftime("%Y-%m-%d")
            self.wypozyczone.append({"tytul": tytul, "data": dzis})
            return True
        return False

    def zwroc(self, tytul):
        for ks in self.wypozyczone:
            if ks["tytul"] == tytul:
                self.wypozyczone.remove(ks)
                return True
        return False

def dodaj_studenta(lista_studentow):
    if len(lista_studentow) >= 15:
        print("Osiągnięto limit 15 studentów.")
        return
    imie = input("Imię: ").strip()
    nazwisko = input("Nazwisko: ").strip()
    indeks = input("ID / numer indeksu: ").strip()
    for s in lista_studentow:
        if s.indeks == indeks:
            print("Student z takim ID już istnieje.")
            return
    nowy = Student(imie, nazwisko, indeks)
    lista_studentow.append(nowy)
    print(f"Dodano studenta: {nowy}")

def wybierz_studenta(lista_studentow):
    if not lista_studentow:
        print("Brak studentów w systemie.")
        return None
    for i, student in enumerate(lista_studentow, start=1):
        print(f"{i}. {student}")
    try:
        index = int(input("Wybierz numer studenta: ")) - 1
        return lista_studentow[index]
    except (ValueError, IndexError):
        print("Błędny numer.")
        return None

def wypozycz_ksiazke(student, lista_ksiazek):
    if not student.moze_wypozyczyc():
        print("Ten student ma już 5 książek.")
        return
    for i, ksiazka in enumerate(lista_ksiazek, start=1):
        print(f"{i}. {ksiazka}")
    try:
        wybor = int(input("Wybierz numer książki do wypożyczenia: ")) - 1
        ksiazka = lista_ksiazek[wybor]
    except (ValueError, IndexError):
        print("Nieprawidłowy numer.")
        return
    if not ksiazka.czy_dostepna():
        print("Brak dostępnych egzemplarzy.")
        return
    if student.wypozycz(ksiazka.tytul):
        ksiazka.wypozycz()
        print(f"Wypożyczono: {ksiazka.tytul}")
    else:
        print("Nie można wypożyczyć.")

def zwroc_ksiazke(student, lista_ksiazek):
    if not student.wypozyczone:
        print("Ten student nie ma wypożyczonych książek.")
        return
    for i, item in enumerate(student.wypozyczone, start=1):
        print(f"{i}. {item['tytul']} (od: {item['data']})")
    try:
        wybor = int(input("Wybierz numer książki do zwrotu: ")) - 1
        tytul = student.wypozyczone[wybor]["tytul"]
    except (ValueError, IndexError):
        print("Błędny numer.")
        return
    if student.zwroc(tytul):
        for ksiazka in lista_ksiazek:
            if ksiazka.tytul == tytul:
                ksiazka.zwroc()
                break
        print(f"Zwrócono: {tytul}")
