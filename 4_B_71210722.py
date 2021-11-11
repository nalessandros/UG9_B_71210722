def diskonNich():
    #input
    sepeda = int(25000)
    kipasAngin = int(6000)
    helmRossi = int(8000)

    #proses
    discSepeda = 10/100
    discKipas = 55/100
    discHelm = 77/100

    #cetak layar
    print("=======GEBYAR DISKON=======")
    print("=======MASUKKAN JUMLAH BARANG YANG DIPESAN=======")

    #input
    aa = int(input("KIPAS ANGIN DISKON 10%  Rp 25.000,00    : "))
    bb = int(input("SEPEDA DISKON 55%       Rp 6.000,00    : "))
    cc = int(input("HELM ROSSI DISKON 77%   Rp 8.000,00    : "))

    #proses
    aaa = aa * sepeda * discSepeda
    bbb = bb * kipasAngin * discKipas
    ccc = cc * helmRossi * discHelm

    #cetak layar
    print("=======TOTAL=======")
    print("TOTAL KIPAS ANGIN    : Rp ", aaa)
    print("TOTAL KIPAS ANGIN    : Rp ", bbb)
    print("TOTAL KIPAS ANGIN    : Rp ", ccc)
    print("jumlah total diskon yang didapat adalah Rp ", aaa + bbb + ccc)
diskonNich()
