def hitung_statistik(daftar_angka):
    """Menghitung nilai minimum, maksimum, dan rata-rata dari sebuah list"""
    if not daftar_angka:
        return None, None, None
        
    minimum = min(daftar_angka)
    maksimum = max(daftar_angka)
    rata_rata = sum(daftar_angka) / len(daftar_angka)
    
    return minimum, maksimum, rata_rata

if __name__ == "__main__":
    nilai = [80, 90, 75, 85, 95]
    min_val, max_val, avg_val = hitung_statistik(nilai)
    
    print(f"Data Nilai: {nilai}")
    print(f"Nilai Minimum : {min_val}")
    print(f"Nilai Maksimum: {max_val}")
    print(f"Rata-rata     : {avg_val}")