import time

def divisors(n):
    result = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    return list(sorted(result))

fichero_cifrado = open("5", "r")
texto = "".join(fichero_cifrado)
fichero_descifrado = ""

divisores = divisors(len(texto))
print(divisores)

for x in range(len(divisores)):

    f = divisores[x]
    c = divisores[len(divisores)-1-x]

    for i in range(0,f):
        for j in range(0,c):
            fichero_descifrado += texto[f*j+i]

    print(fichero_descifrado)
    time.sleep(2)
    print(f)
    print(c)
    fichero_descifrado = ""








