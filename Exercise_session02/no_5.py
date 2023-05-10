import math
if __name__ == '__main__': 
    A = 60
    B = 40
    pukulJalan = 9
    jarak= 120

    konversiJam = jarak/(A+B)
    konversiMenit = (konversiJam*60)

    jam = math.floor(konversiJam)
    menit = konversiMenit - 60

    jamTabrakan = jam + pukulJalan

    print("Mobil A dan B bertabrakan pada pukul jam", jamTabrakan,":", int(menit))
    