print("=== PROGRAM DERET ANGKA ===")

# Menampilkan semua bilangan ganjil
# dari 1 hingga batas yang ditentukan

BATAS_ATAS = 10


def adalah_ganjil(angka):
    return angka % 2 != 0


def tampilkan_angka_ganjil(batas):
    print("=== PROGRAM DERET ANGKA ===")
    for angka in range(1, batas + 1):
        if adalah_ganjil(angka):
            print("Angka ganjil:", angka)


tampilkan_angka_ganjil(BATAS_ATAS)

# Selesai