croissant = int(input('Aantal croissants: '))
croissantprijs = float(input('Prijs per croissant: '))
stokbrood = int(input('Aantal stokbroodjes: '))
stokbroodprijs = float(input('Prijs per stokbrood: '))
korting = float(input('Hoeveelheid korting: '))
bedrag = (croissant * croissantprijs) + (stokbrood * stokbroodprijs) - korting
text = 'De feestlunch kost je bij de bakker ' + str(bedrag) + ' euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!'

print(text)