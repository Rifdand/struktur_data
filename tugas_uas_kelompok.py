# TUGAS PROJECT UAS DENGAN LOOP MENU

print("##### Kelompok 1 #####")
print("Rifdan (24241107)")
print("Muammar hirsan (24241151)")

while True:
    print("\nDaftar Program")
    print("1. Meet1 (Tabel Kebenaran/Logika)")
    print("2. Meet2 (Operasi Logika)")
    print("3. Meet3-4 (Luas Segitiga & Gambar)")
    print("4. Meet5 (Kalkulator Sederhana)")
    print("5. Meet6 (Hak Akses)")
    print("6. Meet7 (Cek Password)")
    print("7. Meet8 (Manipulasi String)")
    print("8. Meet9-10 (Pemisah Domain)")
    print("9. Exit")

    pilihan = input("\nMasukkan nomor program yang ingin dijalankan: ")

    if pilihan == "1":
        print("\n=== Meet1: Tabel Kebenaran ===")
        a = 24
        b = 53

        hasil = a < b
        print(f"{a} < {b} = {hasil}")

        hasil = a > b
        print(f"{a} > {b} = {hasil}")

        hasil = a <= b
        print(f"{a} <= {b} = {hasil}")

        hasil = a != b
        print(f"{a} != {b} = {hasil}")

        hasil = not (a == b)
        print(f"not ({a} == {b}) = {hasil}")

    elif pilihan == "2":
        print("\n=== Meet2: Operasi Logika ===")
        x = True
        z = not x
        print("Nilai dari z =", z)

        print("\n********** AND ***********")
        x = True; y = True
        print(x, "and", y, "=", x and y)

        x = True; y = False
        print(x, "and", y, "=", x and y)

        x = False; y = True
        print(x, "and", y, "=", x and y)

        x = False; y = False
        print(x, "and", y, "=", x and y)

    elif pilihan == "3":
        print("\n=== Meet3-4: Luas Segitiga & Gambar ===")
        alas = int(input("Masukkan alas segitiga: "))
        tinggi = int(input("Masukkan tinggi segitiga: "))

        if alas > 0 and tinggi > 0:
            luas = 0.5 * alas * tinggi
            print(f"\nLuas segitiga adalah: {luas:.2f}\n")
            print("Gambar segitiga:")
            for i in range(1, tinggi + 1):
                print(' ' * (tinggi - i) + '*' * (2 * i - 1))
        else:
            print("Alas dan tinggi harus lebih dari 0!")

    elif pilihan == "4":
        print("\n=== Meet5: Kalkulator Sederhana ===")
        print("Masukkan dua angka dan pilih operasi (+, -, *)")
        operasi = input("Operasi (+, -, *): ")
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        if operasi == "+":
            hasil = angka1 + angka2
        elif operasi == "-":
            hasil = angka1 - angka2
        elif operasi == "*":
            hasil = angka1 * angka2
        else:
            hasil = "Operasi tidak valid"

        print("Hasil:", hasil)

    elif pilihan == "5":
        print("\n=== Meet6: Hak Akses ===")
        hak_akses = input("Masukkan hak akses Anda: ").lower()
        print("Full akses" if hak_akses == "admin" else "Akses denied")

    elif pilihan == "6":
        print("\n=== Meet7: Pengecekan Password ===")
        password = input("Masukkan password: ")

        if len(password) < 8:
            print("Karakter kurang")
        else:
            print("Karakter cukup")

    elif pilihan == "7":
        print("\n=== Meet8: Manipulasi String ===")
        number = "1234567890"
        print("a. Data terakhir:", number[-1])
        print("b. Data pertama:", number[0])
        print("c. Data ke-3 sampai ke-6:", number[2:6])

    elif pilihan == "8":
        print("\n=== Meet9-10: Pemisah Domain ===")
        domain = input("Masukkan nama domain anda (contoh: google.com): ")
        if "." in domain:
            nama, ekstensi = domain.split(".")
            print("Nama domain anda adalah =", nama)
            print("Nama yang anda gunakan adalah =", ekstensi)
        else:
            print("Domain tidak valid!")

    elif pilihan == "9":
        print("Program selesai. Terima kasih.")
        break

    else:
        print("Pilihan tidak valid.")
