def hitung_luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang dan mengembalikan nilainya"""
    luas = panjang * lebar
    return luas

if __name__ == "__main__":
    p = 10
    l = 5
    hasil = hitung_luas_persegi_panjang(p, l)
    print(f"Panjang: {p}, Lebar: {l}")
    print(f"Luas Persegi Panjang adalah: {hasil}")