from init_adatok import init_rendszer

def menu():
    print("\n--- Repülőjegy Foglalási Rendszer ---")
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
            for j in legitarsasag.listaz_jaratok():
                print(j)
        elif valasz == "2":
            nev = input("Utas neve: ")
            jaratszam = input("Járatszám: ")
            jarat = legitarsasag.keres_jarat(jaratszam)
            if jarat:
                foglalasok.append(JegyFoglalas(nev, jarat))
                print(f"Foglalás rögzítve. Ár: {jarat.jegyar} Ft")
            else:
                print("Nincs ilyen járatszám.")
        elif valasz == "3":
            nev = input("Utas neve: ")
            jaratszam = input("Járatszám: ")
            talalat = None
            for f in foglalasok:
                if f.utas_nev == nev and f.jarat.jaratszam == jaratszam:
                    talalat = f
                    break
            if talalat:
                foglalasok.remove(talalat)
                print("Foglalás törölve.")
            else:
                print("Nem található ilyen foglalás.")
        elif valasz == "4":
            for f in foglalasok:
                print(f.info())
        elif valasz == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
