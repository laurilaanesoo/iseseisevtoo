#Iseseisev töö
#02.03.2022
#Lauri Laanesoo

#Tuleb sisestada sõna, mida teha salakeeleks
salakeel = input("Sisesta sõna, mida tahad teha salakeeleks: ")
#Kasutab for funktsiooni, et tekitada suvalisi tähti
for i in salakeel:
    kiri = (chr(ord(i) + 5))
    print(kiri,end='')
#Väljastab sisestatud sõnumi salakeeles
print(f"\nSisestatud Sõnum::{salakeel}")

#Tõlgib soovitud sõna 
tolkimine = input("Sisesta sõna, mida tahad tõlkida: " )
tolkimine = tolkimine.lower().replace(" ", "")
for i in tolkimine:
    kiri = (chr(ord(i) - 5))
    print(kiri,end='')
#Väljastab sisestatud sõnumi tavatähtedega
print(f"\nSisestatud sõnum: {tolkimine}")

