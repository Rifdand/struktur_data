#membuat program kalkulator sederhana
print("===kalkulator sederhana===")
print(" masukkan dua angka dan pilih operasi (+ : * -)")

operasi = input("masukkan operasi ( + : * - ):")
angka1 = float(input("masukkan angka pertama:"))
angka2 = float(input("masukkan angka kedua:"))

if operasi == "+":
    final = angka1 + angka2
    print(final)
elif operasi == "-":
    final = angka1 - angka2
    print(final)
elif operasi == "*":
    final = angka1 * angka2
    print(final)
else:
    final = angka1 / angka2
    print(final)