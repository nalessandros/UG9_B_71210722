def balikNama():
    #input
    namaKamu = input("Nama : ")
    ttlKamu = input("Tempat tanggal lahir : ")

    #proses
    balik = namaKamu.split()
    bbb = ""
    ccc = ""
    aa = ''.join(balik[-1])
    bb = ' '.join(balik[:-1])

    #cetak layar
    print("Haloo! " + aa + ", " + bb)
    print("Anda lahir di " + ttlKamu)

balikNama()
