def jumlahkan_semua(*angka):
    """Menjumlahkan sekumpulan angka menggunakan *args"""
    total = 0
    for n in angka:
        total += n
    return total

if __name__ == "__main__":
    hasil_1 = jumlahkan_semua(1, 2, 3)
    hasil_2 = jumlahkan_semua(5, 10, 15, 20, 25)
    
    print(f"Jumlah dari (1, 2, 3) = {hasil_1}")
    print(f"Jumlah dari (5, 10, 15, 20, 25) = {hasil_2}")