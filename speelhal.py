toegang = float(input('Toegangs prijs: '))
personen = int(input('Aantal personen: '))
vr = float(input('VR kost per minuut: '))
minuten = int(input('Aantal minuten: '))
bedrag = (toegang * personen) + (vr * minuten * personen)
text = 'Dit geweldige dagje-uit met ' + str(personen) + ' mensen in de Speelhal met 45 minuten VR kost je maar ' + str(bedrag) + ' euro'

print(text)