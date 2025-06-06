
# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().

text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.

print("Hola" + " " + "Mundo")

# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.

text = "Esta es una lÃ­nea\nEsta es otra lÃ­nea"
print(text)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

name = "Brais"
surname = "Moure"
age = 37
print(f"Mi nombre es {name} {surname} y tengo {age} aÃ±os")

# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno.

palabra = "Python"
a, b, c, d, e, f = palabra
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un â€œsliceâ€ de la palabra â€œProgramaciÃ³nâ€ para obtener los caracteres desde la posiciÃ³n 3 hasta la 7.

text = "ProgramaciÃ³n"
text_slice = text[3:8]
print(text_slice)

# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.

text = "Python"
reversed_text = text[::-1]
print(reversed_text)

# 8. Convierte la cadena â€œaprendiendo pythonâ€ en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.

text = "aprendiendo python"
print(text.upper())

# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€ en la cadena â€œProgramaciÃ³n en Pythonâ€.

text = "ProgramaciÃ³n en Python"
print(text.count("n"))

# 10. Verifica si la cadena â€œ12345â€ es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.

text = "12345"
print(text.isnumeric())

