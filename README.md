def calculate_total(apel_qty, jeruk_qty, anggur_qty):
    # Harga produk
    harga_apel = 10000
    harga_jeruk = 15000
    harga_anggur = 20000
    
    # Perhitungan subtotal untuk setiap produk
    subtotal_apel = apel_qty * harga_apel
    subtotal_jeruk = jeruk_qty * harga_jeruk
    subtotal_anggur = anggur_qty * harga_anggur
    
    # Tampilkan detail belanja
    print("\nDetail Belanja:")
    if apel_qty > 0:
        print(f"Apel  : {apel_qty} x {harga_apel} = {subtotal_apel}")
    if jeruk_qty > 0:
        print(f"Jeruk : {jeruk_qty} x {harga_jeruk} = {subtotal_jeruk}")
    if anggur_qty > 0:
        print(f"Anggur: {anggur_qty} x {harga_anggur} = {subtotal_anggur}")
    
    # Total belanja
    total = subtotal_apel + subtotal_jeruk + subtotal_anggur
    print(f"\nTotal: {total}")
    
    return total

def process_payment(total):
    while True:
        try:
            uang = int(input("\nMasukkan jumlah uang: "))
            
            # Jika uang kurang
            if uang < total:
                kurang = total - uang
                print(f"Uangnya kurang sebesar {kurang}")
            
            # Jika uang pas
            elif uang == total:
                print("Terimakasih")
                break
            
            # Jika uang lebih
            else:
                kembalian = uang - total
                print("Terimakasih")
                print(f"Uang kembali anda: {kembalian}")
                break
        
        except ValueError:
            print("Masukkan jumlah uang yang valid.")

# Fungsi utama
def main():
    try:
        # Input jumlah barang
        apel_qty = int(input("Masukkan Jumlah Apel: "))
        jeruk_qty = int(input("Masukkan Jumlah Jeruk: "))
        anggur_qty = int(input("Masukkan Jumlah Anggur: "))
        
        # Hitung total belanja
        total = calculate_total(apel_qty, jeruk_qty, anggur_qty)
        
        # Proses pembayaran
        process_payment(total)
    
    except ValueError:
        print("Masukkan jumlah yang valid.")

# Jalankan program
if __name__ == "__main__":
    main()
