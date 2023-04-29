fichero_cifrado = open("4", "r")
texto = "".join(fichero_cifrado)

fichero_descifrado = ""
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
especiales = " !'()*+,-./:;<=>?@[]\^_`{}|~"

for num in range(26):
    for i in range(0,100):
        c = texto[i]

        if c == " " or c == "\n" or c.isdigit() or c in especiales:
            fichero_descifrado += texto[i]

        else:
            fichero_descifrado += abecedario[(ord(c) % 52 - num) % 52]

    print("NEW")
    print(fichero_descifrado)
    fichero_descifrado = ""









