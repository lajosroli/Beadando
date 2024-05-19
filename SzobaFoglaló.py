from abc import ABC, abstractmethod
from datetime import datetime

#Osztály létrehozás
class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def leiras(self):
        pass

class EgyesSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=6000, szobaszam=szobaszam)

    def leiras(self):
        return f"Egyágyas szoba, ára: {self.ar} HUF, szobaszám: {self.szobaszam}"

class KettesSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=9000, szobaszam=szobaszam)

    def leiras(self):
        return f"Kétágyas szoba, ára: {self.ar} HUF, szobaszám: {self.szobaszam}"

class Szálloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def szoba_hozzaadas(self, szoba):
        self.szobak.append(szoba)

class Foglalás:
    def __init__(self, szalloda, szoba, datum):
        self.szalloda = szalloda
        self.szoba = szoba
        self.datum = datum


#Foglalás kezelése

class Szálloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadas(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szoba_szam, datum):
        if not self._datum_ervenyes(datum):
            return "Érvénytelen dátum!"
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szoba_szam and foglalas.datum == datum:
                return "A szoba foglalt az adott dátumon!"
        for szoba in self.szobak:
            if szoba.szobaszam == szoba_szam:
                uj_foglalas = Foglalas(self, szoba, datum)
                self.foglalasok.append(uj_foglalas)
                return f"Foglalás sikeres! Ára: {szoba.ar} HUF"
        return "Nincs ilyen szoba!"

    def lemondas(self, szoba_szam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szoba_szam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return "Foglalás lemondva!"
        return "Nincs ilyen foglalás!"

    def listaz_foglalasok(self):
        if not self.foglalasok:
            return "Nincsenek foglalások."
        eredmeny = "Foglalások listája:\n"
        for foglalas in self.foglalasok:
            eredmeny += f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}, Ár: {foglalas.szoba.ar} HUF\n"
        return eredmeny


#Felhasználói interfész és adatvalidáció

def main():
    szalloda = Szalloda("Példa Szálloda")
    szalloda.szoba_hozzaadas(EgyesSzoba(101))
    szalloda.szoba_hozzaadas(KettesSzoba(102))
    szalloda.szoba_hozzaadas(KettesSzoba(103))

    szalloda.foglalas(101, "2024-06-01")
    szalloda.foglalas(102, "2024-06-02")
    szalloda.foglalas(103, "2024-06-03")
    szalloda.foglalas(101, "2024-06-04")
    szalloda.foglalas(102, "2024-06-05")

    while True:
        print("\n--- Szállodai Foglalási Rendszer ---")
        print("1: Szoba foglalás")
        print("2: Foglalás lemondás")
        print("3: Foglalások listázás")
        print("4: Kilépés")
        valasztas = input("Válasszon egy lehetőséget(1-4): ")

        if valasztas == "1":
            szoba_szam = int(input("Addja meg a szoba számát: "))
            datum = input("Addja meg a foglalás dátumát (YYYY-MM-DD): ")
            print(szalloda.foglalas(szoba_szam, datum))
        elif valasztas == "2":
            szoba_szam = int(input("Addja meg a szoba számát: "))
            datum = input("Addja meg a foglalás dátumát (YYYY-MM-DD): ")
            print(szalloda.lemondas(szoba_szam, datum))
        elif valasztas == "3":
            print(szalloda.listaz_foglalasok())
        elif valasztas == "4":
            break
        else:
            print("Nincs ilyen lehetőség, próbálja újra.")

if __name__ == "__main__":
    main()