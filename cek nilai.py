"""
Cek nilai Menggunakan Loop 
" Loop cek inputan range bilangan bulat harus >0-100
" loop run program (ok)
"""
#cek nilai
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print("**********************")
    print("     CEK NILAI        ")
    print("**********************")
    u=1
    while int(u)>0 and int(u)<=100:
        u = input(">> Masukan Nilai = ")
        #cek batasan inputan bilangan bulat 0-100
        if int(u)>0 and int(u)<=100:
            if int(u)>=80:
                status="BAIK SEKALI"
            elif int(u)>=65:
                 status="BAIK" 
            elif int(u)>=55:
                 status="CUKUP"   
            elif int(u)>=40:
                 status="KURANG"   
            else:
                status="KURANG SEKALI"
            print  (status)  

            ulangprog = input(">> ulang program ? y/t = ")  
            if ulangprog=="t" or ulangprog=="T":
                break 
        else:
            pesan=">>> masukan bilangan bulat antara 0-100 saja" 
            print(pesan)  
            break          




    

