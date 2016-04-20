print('hello')
annee = int(input('l annee: '))
print(annee)
if annee % 4 !=0:
    print('not bi')
elif  annee % 400 == 0 and annee % 100 ==0 :
    print('bissextile!')
else : print('not bi')
# cest fini
print('end')
