Pilihan = "ya"
while Pilihan == "ya":
  print("""
 ========================================

            Adivah Coffe Shop
        Menu Makanan Dan Minuman

 ========================================

                        Ice         Hot
  A.Latte Coffe    : Rp 25.000  Rp 22.000
  B.Machiato Coffe : Rp 26.000  Rp 23.000
  C.Americano Coffe: Rp 23.000  Rp 20.000 
  D.Cappucino coffe: Rp 25.000  Rp.23.000
  E.Moccacino Coffe: Rp 24.000  Rp.21.000

 =========================================
 """)
  import time
  tanggal=time.strftime("%d-%m-%y %H:%M:%S")
  nama=str(input("masukan nama anda ="))
  alamat=str(input("masukan alamat anda ="))
  noTelpon=str(input("masukan nomer telepon anda ="))
  Pesan=str(input("masukkan Menu Sesuai Abjad Dan Pilih ="))
  Jumlah_Pesanan=int(input("Masukan Jumlah Pesanan="))
  if Pesan=="a":
    Nama="Latte Coffe"
    varian=str(input("Ice/Hot ="))
    if varian=="ice":
      harga=(25000)
      hargaTotal=int(25000*Jumlah_Pesanan)
    else : 
      harga=(22000)
      hargaTotal=int(22000*Jumlah_Pesanan)

  elif Pesan=="b":
    Nama="Machiato Coffe"
    varian=str(input("Ice/Hot ="))
    if varian=="ice":
      harga=(26000)
      hargaTotal=int(26000*Jumlah_Pesanan)
    else :
      harga(23000)  
      hargaTotal=int(23000*Jumlah_Pesanan)
 
  elif Pesan=="c":
    Nama="Americano Coffe"
    varian=str(input("Ice/Hot ="))
    if varian=="ice":
      harga=(23000)  
      hargaTotal=int(23000*Jumlah_Pesanan)
    else :
      harga=(20000)  
      hargaTotal=int(20000*Jumlah_Pesanan)
 
  elif Pesan=="d":
    Nama="Cappucino Coffe"
    varian=str(input("Ice/Hot ="))
    if varian=="ice":
      harga=(25000)  
      hargaTotal=int(25000*Jumlah_Pesanan)
    else :
      harga=(23000)
      hargaTotal=int(23000*Jumlah_Pesanan)
  elif Pesan=="e":
    Nama="Moccacino Coffe"
    varian=str(input("Ice/Hot ="))
    if varian=="ice":
      harga=(24000)  
      hargaTotal=int(24000*Jumlah_Pesanan)
    else :
      harga=(21000)  
      hargaTotal=int(21000*Jumlah_Pesanan)
  else:
    Pesan = "-"
    Nama= "-"
    varian= "-"
    harga= "-"
    pilihan=input("menu tidak tersedia,silahkan pilih kembali ya/tidak =")
  print("---------------------------------")
  print("Adivah Coffe")
  print("---------------------------------")
  print("Nama         :",nama)
  print("Alamat       :",alamat)
  print("No.telp      :",noTelpon)
  print("Tanggal      :",tanggal)
  print("Menu         :",Nama)
  print("Varian       :",varian)
  print("Jumlah Pesan :", Jumlah_Pesanan)
  print("Harga satuan :",harga)
  print("Jumlah Bayar :", hargaTotal)
  print("---------------------------------")
  pilihan=input("apakah anda ingin order kembali ya/tidak =") 