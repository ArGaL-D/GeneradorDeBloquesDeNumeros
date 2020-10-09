import os
import sys 
# Tamaño de la terminal(rectángulo), en realidad la base(fila o línea) hace referencia al total
# máximo de caracteres permitidos por línea en la terminal
altura, base = os.popen('stty size', 'r').read().split()

linea_A         = ''
linea_B         = ''
linea_dato      = ''
ancho                    = int(base)
total_caracteres_Linea   = int(base)
total_caracteres_Fila_A  = 0
cantidad_bloques         = 0

# Un argumento en python dentro de la terminal
if  len(sys.argv) == 2:  
        try:
            cantidad_bloques = int(sys.argv[1])
        except:
            print(chr(27)+"[5;31m"+'\n ->',chr(27)+"[0m"+'Ingresar SOLO numeros')

else:
        print(chr(27)+"[1;33m"+'\n -> Tambien puedes agregar un argumento --'+chr(27)+"[0m"+'\n -> bloques.py [1 - 99,999]')
        cantidad_bloques = 0

# Generar el número total de bloques (cuadros)
while True:

    if cantidad_bloques > 99999 or cantidad_bloques < 1 :
        print(chr(27)+"[5;31m"+'\n ->',chr(27)+"[0m"   +"Cantidad maxima permitida: 1 - 99,999\n")
        
        try:
            cantidad_bloques = int(input(chr(27)+"[2;38m"+' Cantidad:'+chr(27)+"[0m"' '))
        except:
            print(chr(27)+"[5;31m"+'\n ->',chr(27)+"[0m"+'Ingresar SOLO numeros')
    else:
        for var in range(cantidad_bloques):
            var +=1

            if   var <=  9:
                linea_A     +=  ' ++++++'     # Fila A
                linea_dato  += f' +  {var} +' # Fila Dato
                linea_B     +=  ' ++++++'     # Fila B
            elif var <= 99:
                linea_A     +=  ' ++++++'     
                linea_dato  += f' + {var} +'
                linea_B     +=  ' ++++++'     
            elif var <= 999:
                linea_A     +=  ' ++++++'     
                linea_dato  += f' + {var}+'
                linea_B     +=  ' ++++++'     
            elif var <=9999: 
                linea_A     +=  ' ++++++'     
                linea_dato  += f' +{var}+'
                linea_B     +=  ' ++++++'
            else:

                linea_A     +=  '       +-----+'        
                linea_dato  += f'       +{var}+'
                linea_B     +=  '       +-----+'
        break

# Cada línea de bloque contiene 6 caracteres -> '+' y un espacio = 7 caracteres, es decir, para que los bloques se ajusten al 
# tamaño de la terminal; el ancho (total de caracteres por línea) debe ser divido por 7, si su residuo es diferente de '0' 
# significa que el ancho no es el correcto.
while ancho%7 != 0:
    ancho -=1
    total_caracteres_Linea -=1

# Imprimir los bloques de números
# Número de filas
numero_filas = 0
for var in range(cantidad_bloques):

    if total_caracteres_Fila_A != len(linea_A):
        numero_filas +=1
        print(   linea_A[ancho-total_caracteres_Linea: ancho] )
        print(linea_dato[ancho-total_caracteres_Linea: ancho] )
        print(   linea_B[ancho-total_caracteres_Linea: ancho],'\n' )
        
        # Se suma el total de caracteres por linea (Fila A)
        total_caracteres_Fila_A += len(linea_A[ancho-total_caracteres_Linea: ancho] )
        
        ancho += total_caracteres_Linea
    else:
        break

print(' Filas (bloques): ',numero_filas)