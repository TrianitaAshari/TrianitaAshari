"""
Cek nilai kelulusan Menggunakan Loop 
" loop run program (ok)
"""
#cek kelulusan jika, jika nilai > 60 maka status lulus
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print("****************************")
    print("       CEK KELULUSAN        ")
    print("****************************")
    #setiap value yang diinputkan, secara deafult bertipe data STRING
    n = input ("masukan nilai = ")
    u = int(n)
    #cek nilai
    if int(u)>=60:
        status = "LULUS"
    else:
        status = "ULANG"
        
        
    print (status)   

    ulangprog = input(">> ulang program ? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break