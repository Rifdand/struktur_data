#kondisional statment
#if else dalam satu line 
# Program pengecekan hak akses
# Input hak akses
hak_akses = input("Masukkan hak akses Anda: ").lower()
if hak_akses == "admin":
    print("Full akses")
else:
    print("Akses denied")