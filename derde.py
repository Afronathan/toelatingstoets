# programma met datetime
from datetime import date
today = date.today ()
print "Vandaag is het:" ,today.day , today.month , today.year
#vragen om geboortedatum + doorlating procedure 
print "typ je geboortejaar in:"
geboortejaar = int(raw_input())
if today.year - geboortejaar < 10:
	print "Je bent geweigerd."
	exit ()
if today.year - geboortejaar > 100:
	print "U bent geweigerd."
	exit ()
print "typ je geboortemaand in:"
geboortemaand = int(raw_input())
if today.year - geboortejaar == 10 and today.month < geboortemaand:
	print "Je bent geweigerd."
	exit ()
print "typ je geboortedag in:"
geboortedag = int(raw_input())
if today.year - geboortejaar == 10 and today.month == geboortemaand and today.day < geboortedag:
	print "Je bent geweigerd." 
	exit ()
else :
	print "Welkom"	

#leeftijd berekenen
if geboortemaand <= today.month and geboortedag <= today.day:
	print "Je leeftijd is zoveel jaar:" , today.year - geboortejaar,
	print "En zoveel maanden:" , today.month - geboortemaand
else :
	print "Je leeftijd is zoveel jaar:" , today.year - geboortejaar -1,
	print "en zoveel maanden:" , (12 - geboortemaand) + (today.month -1)
if geboortedag <= today.day:
	print "Je leeftijd is zoveel maanden:" ,(today.year - geboortejaar) * 12 + (today.month - geboortemaand)
else :
	print "Je leeftijd is zoveel maanden:" , (today.year - geboortejaar) * 12 + (today.month - geboortemaand) -1

#geboortedag weten
print "Op welke dag van de week ben je geboren?"
DVDW = (raw_input())
def m 
def d 
def w 
def v 
def z 
if not m or d or w or v or z :
	print "Fout! Alleen eerste letter geven."



