import math
if __name__ == '__main__':
    
    hari = 485

    thn = hari // 360
    jmlHari = hari % 360

    bulan = jmlHari // 30
    jmlHari = jmlHari % 30

    minggu = jmlHari // 7
    jmlHari = jmlHari % 7

    print(thn," tahun, ",bulan," bulan, ",minggu," minggu, ", jmlHari," hari")

    