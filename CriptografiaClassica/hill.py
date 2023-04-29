from sympy import *
import itertools

fichero_cifrado = open("6", "r")
texto = "".join(fichero_cifrado)
fichero_descifrado = ""
matriz_permutadora = Matrix()

plaintext = ""
frecuencias = {}

for i in range(0,len(texto)):

    plaintext += chr(ord(texto[i])%26+65)
    if i % 2 == 0 and i >= 2:
        if not plaintext[i-2:i+1] in frecuencias:
            frecuencias[plaintext[i-2:i+1]] = 1
        else:
            frecuencias[plaintext[i-2:i+1]] +=1

frecuencias = dict(sorted(frecuencias.items(), key=lambda item: item[1]))
C = Matrix([[10,17,1], [3,12,1], [3,13,20]])

candidatos = ["THE","AND","ING","HER","YOU","VER","WAS","HAT","FOR","NOT","THI","THA","HIS","ENT","ION","ITH","ERE","WIT","ALL","EVE","OUL","ULD","TIO","TER","HAD","HEN","ERA","ARE","HIN","OUR","SHO","TED","OME","BUT"]
candidatos_agrupados = list(itertools.permutations(candidatos,3))

for i in range(0,len(candidatos_agrupados)):

    M = Matrix([[ord(candidatos_agrupados[i][0][0])-65, ord(candidatos_agrupados[i][0][1])-65, ord(candidatos_agrupados[i][0][2])-65],[ord(candidatos_agrupados[i][1][0])-65, ord(candidatos_agrupados[i][1][1])-65, ord(candidatos_agrupados[i][1][2])-65],[ord(candidatos_agrupados[i][2][0])-65, ord(candidatos_agrupados[i][2][1])-65, ord(candidatos_agrupados[i][2][2])-65]])
    M = M.T

    if (M.det() != 0 and gcd(M.det(),26)==1):

        A = (C * M.inv_mod(26))%26
        if (A.det() != 0 and gcd(A.det(),26)==1):

            D = (A.inv_mod(26)*C.T)%26
            if D == M:

                print("Encontrada")
                break

for i in range(0,90,9):

    C = Matrix([[ord(texto[i])-65,ord(texto[i+1])-65,ord(texto[i+2])-65],[ord(texto[i+3])-65,ord(texto[i+4])-65,ord(texto[i+5])-65],[ord(texto[i+6])-65,ord(texto[i+7])-65,ord(texto[i+8])-65]])
    M = (matriz_permutadora.inv_mod(26)*C.T)%26
    M = M.T
    fichero_descifrado += chr(M[0,0]+65)+chr(M[0,1]+65)+chr(M[0,2]+65)+chr(M[1,0]+65)+chr(M[1,1]+65)+chr(M[1,2]+65)+chr(M[2,0]+65)+chr(M[2,1]+65)+chr(M[2,2]+65)

print(fichero_descifrado)