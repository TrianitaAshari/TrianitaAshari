"""
Cek nilai Menggunakan Loop 
" Loop cek penilaian mahasiswa
" loop run program (ok)
"""
#cek penilaian mahasiswa
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print("***********************************")
    print("     CEK PENILAIAN MAHASISWA       ")
    print("***********************************")
    n = input("Masukan nilai = ")
    u = int(n)
    if u>=91:
        nilai = "A"
    elif u>=81:
        nilai = "B"
    elif u>=71:
        nilai = "C"
    else:
        nilai= "D"
    
    
    print (nilai)    

    ulangprog = input(">> ulang program ? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break
        