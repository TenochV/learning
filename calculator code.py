texto = input('Dame un número:')
popo = input('Dame otro número:')

numero = int(texto)
pipi = int(popo)
if (numero < pipi):
    print('El número', numero, 'es menor que', pipi)
elif  (numero > pipi):
    print('El' , numero, 'es mayor que' , pipi)
else:
    print('El número ' , numero, 'igual a' , pipi)
