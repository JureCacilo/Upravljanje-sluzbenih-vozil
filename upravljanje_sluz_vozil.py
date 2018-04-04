class Vozilo(object):

    def __init__(self, znamka, model, st_prevoz_km, zadnji_servis):

        self.znamka = znamka
        self.model = model
        self.st_prevoz_km = st_prevoz_km
        self.zadnji_servis = zadnji_servis

    def znamka_model(self):
        return self.znamka + ", " + self.model



def seznam_vozil_(vozni_park):
    for index, vozilo in enumerate(vozni_park):
        print("ID: ", str(index))
        print(vozilo.znamka_model())
        print("Stevilo prevozenih kilometrov: " + str(vozilo.st_prevoz_km))
        print("Datum zadnjega servisa: " + vozilo.zadnji_servis)
        print("")

    if not vozni_park:
        print("Nimas nobenega vozila v voznem parku.")
        print("")

def uredi_st_prevoz_km(vozni_park):
    print("Vnesi ID vozila, ki bi mu rad spremenil stevilo prevozenih kilometrov.")
    for index, vozilo in enumerate(vozni_park):
        print(str(index) + ") " + vozilo.znamka_model())

    print("")
    if not vozni_park:
        print("Nimas nobenega vozila v voznem parku.")
        print("")

    else:
        id_vozila = int(input("Vnesite ID vozila:"))
        vozilo = vozni_park[id_vozila]
        novo_st_km = float(input("Vnesite novo stevilo prevozenih kilometrov:"))
        vozilo.st_prevoz_km = novo_st_km
        print(vozilo.znamka_model() + " je bilo uspesno spremenjeno stevilo prevozenih kilometrov.")


def uredi_zadnji_servis(vozni_park):
    print("Vnesi ID vozila, ki bi mu rad spremenil datum zadnjega servisa.")
    for index, vozilo in enumerate(vozni_park):
        print(str(index) + ") " + vozilo.znamka_model())

    print("")
    if not vozni_park:
        print("Nimas nobenega vozila v voznem parku.")
        print("")
    else:

        id_vozila = int(input("Vnesite ID vozila?:"))
        vozilo = vozni_park[id_vozila]
        nov_servis = input("Vnesite nov zadnji servis(primer zapisa: 04.03.2018):")
        vozilo.zadnji_servis = nov_servis
        print(vozilo.znamka_model() + " je bil usepsno spremenjen zadnji servis.")

def dodati_novo_vozilo(vozni_park):
    znamka = input("Vnesi znamko vozila: ")
    model = input("Vnesi model vozila: ")
    st_prevoz_km = float(input("Vnesi stevilo prevozenih kilometrov: "))
    zadnji_servis = input("Vnesi zadnji servis vozila(primer zapisa: 04.03.2018):")

    novo_vozilo = Vozilo(znamka = znamka,model = model, st_prevoz_km = st_prevoz_km, zadnji_servis = zadnji_servis )
    vozni_park.append(novo_vozilo)

    print("")
    print(novo_vozilo.znamka_model() + " je bilo usepsno dodano v park vozil.")

def izbrisi_vozilo(vozni_park):
    print("Vnesi ID vozila, ki bi ga rad izbrisal.")
    for index, vozilo in enumerate(vozni_park):
        print(str(index) + ") " + vozilo.znamka_model())

    print("")

    if not vozni_park:
        print("Nimas nobenega vozila v voznem parku.")
        print("")
    else:

        id_vozila = int(input("Vnesite ID vozila?:"))
        vozilo = vozni_park[id_vozila]
        vozni_park.remove(vozilo)
        print("Vozilo je bilo odstranjeno uspesno.")

def main():
    print("Dobrodosli v voznem parku.")

    #Dodajmo vozila v vozni park
    avto1 = Vozilo(znamka = "Ford", model = "Focus", st_prevoz_km = 60000, zadnji_servis = "15.01.2018")
    avto2 = Vozilo(znamka = "Audi", model = "A4", st_prevoz_km = 33000, zadnji_servis = "12.12.2017")
    avto3 = Vozilo(znamka = "Citroen", model = "Berlingo", st_prevoz_km = 150000, zadnji_servis = "03.04.2018")

    vozni_park = [avto1, avto2, avto3]

    while True:
        print("Prosim vnesite eno izmed teh moznosti")
        print("1: Poglej vsa vozila")
        print("2: Dodaj novo vozilo")
        print("3: Uredi stevilo prevozenih km na vozilu")
        print("4: Uredi zadnji servis vozila")
        print("5: Izbrisi vozilo iz voznega parka")
        print("6: Koncaj program")

        izbira = input("Izberi moznost(1, 2, 3, 4, 5, 6):")
        print("")

        if izbira == "1":
            seznam_vozil_(vozni_park)
        elif izbira == "2":
            dodati_novo_vozilo(vozni_park)
        elif izbira == "3":
            uredi_st_prevoz_km(vozni_park)
        elif izbira == "4":
            uredi_zadnji_servis(vozni_park)
        elif izbira == "5":
            izbrisi_vozilo(vozni_park)
        elif izbira == "6":
            print("Hvala, ker ste uporabljali program za upravljanje sluzbenih vozil.")
            break
        else:
            print("Oprostite ta moznost ne obstaja, poskusite se enkrat.")
            continue

if __name__ == "__main__":
    main()




