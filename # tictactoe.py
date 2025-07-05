# tictactoe.py

def cetak_papan(papan):
    """Fungsi untuk mencetak papan Tic-Tac-Toe."""
    print("\n" + " | ".join(papan[0]))
    print("---|---|---")
    print(" | ".join(papan[1]))
    print("---|---|---")
    print(" | ".join(papan[2]) + "\n")

def cek_pemenang(papan, pemain):
    """Fungsi untuk memeriksa apakah ada pemenang."""
    # Cek baris horizontal
    for baris in papan:
        if all(sel == pemain for sel in baris):
            return True
    
    # Cek kolom vertikal
    for kolom in range(3):
        if all(papan[baris][kolom] == pemain for baris in range(3)):
            return True

    # Cek diagonal
    if all(papan[i][i] == pemain for i in range(3)):
        return True
    if all(papan[i][2-i] == pemain for i in range(3)):
        return True
        
    return False

def cek_seri(papan):
    """Fungsi untuk memeriksa apakah permainan seri."""
    for baris in papan:
        for sel in baris:
            if sel.isdigit(): # Jika masih ada angka, papan belum penuh
                return False
    return True

def main():
    """Fungsi utama untuk menjalankan permainan."""
    # Inisialisasi papan dengan angka 1-9 sebagai penanda posisi
    papan = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
             
    pemain_sekarang = 'X'
    game_berjalan = True

    print("Selamat Datang di Game Tic-Tac-Toe!")

    while game_berjalan:
        cetak_papan(papan)
        print(f"Giliran Pemain '{pemain_sekarang}'. Pilih nomor posisi (1-9):")

        # Loop untuk mendapatkan input yang valid
        while True:
            try:
                pilihan = input("Masukkan pilihan Anda: ")
                if not pilihan.isdigit() or not 1 <= int(pilihan) <= 9:
                    print("Input tidak valid. Harap masukkan angka antara 1 dan 9.")
                    continue

                pilihan = int(pilihan)
                
                # Konversi pilihan (1-9) ke koordinat papan (baris, kolom)
                baris = (pilihan - 1) // 3
                kolom = (pilihan - 1) % 3

                if papan[baris][kolom] in ['X', 'O']:
                    print("Posisi ini sudah terisi. Silakan pilih posisi lain.")
                else:
                    papan[baris][kolom] = pemain_sekarang
                    break # Keluar dari loop input jika pilihan valid
            except ValueError:
                print("Input tidak valid. Harap masukkan sebuah angka.")

        # Cek apakah ada pemenang setelah langkah saat ini
        if cek_pemenang(papan, pemain_sekarang):
            cetak_papan(papan)
            print(f"Selamat! Pemain '{pemain_sekarang}' menang!")
            game_berjalan = False
        # Cek apakah permainan seri
        elif cek_seri(papan):
            cetak_papan(papan)
            print("Permainan berakhir seri!")
            game_berjalan = False
        else:
            # Ganti giliran pemain
            pemain_sekarang = 'O' if pemain_sekarang == 'X' else 'X'

    print("Terima kasih sudah bermain!")

# Menjalankan fungsi utama saat script dieksekusi
if __name__ == "__main__":
    main()