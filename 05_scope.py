pesan = "Halo dari Global"

def contoh_scope():
    # Variabel Lokal
    pesan = "Halo dari Lokal"
    print("Di dalam fungsi:", pesan)

def ubah_global():
    global pesan
    pesan = "Pesan Global telah diubah!"

if __name__ == "__main__":
    print("Sebelum fungsi dipanggil:", pesan)
    contoh_scope()
    print("Setelah fungsi dipanggil (pesan global tetap):", pesan)
    
    ubah_global()
    print("Setelah menggunakan keyword global:", pesan)