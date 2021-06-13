"""
Cek golongan Usia Menggunakan Loop 
" Loop cek tingkatan usia
" loop run program (ok)
"""
#cek golongan usia
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print("**********************")
    print("cek golongan usia")
    print("**********************")
    #cek tingkatan usia
    n = input ("masukan usia = ")
    u = int(n)
    if int(u)>60:
        status = "lansia"
    elif int(u)>=35:
        status = "dewasa"
    elif int(u)>=18:
        status = "pemuda"
    elif int(u)>=15:
        status = "remaja" 
    else:
        status = "anak-anak"
        
    print (status)  

    ulangprog = input(">> ulang program ? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break