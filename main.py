#Variables 
PI = 3.14
area = 1 #Variable global
 
def run(radius) -> float:
    # TODO
    #Las variables declaradas en funciones son locales.
    global area
    area = PI * (radius ** 2)
    #El elevado al cuadrado se representa con 2
    #El doble ** es potencia, que sirve para los numeros elevados
    return area
#Programa principal



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

print("El area es: ", area)
