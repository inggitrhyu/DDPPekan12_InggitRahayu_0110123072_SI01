class Gempa:
    #variabel
    lokasi = ''
    skala = 0

    #konstra
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    #method
    def dampak(self):
        if self.skala < 2:
            return "Dampak gempa tidak berasa."
        elif 2 <= self.skala < 4:
            return "Dampak gempa bangunan retak-retak."
        elif 4 <= self.skala < 6:
            return "Dampak gempa bangunan roboh."
        elif self.skala >= 6:
            return "Dampak gempa bangunan roboh dan berpotensi tsunami."
    

    def cetak(self):
        print(
            '\n================',
            '\nlokasi gempa\t:', self.lokasi,
             '\nskala gempa\t:', self.skala,
        )


