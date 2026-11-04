poeng = 0


#Introduksjon til spillet
print("Erling er prosjektleder og leder et team som skal lage en ny medborgerportal.")
print("Flere av gruppene med ulik arbeidserfaringer og ekspertiser begynner å kollidere med hverandre.")
print("Nå er det seks uker siden prosjektet startet.")
print("Uenigheten er fortsatt lavmeld, men Erling legger merke til at frustrasjonen mellom de i gruppen øker.")
print("Klarer han å få dette teamet til å levere en ferdig prototype om 3 uker? ")
print("Det er opp til deg å hjelpe Erling med å ta de riktige valgene for å få teamet til å fungere sammen og levere en prototype.")
input("\nEr du klar for å fortsette dette magiske eventyret som handler om samhold sammen med Erling? (Trykk enter for å starte spillet)\n") 


# Forklaring av Senario 1
print("Den første konflikten Erling må prøve å løse er mellom UX-designer Silje og IT-rådgiver Elias.")
print("Silje og Elias er uenig om teknologivalg.")
print("Silje har designet et forslag til IT-rådgiverne, men Elias mener dette er alt for dyrt, usikkert og urealistisk.")
print("Silje mener det Elias foreslår vil låse brukeropplevelsen og hindre innovasjon.")

#Forklaring av valgmuligheter erling har
print("Erling har to valg for å løse konflikten mellom Silje og Elias.")
print("Alternativ A: Erling gjennomfører individuelle samtaler for å løse det opp")
print("Alternativ B: Erling tar konflikten opp direkte i plenum og ber teamet avgjøre hvilken løsning som er best.")
#definering av scenario 1 A og B
def scenario1_A():
    print("Erling gjennomfører individuelle samtaler med Silje og Elias.")
    print("Han får dem til å forstå hverandres perspektiver og kommer til en løsning, men det tar litt tid.")
def scenario1_B():
    print("Erling tar konflikten opp i plenum")
    print("Teamet blir ikke enige med hverandre og konflikten eskalerer, og kommunikasjonen svekkes.")
    
# Valgmuligheter
while True:
    valg_1 = input("Velg A eller B:")
    if valg_1 in ("a", "b", "A", "B"):
        break
    print("Svaret er ikke gyldig. Velg A eller B")

if valg_1.upper() == "A":
    poeng += 1
    scenario1_A()
    print(f"poeng: {poeng}")
else:
    scenario1_B()
    print(f"Poeng: {poeng}")

#Fortsettelse til scenario 2
input("\nTrykk enter for å fortsette til neste scenario\n")


#Forklaring av scenario 2
print("Det er ikke bare Silje og Elias som bemerker seg problemer under dette prosjektet")
print("Tre uker senere havner også Hamdi i kulturavdelingen og Hallgeir som er brukerrepresentant i konflikt.")
print(" Hamdi ønsker en mer restriktiv og kontrollert løsning for innbyggernes innspill, mens Hallgeir ønsker en mer åpen og dialogstyrt løsning med rom for spontane innspill.")
print("Hva skal Erlig gjøre?")

#Forklaring av valgmuligheter for scenario 2
print("Erling har to valg for å løse konflikten mellom Hamdi og Hallgeir.")
print("Alternativ A: Erling arrangerer et felles møte for å avklare uenigheter")
print("Alternativ B: Erling lar Hamdi og Hallgeir finne ut av konflikten på egen hånd.")

#definering av scenario 2 A og B
def scenario2_A():
    print("Erling arrangerer et felles møte for å avklare uenigheter")
    print("Teamet finner en løsning som ivaretar flere interesser og styrker samarbeidet, men løsningen krever mer planlegging og kan føre til at prototypen blir forsinket.")

def scenario2_B():
    print("Erling lar Hamdi og Hallgeir finne ut av konflikten på egen hånd.")
    print("De blir ikke enige og konflikten eskalerer, og samarbeidet svekkes.")

# Valgmuligheter
while True:
    valg_2 = input("Velg A eller B:")
    if valg_2 in ("a", "b", "A", "B"):
        break
    print("Svaret er ikke gyldig. Velg A eller B")

if valg_2.upper() == "A":
    poeng += 1
    scenario2_A()
    print(f"poeng: {poeng}")
else:
    scenario2_B()
    print(f"Poeng: {poeng}")

#fortsettelse
input("\nTrykk enter for å fortsette til neste oppgave\n")



#Motivasjon eller fremdrift
print("Erling lurer på hvordan han skal bevare og opprettholde gruppedynamikken og motivasjonen for prosjektet.")
print("Erling stusser mellom å prioritere sosiale aktiviteter med teamet eller sette fullt fokus på fremdrift på å levere tjenesten.")
print("Hva tenker du Erling bør gjøre?")

#forklaring av valgmuligheter for motivasjon eller fremdrift
print("Alternativ A: Erling setter av tid til en sosial aktivitet")
print("Alternativ B: Erling prioriterer fremdrift og leveransen fremfor sosiale aktiviteter.")

#definering av scenario 3 A og B
def scenario3_A():
    print("Erling planlegger en grillkveld med teamet for å styrke samholdet og motivasjonen.")
    print("Relasjonene blir bedre i laget og motivasjonen øker")
def scenario3_B():
    print("Erling prioriterer fremdrift og leveransen fremfor sosiale aktiviteter.")
    print("Samarbeidet svekkes og motivasjonen synker, men fremdriften på leveransen opprettholdes.")

# Valgmuligheter
while True:
    valg_3 = input("Velg A eller B:")
    if valg_3 in ("a", "b","A","B"):
        break
    print("Svaret er ikke gyldig. Velg A eller B")

if valg_3.upper() == "A":
    poeng += 1
    scenario3_A()
    print(f"poeng: {poeng}")
else:
    scenario3_B()
    print(f"Poeng: {poeng}")


input("\nTrykk enter for å se om teamet klarte det eller ikke\n")

#Avslutning av spillet
if poeng == 3:
    print("Du og Erling klarte det!")
    print("Prototypen ble levert i tide og teamet har blitt mer sammensveiset og motivert for fremtidige prosjekter.")
elif poeng >= 1:
    print("Dere klarte det så vidt...")
    print("Prototypen ble levert, men teamet har fortsatt noen utfordringer med samarbeidet og motivasjonen er i kjellern.")
else:
    print("Teamet ditt slutter en etter en og prototypen ble ikke levert i tide." \
    " Erling må starte prosjektet på nytt med et nytt team.")
