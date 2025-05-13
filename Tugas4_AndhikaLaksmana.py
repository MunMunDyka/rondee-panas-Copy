print("Selamat datang di program tugas Python!")

nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
print(f"Halo, {nama}! Tahun depan kamu berumur {umur + 1} tahun.\n")

mahasiswa = ["Andhika Laksmana", "Vinsensius", "Syahana", "Nabilah", "Nandayo"]

while True:
    cari_nama = input("Masukkan nama mahasiswa yang ingin dicari: ")
    if cari_nama in mahasiswa:
        print(f"{cari_nama} ada dalam daftar mahasiswa.")
        break
    else:
        print("Nama tidak ada dalam daftar. Silakan coba lagi.\n")

print("\nDaftar nama mahasiswa:")
for i, m in enumerate(mahasiswa, 1):
    print(f"{i}. {m}")

if cari_nama in mahasiswa:
    print(f"\n{cari_nama} ada di nama daftar mahasiswa.\n")

data_mahasiswa = {
    "220101": "Andhika Laksmana",
    "220102": "Vinsensius",
    "220103": "Syahana",
    "220104": "Nabilah",
    "220105": "Nandayo"
}
print("\nData Mahasiswa:")
for nim, nama in data_mahasiswa.items():
    print(f"NIM: {nim}, Nama: {nama}")

# CIHUYYYYY
angka = int(input("\nMasukkan sebuah angka: "))
if angka % 2 == 0:
    print(f"Angka {angka} adalah genap.")
else:
    print(f"Angka {angka} adalah ganjil.")
