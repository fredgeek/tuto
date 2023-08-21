#  fichier reserve au collaborateurs....
# kenfack durel

def table_mult(nombre):
    for i in range(nombre):
        print(f"{nombre} * {i} = {nombre*i}")
        
    return "fin"

nmbr=int(input("entre un nombre : "))
print(table_mult(nmbr))