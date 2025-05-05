from init_adatok import init_rendszer
from jegyfoglalas import JegyFoglalas

def menu():
    print("\n--- GDE - air Repülőjegy Foglalási Rendszer ---")
    print("1. Járatok listázása")
    print("2. Jegy foglalása")
    print("3. Foglalás lemondása")
    print("4. Foglalások listázása")
    print("0. Kilépés")

def main():
    legitarsasag, foglalasok = init_rendszer()

    while True:
        menu()
        valasz = input("Választás: ")

        if valasz == "1":
            print("\nElérhető járatok:")
            for jarat_info in legitarsasag.listaz_jaratokat():
                print(jarat_info)

        elif valasz == "2":
            nev = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a járatszámot: ")
            jarat = legitarsasag.keres_jarat(jaratszam)

            if jarat:
                foglalas = JegyFoglalas(nev, jarat)
                foglalasok.append(foglalas)
                print(f"Sikeres foglalás! Ár: {jarat.jegyar} Ft")
            else:
                print("Hibás járatszám!")

        elif valasz == "3":
            nev = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a járatszámot: ")

            torlendo = None
            for f in foglalasok:
                if f.utas_nev == nev and f.jarat.jaratszam == jaratszam:
                    torlendo = f
                    break

            if torlendo:
                foglalasok.remove(torlendo)
                print("Foglalás törölve.")
            else:
                print("Nem található ilyen foglalás.")

        elif valasz == "4":
            if foglalasok:
                print("\nAktuális foglalások:")
                for f in foglalasok:
                    print(f.info())
            else:
                print("Nincs egyetlen foglalás sem.")

        elif valasz == "0":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás. Próbáld újra.")

if __name__ == "__main__":
    main()
