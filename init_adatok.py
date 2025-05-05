from jarat import BelfoldiJarat, NemzetkoziJarat
from legitarsasag import LegiTarsasag
from jegyfoglalas import JegyFoglalas

def init_rendszer():
    legitarsasag = LegiTarsasag("PythonAir")

    j1 = BelfoldiJarat("B101", "Budapest")
    j2 = BelfoldiJarat("B102", "Debrecen")
    j3 = NemzetkoziJarat("N201", "London")

    legitarsasag.hozzaad_jarat(j1)
    legitarsasag.hozzaad_jarat(j2)
    legitarsasag.hozzaad_jarat(j3)

    foglalasok = [
        JegyFoglalas("Kiss Anna", j1),
        JegyFoglalas("Nagy Béla", j2),
        JegyFoglalas("Szabó Imre", j3),
        JegyFoglalas("Tóth Zsófi", j1),
        JegyFoglalas("Varga Péter", j2),
        JegyFoglalas("Kovács Lilla", j3),
    ]

    return legitarsasag, foglalasok
