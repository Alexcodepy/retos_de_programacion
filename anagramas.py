"""
Determina si dos palabras son anagramas.
Deben tener las mismas letras en la misma cantidad.
Si son idénticas o de distinta longitud, no lo son.
Imprime "Son anagramas" o "No son anagramas"."""

def anagrama(palabra1, palabra2):
    if len(palabra1) != len(palabra2) or palabra1 == palabra2:
        print("No son anagramas")
        return

    for letra in palabra1:
        if palabra1.count(letra) != palabra2.count(letra):
            print("No son anagramas")
            return

    print("Son anagramas")

anagrama("gaua", "agua")

#Otra manera de hazerlo
#Smplificado usando sorted

def anagrama(palabra1, palabra2):
    if len(palabra1) != len(palabra2) or palabra1 == palabra2:
        print("No son anagramas")
    elif sorted(palabra1) == sorted(palabra2):
        print("Son anagramas")
    else:
        print("No son anagramas")

anagrama("ga", "ag")
