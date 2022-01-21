#belajar menerapkan islower,isupper,lower,dan upper ke dlm contoh kasus

print("kasus".center(25,"="))

string = 'Yuhui MERRY apa kaBaR? SEmoga harimu SeNIN terus haHAHA'
newstring = ''
huruf1 = 0
huruf2 = 0
huruf3 = 0

for i in string:
    if (i.isupper()) == True: 
        huruf1+= 1
        newstring+=(i.lower())
    elif (i.islower()) == True:
        huruf2+= 1
        newstring+=(i.upper())
    elif (i.isspace()) == True:
        huruf3+= 1
        newstring+= i

print("hasil string:")
print("hurufbesar -",huruf1)
print("hurufkecil -",huruf2)
print("spasi -",huruf3)

print("setelah mengubah kasus :")
print(newstring)

#fungsi islower untuk memeriksa apakah argumen berisi karakter huruf kecil
#jika benar huruf kecil maka hasilnya "True" jika tidak hasilnya akan "False"
#contoh
print("islower".center(25,"="))

huruf = "abcdefgh"
print(huruf.islower())
huruf = "ABCDEFGH"
print(huruf.islower())

print("isupper".center(25,"="))
#fungsi isupper untuk memeriksa apakah argumen berisi karakter huruf besar
#jika benar huruf besar maka hasilnya "True" jika tidak hasilnya akan "False"
#contoh
huruf = "abcdefgh"
print(huruf.isupper())
huruf = "ABCDEFGH"
print(huruf.isupper())
