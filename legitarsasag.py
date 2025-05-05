class Legitarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def hozzaad_jarat(self, jarat):
        self.jaratok.append(jarat)

    def listaz_jaratok(self):
        return [jarat.info() for jarat in self.jaratok]

    def keres_jarat(self, jaratszam):
        return next((j for j in self.jaratok if j.jaratszam == jaratszam), None)