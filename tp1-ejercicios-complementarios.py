
# 1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero1 = 10
print(numero1)
# 10

# 2. No borres la variable número uno y crea una variable llamada "numero2" asignándole
# un número decimal de tu elección.
numero2 = 10.5
print(numero2)
# 10.5

# 3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".
suma = numero1 + numero2
print(suma)
# 20.5

# 4. Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para
# multiplicación y otra para división. Imprime estas variables.
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(suma)
print(resta)
print(multiplicacion)
print(division)
# 20.5
# -0.5
# 105.0
# 0.9523809523809523

# 5. Crea una variable llamada "nombre" y asígnale tu nombre como valor.
nombre = "Dave"
print(nombre)
# Dave

# 6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el
# precio de un artículo ficticio.
precio = 2000.20
print(precio)
# 2000.2

# 7. Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale
# un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le
# quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al
# 100% y el valor 0 al 0%.
descuento = 0.70
print(descuento)
# 0.7`

# 8. Ahora, intenta calcular el precio final aplicando el descuento al precio original y
# almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que
# aplicar la lógica de matemáticas
precio_final = precio * descuento
print("El articulo con decuento te queda en: ", precio_final)
# El articulo con decuento te queda en:  1400.1399999999999

# 9. Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu
# elección. Qué sea un string.
cadena = "Hola mundo"
print(cadena)
# Hola mundo

# 10. Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas
# a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de
# Python.
longitud = len(cadena)
print(longitud)
# 10

# 11. Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y
# conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo
# mismo.
precio = int(precio)
print(precio)
# 2000

# 12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas
# en una tercera variable llamada "nombre_completo", el nombre y el apellido con un
# espacio entre medio. Puedes usar libremente la forma de concatenación que quieras.
nombre = "Dave"
apellido = "Mustaine"
nombre_completo = nombre + " " + apellido
print(nombre_completo) 
# Dave Mustaine

# 13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.
edad = 20
edad+=5
edad-=10
print(edad) 
# 15

# 14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y
# centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3.
altura = 1.76
altura*=4
altura/=3
print(altura)
# 2.3466666666666667

# 15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después
# transfórmalo todo en minúsculas con algún método o función de Python.
nombre_mayus = "NAHUEL"
print(nombre_mayus.lower())
# nahuel

# 16. Por último, con la variable con el nombre en mayúsculas, aplica un método parecido
# para que se transforme todo en minúsculas excepto la primera letra.
print(nombre_mayus.title())
# Nahuel