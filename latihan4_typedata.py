#jumlah barang
beras = 5#int(input("Jumlah beras : "))
kecap   = 5#int(input("Jumlah kecap   : "))
telor  = 5#int(input("Jumlah telor  : "))
cabai  = 5#int(input("Jumlah cabai  : "))
bumbu = 5#int(input("Jumlah bumbu  : "))
minyak  = 5#int(input("Jumlah minyak   : "))

#jumlah
j_beras = 10000*beras
j_kecap = 2000*kecap
j_telor = 2500*telor
j_cabai = 3000*cabai
j_bumbu = 8000*bumbu racik
j_minyak = 10000*minyak

#belanja
belonjo = (j_beras+j_kecap+j_telor+j_cabai+j_bumbu+j_minyak)

#diskon
if belonjo > 100000:
  diskon = belonjo*0.5
else:
  diskon = 0 
f_diskon = f"{diskon:.2f}".rstrip("0").rstrip(".")

#total rego
rego = belonjo-diskon
f_rego = f"{rego:.2f}".rstrip("0").rstrip(".")

#tampilane
print ("        TOKO_RIFQI/10/(081)30303030     ")
print ("")
print ("---------------------------------------------")
import datetime
waktu = datetime.datetime.now()
f_waktu = waktu.strftime("%Y-%m-%d %H:%M")
print(f_waktu,"               12042/ALL/02")
print ("---------------------------------------------")
print ("")
print ("No | NamaProduk  | Qty |  Harga   | Jumlah ")
print ("")
print ("1. beras         ",beras,"   Rp 10.000 ","","Rp",j_beras)
print ("2. kecap           ",kecap,"   Rp 2.000 ","","Rp",j_kecap)
print ("3. telor          ",telor,"   Rp 2.500"," ","Rp",j_telor)
print ("4. cabai          ",cabai,"   Rp 5.000","","Rp",j_cabai)
print ("5. bumbu         ",bumbu,"   Rp 8.000"," ","Rp",j_bumbu)
print ("6. minyak          ",minyak,"   Rp 10.000"," ","Rp",j_minyak)
print ("                   --------------------------")
print ("                   Total Belanja : Rp",belanja)
print ("                   Diskon        : Rp",f_diskon)
print ("                   --------------------------",)
print ("")
print ("                   Total Harga   : Rp",f_rego)

#bayar
bayar = int(input("                   Bayar         : Rp "))
while bayar < harga:
    print("uang anda kurang'")
    bayar = int(input("                   Bayar Ulang   : Rp "))
  
#kembali
kembalian = bayar-harga
f_sosok = f"{sosok:.2f}".rstrip("0").rstrip(".")

print ("                   Kembalian     : Rp",f_kembalian)
print ("")
print ("")
print ("")
print ("             TERIMAKASIH ' ")z
