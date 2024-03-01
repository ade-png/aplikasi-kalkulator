class kalkulator:
    def tambah(self,a,b):
        hasil = a+b
        print (f"Hasil dari {a}+{b} adalah {hasil} ")
    def kurang(self,a,b):
        hasil = a-b
        print (f"hasil dari {a}-{b} adalah {hasil} ")
    def kali(self,a,b):
        hasil = a*b
        print (f"hasil dari {a}*{b} adalah {hasil} ")
    def bagi(self,a,b):
        if b ==0:
            print("tidak dapat dibagi 0")
        else:
            hasil = a/b
            print (f"hasil dari {a}/{b} adalah {hasil} ")
        
cal = kalkulator()
while True:
    print(" aplikasi kalkulator sederhana ")
    print("=============================")
    print("1. kalkulator")
    print("2. keluar")
    s1 = int(input("masukan pilihan 1/2: "))
    if s1 ==1:
        a = float(input("masukan angka pertama: "))
        b = float(input("masukan angka kedua: "))
        print("metode operasi: ")
        print("1. pertambahan")
        print("2. pengurangan")
        print("3. perkalian")
        print("4. pembagian")
        o = str(input("masukan operasi: "))
        if o == '1' :
            cal.tambah(a,b)
        elif o =='2' :
            cal.kurang(a,b)
        elif o =='3' :
            cal.kali(a,b)
        elif o =='4' :
            cal.bagi(a,b)
        else:
            print("pilihan yang anda pilih tidak ada")
            
    elif s1 == 2:
             print("terima kasih")
             break