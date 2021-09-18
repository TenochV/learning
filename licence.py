texto = input('Dame un nombre:')
popo = input('Dame una direccion:')
s = input('Dame una edad:')

kaka = int(s)

if (kaka>=18):
    print('Licencia de conducir')
    print(texto)
    print(s,'años')
    print(popo)

elif (kaka>=16):
    print('permiso de conducir')
    print(texto)
    print(s,'años')
    print(popo)

else: 
    print('no tienes edad para conducir perdedora')
   
