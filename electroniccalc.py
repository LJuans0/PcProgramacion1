print("THIS ELECTRONIC CALCULATOR ONLY WORKS WITH NUMBERS OF ELECTRONS IN AN ATOM")
print("THE LOCATION OF THE ELEMENT IN THE PERIODIC TABLE MAY NOT WORK IF IT ENTERS THE D OR F ORBITAL")

e=int(input("Enter the number of electrons:"))
print("thinking...")
erestantes=e
configuracion=""
orbitales = [
    (1,"s", 2), (2,"s", 2), (2,"p", 6),
    (3,"s", 2), (3,"p", 6),
    (4,"s", 2), (3,"d", 10), (4,"p", 6),
    (5,"s", 2), (4,"d", 10), (5,"p", 6),
    (6,"s", 2), (4,"f", 14), (5,"d", 10), (6,"p", 6),
    (7,"s", 2), (5,"f", 14), (6,"d", 10), (7,"p", 6)
]
ev=0
nv=1
grupo=0
# Recorremos los orbitales hasta llenar todos los electrones
for nivel, subnivel, orbital in orbitales:
    if erestantes <= 0:
        break
    if erestantes >= orbital:
        configuracion += f"{nivel}{subnivel}{orbital} "
        erestantes -= orbital
        if nv<nivel:
            nv = nivel
            ev = orbital
        elif nv == nivel:
            ev += orbital
    else:
        configuracion += f"{nivel}{subnivel}{erestantes} "
        if nv<nivel:
            nv = nivel
            ev = erestantes
        elif nv == nivel and ev!=erestantes:
            ev += erestantes
        erestantes = 0
print("------------------------------------RESULTS------------------------------------")
print("Electronic configuration→", configuracion)
print("Valence level→",nv)
print("Valence electrons→",ev)
print("↓↓↓Place in the periodic table↓↓↓")
if ev>2:
    grupo=ev+10
else:
    grupo=ev
print(f"Period:{nv} Group:{grupo}")
print("--------------------------------------------------------------------------------")