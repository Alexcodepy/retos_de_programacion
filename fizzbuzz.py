```python
"""
Imprime los números del 1 al 100.
Si un número es divisible por 3, muestra “fizz”.
Si es divisible por 5, muestra “buzz”.
Si es divisible por ambos, muestra “fizzbuzz”; si no, el número.
"""

def fizz_buzz():    
    lista_inicial = list(range(1, 101))
    for e in lista_inicial:
        if e% 3 == 0 and e%5 == 0:  
            print(e, "fizzuzz",sep="-")
        else:
            if e%3 == 0:
                print(e, "fizz",sep="-")
            elif 3%5 == 0:
                print(e, "buzz",sep="-")
            else:
                print(e)
 
fizz_buzz()
```
