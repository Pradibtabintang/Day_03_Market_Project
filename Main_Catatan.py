# Create price list
price_apple = 10000
price_orange = 15000
price_grape = 20000

# Create User Input
amount_apple = input("Masukan Jumlah apel: ")
amount_orange = input("Masukan Jumlah Jeruk: ")
amount_grape = input("Masukan Jumlah Anggur: ")

# Convert user input to integer
amount_apple = int(amount_apple)
amount_orange = int(amount_orange)
amount_grape = int(amount_grape)

# Calculate Price
price_apple_total = price_apple * amount_apple
price_orange_total = price_orange * amount_orange
price_grape_total = price_grape * amount_grape

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