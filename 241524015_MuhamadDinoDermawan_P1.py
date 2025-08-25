# Nama:   Muhamad Dino Dermawan
# NIM:    241524015
# Kelas:  D4-2A
# Tgl:    19-08-2025
# Matkul: Aljabar Linear PR

import numpy as np

def analisis_matriks_final():
    """
    Program analisis matriks versi final.
    Implementasi pengecekan matriks segitiga atas dan bawah telah
    diverifikasi sesuai dengan definisi formal matematis.
    """
    
    # --- 1. Input Matriks m x n ---
    print("--- Input Matriks m x n ---")
    try:
        m = int(input("Masukkan jumlah baris (m): "))
        n = int(input("Masukkan jumlah kolom (n): "))
        if m <= 0 or n <= 0:
            print("Dimensi matriks harus bilangan bulat positif.")
            return
    except ValueError:
        print("Input tidak valid. Masukkan angka untuk dimensi.")
        return

    matriks_list = []
    print(f"Masukkan elemen-elemen untuk matriks {m}x{n}:")
    for i in range(m):
        baris = []
        for j in range(n):
            while True:
                try:
                    elemen = float(input(f"  Masukkan elemen baris {i+1}, kolom {j+1}: "))
                    baris.append(elemen)
                    break
                except ValueError:
                    print("Input tidak valid. Masukkan sebuah angka.")
        matriks_list.append(baris)
    
    matriks = np.array(matriks_list)
        
    # --- Tampilan Matriks ---
    print("\n--- Tampilan Matriks ---")
    print("Matriks Lengkap:\n", matriks)
    print("\nNilai Diagonal Utama:\n", np.diag(matriks))
    print("\nBentuk Segitiga Atas (representasi):\n", np.triu(matriks))
    print("\nBentuk Segitiga Bawah (representasi):\n", np.tril(matriks))
    
    # --- Output: Nilai elemen matriks baris ke-m dan kolom ke-n ---
    print("\n--- Nilai Elemen Spesifik ---")
    try:
        baris_spesifik = int(input("Masukkan nomor baris yang ingin dilihat: ")) - 1
        kolom_spesifik = int(input("Masukkan nomor kolom yang ingin dilihat: ")) - 1
        
        if 0 <= baris_spesifik < m and 0 <= kolom_spesifik < n:
            nilai_elemen = matriks[baris_spesifik, kolom_spesifik]
            print(f"Nilai elemen baris {baris_spesifik+1}, kolom {kolom_spesifik+1}: {nilai_elemen}")
        else:
            print("Indeks baris/kolom di luar range matriks!")
    except ValueError:
        print("Input tidak valid untuk baris/kolom spesifik.")
    
    # --- Klasifikasi Jenis Matriks ---
    print("\n\n--- B. Klasifikasi Jenis Matriks (Pengecekan Syarat) ---")

    # 5. Cek Matriks Nol
    print(f"Apakah merupakan Matriks Nol? -> {np.all(matriks == 0)}")
    
    # Pengecekan selanjutnya hanya berlaku untuk matriks persegi
    if m != n:
        print("\n   (Pengecekan Matriks Identitas, Diagonal, dan Segitiga dilewati")
        print("    karena matriks ini tidak persegi).")
    else:
        # 6. Cek Matriks Identitas
        is_identity = np.array_equal(matriks, np.identity(m))
        print(f"Apakah merupakan Matriks Identitas? -> {is_identity}")

        # 7. Cek Matriks Diagonal
        is_diagonal = np.array_equal(matriks, np.diag(np.diag(matriks)))
        print(f"Apakah merupakan Matriks Diagonal? -> {is_diagonal}")

        # 8. Cek Matriks Segitiga Atas
        is_upper_triangular = np.all(np.tril(matriks, k=-1) == 0)
        print(f"Apakah merupakan Matriks Segitiga Atas? -> {is_upper_triangular}")

        # 9. Cek Matriks Segitiga Bawah
        is_lower_triangular = np.all(np.triu(matriks, k=1) == 0)
        print(f"Apakah merupakan Matriks Segitiga Bawah? -> {is_lower_triangular}")

    # 10. Cek Matriks Sparse
    try:
        jumlah_nol = np.count_nonzero(matriks == 0)
        total_elemen = matriks.size
        is_sparse = (jumlah_nol / total_elemen) > 0.5
        print(f"Apakah merupakan Matriks Sparse (>50% elemen nol)? -> {is_sparse}")
    except ZeroDivisionError:
        print("Apakah merupakan Matriks Sparse (>50% elemen nol)? -> False (matriks kosong)")


# Menjalankan fungsi utama program
if __name__ == "__main__":
    analisis_matriks_final()