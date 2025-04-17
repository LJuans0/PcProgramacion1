print("THIS ELECTRONIC CALCULATOR ONLY WORKS WITH NUMBERS OF ELECTRONS")
e=int(input("Enter the number of electrons:"))
print("thinking...")
erestantes=e
configuracion=""
orbitales = [
    ("1s", 2), ("2s", 2), ("2p", 6),
    ("3s", 2), ("3p", 6),
    ("4s", 2), ("3d", 10), ("4p", 6),
    ("5s", 2), ("4d", 10), ("5p", 6),
    ("6s", 2), ("4f", 14), ("5d", 10), ("6p", 6),
    ("7s", 2), ("5f", 14), ("6d", 10), ("7p", 6)
]
# Recorremos los orbitales hasta llenar todos los electrones
for orbital, capacidad in orbitales:
    if erestantes <= 0:
        break
    if erestantes >= capacidad:
        configuracion += f"{orbital}{capacidad} "
        erestantes -= capacidad
    else:
        configuracion += f"{orbital}{erestantes} "
        erestantes = 0
print("Configuración electrónica:", configuracion)