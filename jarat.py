from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def info(self):
        pass

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 10000)

    def info(self):
        return f"Belföldi: {self.jaratszam} -> {self.celallomas} | Ár: {self.jegyar} Ft"

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, 30000)

    def info(self):
        return f"Nemzetközi: {self.jaratszam} -> {self.celallomas} | Ár: {self.jegyar} Ft"