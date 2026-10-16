def sapa_halo():
    """Fungsi sederhana tanpa parameter"""
    print("Halo! Selamat datang di belajar fungsi Python.")

def sapa_nama(nama, waktu="Pagi"):
    """Fungsi dengan parameter wajib dan parameter default"""
    print(f"Halo, {nama}! Selamat {waktu}.")

if __name__ == "__main__":
    sapa_halo()
    sapa_nama("Budi")
    sapa_nama("Siti", "Malam")