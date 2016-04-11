class beleznica__kontaktov:
    def __init__(self, first_name, last_name, email, phone, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def izpis(self):
        print "First name:", self.first_name
        print "Last name:", self.last_name

beleznica__kontaktov = []

while True:
    dodaj_nov_kontakt = (raw_input("Zelite dodati nov kontakt? da/ne: ").lower())
    if dodaj_nov_kontakt == "da":
        nov_kontakt = beleznica__kontaktov(ime=raw_input("Ime:"),
                                           priimek=raw_input("Priimek:"),
                                           naslov=raw_input("Naslov:"),
                                           telefon=raw_input("Telefon:"),
                                           email=raw_input("E-mail:"))

        beleznica__kontaktov.append(nov_kontakt)

    elif dodaj_nov_kontakt == "ne":
        break

for nov_kontakt in beleznica__kontaktov:
    beleznica__kontaktov.izspis()





