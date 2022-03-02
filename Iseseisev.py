#Iseseisev töö
#02.03.2022
#Lauri Laanesoo



sisend = int(input("Kas soovid salakeelt luua või tõlkida? [1,2]:"))

if sisend == 1:
    salakeel = input("Sisesta sõna, mida tahad teha salakeeleks: ")
    encMessage = rsa.encrypt(message.encode(),publicKey)
    print(encMessage)
else:
    tolkimine = input("Sisesta sõna, mida tahad tõlkida: " )
    decMessage = rsa.decrypt(encMessage, privateKey).decode()
    
    tahestik="abcdefghijklmnopqrstuvwxyz"
sonum = input("Sisesta sõna, mida tahad krüpteerida")
krupt,dekrupt="",""
voti = 5

for taht in sonum:
    uus = (tahestik.find(taht)+voti)%len(tahestik)
    krupt+=tahestik[uus]
    
for taht in krupt:
    uus = (tahestik.find(taht)-voti)%len(tahestik)
    dekrupt+=tahestik[uus]
    
print("Sõnum:",krupt)