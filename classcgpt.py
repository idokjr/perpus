class Buku:
    def __init__(self, judul, pengarang, tersedia=True):
        self.judul = judul
        self.pengarang = pengarang
        self.tersedia = tersedia

class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []
        self.anggota = []
        self.buku_dipinjam = {}

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tambah_anggota(self, anggota):
        self.anggota.append(anggota)

    def pinjam_buku(self, id_anggota, judul_buku):
        for buku in self.daftar_buku:
            if buku.judul == judul_buku and buku.tersedia:
                for anggota in self.anggota:
                    if anggota.id_anggota == id_anggota:
                        buku.tersedia = False
                        self.buku_dipinjam[buku.judul] = anggota.nama
                        print(f"{buku.judul} berhasil dipinjam oleh {anggota.nama}")
                        return
        print("Buku tidak tersedia atau ID anggota tidak valid.")

    def kembalikan_buku(self, judul_buku):
        if judul_buku in self.buku_dipinjam:
            self.daftar_buku.append(Buku(judul_buku, ""))
            del self.buku_dipinjam[judul_buku]
            print(f"Buku {judul_buku} berhasil dikembalikan.")
        else:
            print("Buku tidak sedang dipinjam.")

    def tampilkan_daftar_buku(self):
        print("Daftar Buku:")
        for buku in self.daftar_buku:
            ketersediaan = "Tersedia" if buku.tersedia else "Dipinjam"
            print(f"{buku.judul} oleh {buku.pengarang} - {ketersediaan}")

    def tampilkan_daftar_anggota(self):
        print("Daftar Anggota:")
        for anggota in self.anggota:
            print(f"{anggota.nama} (ID: {anggota.id_anggota})")

    def tampilkan_buku_dipinjam(self):
        print("Buku yang sedang dipinjam:")
        for judul_buku, nama_anggota in self.buku_dipinjam.items():
            print(f"{judul_buku} dipinjam oleh {nama_anggota}")


def main():
    perpustakaan = Perpustakaan()

    # Tambahkan beberapa buku dan anggota
    perpustakaan.tambah_buku(Buku("siksa Neraka", "M.Arif"))
    perpustakaan.tambah_buku(Buku("langit", "Ryan F."))
    perpustakaan.tambah_buku(Buku("air dan tanah", "supratman"))
    
    perpustakaan.tambah_anggota(Anggota("peng", 90901))
    perpustakaan.tambah_anggota(Anggota("idok", 12345))
    perpustakaan.tambah_anggota(Anggota("marta", 54321))

    while True:
        print("\n=== Menu ===")
        print("1. Daftar Buku")
        print("2. Daftar Anggota")
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        print("5. Daftar Buku yang Sedang Dipinjam")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")
        print("\n")

        if pilihan == '1':
            perpustakaan.tampilkan_daftar_buku()
        elif pilihan == '2':
            perpustakaan.tampilkan_daftar_anggota()
        elif pilihan == '3':
            id_anggota = int(input("Masukkan ID Anggota: "))
            judul_buku = input("Masukkan Judul Buku yang Ingin Dipinjam: ")
            perpustakaan.pinjam_buku(id_anggota, judul_buku)
        elif pilihan == '4':
            judul_buku = input("Masukkan Judul Buku yang Ingin Dikembalikan: ")
            perpustakaan.kembalikan_buku(judul_buku)
        elif pilihan == '5':
            perpustakaan.tampilkan_buku_dipinjam()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan layanan perpustakaan.")
            break
        else:
            print("Menu tidak valid. Silakan pilih menu yang benar.")


if __name__ == "__main__":
    main()
