# utilitas_matematika.py

def kuadrat(x):
    """Mengembalikan nilai kuadrat dari x"""
    return x ** 2

def faktorial(n):
    """Menghitung nilai faktorial secara rekursif"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)