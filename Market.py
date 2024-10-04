# Harga produk
harga_apel = 10000
harga_jeruk = 15000
harga_anggur = 20000

apel_qty = int(input ("Masukkan jumlah apel:"))
jeruk_qty = int(input ("Masukkan jumlah jeruk:"))
anggur_qty = int(input ("Masukkan jumlah anggur;"))

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

