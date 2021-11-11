def volumeTabung():
    #input
    jari = int(input("Masukan jari-jari alas tabung : "))
    tinggi = int(input("Masukan tinggi tabung : "))
    phi = 22/7

    #proses
    volume = int((phi*(jari*jari))*tinggi)

    #cetak layar
    print("Volume tabung adalah " + "%.1f" % volume)
volumeTabung()
