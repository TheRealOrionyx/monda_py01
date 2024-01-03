def prideti_produkta(saldytuvas_turinys, produktas, kiekis):
    if produktas in saldytuvas_turinys:
        saldytuvas_turinys[produktas] += kiekis
    else:
        saldytuvas_turinys[produktas] = kiekis

def isimti_produkta(saldytuvas_turinys, produktas, kiekis):
    if produktas in saldytuvas_turinys:
        if saldytuvas_turinys[produktas] >= kiekis:
            saldytuvas_turinys[produktas] -= kiekis
        else:
            print(f"Kiekio nepakanka: {produktas}")
    else:
        print(f"Produktas nerastas: {produktas}")

def patikrinti_kieki(saldytuvas_turinys, produktas, reikiamas_kiekis):
    if produktas in saldytuvas_turinys:
        return saldytuvas_turinys[produktas] >= reikiamas_kiekis
    else:
        return False

def ispausdinti_turini(saldytuvas_turinys):
    print("Šaldytuvo turinys:")
    for produktas, kiekis in saldytuvas_turinys.items():
        print(f"{produktas}: {kiekis}")

def patikrinti_recepta(saldytuvas_turinys, receptas):
    truksta = {}
    for produktas, reikiamas_kiekis in receptas.items():
        if patikrinti_kieki(saldytuvas_turinys, produktas, reikiamas_kiekis):
            continue
        else:
            truksta[produktas] = reikiamas_kiekis - saldytuvas_turinys.get(produktas, 0)
    if truksta:
        print("Trūksta šių produktų:")
        for produktas, trukstamas_kiekis in truksta.items():
            print(f"{produktas}: {trukstamas_kiekis}")
    else:
        print("Receptas įgyvendinamas!")

# Vartotojo įvesties pavyzdys:
saldytuvas_turinys = {}

while True:
    veiksmas = input("Pasirinkite veiksmą (pridėti/išimti/turinys/receptas/exit): ").lower()

    if veiksmas == "exit":
        break
    elif veiksmas == "prideti":
        produktas = input("Įveskite produktą: ")
        kiekis = float(input("Įveskite kiekį: "))
        prideti_produkta(saldytuvas_turinys, produktas, kiekis)
    elif veiksmas == "isimti":
        produktas = input("Įveskite produktą: ")
        kiekis = float(input("Įveskite kiekį: "))
        isimti_produkta(saldytuvas_turinys, produktas, kiekis)
    elif veiksmas == "turinys":
        ispausdinti_turini(saldytuvas_turinys)
    elif veiksmas == "receptas":
        recepto_ivestis = input("Įveskite receptą (pvz.: Pomidoras:1, Duona:0.5): ")
        receptas = dict(item.split(":") for item in recepto_ivestis.split(","))
        patikrinti_recepta(saldytuvas_turinys, receptas)
    else:
        print("Nežinomas veiksmas. Bandykite dar kartą.")
