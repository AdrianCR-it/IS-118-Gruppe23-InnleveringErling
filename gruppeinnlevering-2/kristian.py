#variabel for poeng systemet
poeng = 0

#Introduksjon av spillet
print("Erling er prosjektleder og leder et team som skal lage en ny medborgerportal.")
print("Flere grupper med ulike arbeidserfaringer og ekspertiser begynner å kollidere.")
print("Det har gått seks uker siden prosjektet startet.")
print("Uenigheten er enda lavmeld, men Erling legger merke til at frustrasjonen øker.")
print("Klarer dette teamet å levere ferdig prototype om tre uker? ")
print("Klarer de å gå ut av stormingsfasen og inn i normingsfasen? ")
input ("\nTrykk enter for å fortsette\n")


#Introduksjon til senario 1
print("UX-designer Silje og IT-rådgiver Elias er uenig i teknologivalg.")
print("Elias mener forslaget til Silje er alt for dyrt, usikkert og urealistisk.")
print("Silje mener forslaget til Elias vil låse brukeropplevelsen")


#Forklaring av senario 1 alternativer
print()
print("Hva bør Erling gjøre?")
print("A: Skal han ta individuelle samtaler for å dempe temperaturen?")
print("B: Skal han ta det opp i plenum for å skape åpenhet?")

#Logikken under valget av senario 1
def Senario1_A():
    print("Erling samler Silje og Elias til individuelle samtaler.")
    print("Erling anerkjenner deres begges behov, men er stram på at personangrep og rekrutering av andre er ikke greit.")
    print("Konflikten løses, men tar litt tid")
def Senario1_B():
    print("Erling samler hele teamet til et felles møte for å ta opp problemet i plenum.")
    print("Silje og Elias får senen for å forklare hva de tenker og mener er lurest. Silje og Elias føler også at de må forsvare seg selv foran kollegaene sine")

while True:
    valg_1 = input("Velg A eller B: ")
    if valg_1 in ("a", "b", "A", "B"):
        break
    print("Svaret ditt er ikke gyldig. Velg a eller b")

if valg_1.lower() == "a":
    poeng += 1
    print("Du valgte alternativ A:")
    Senario1_A()
else:
    poeng -= 1
    print("Du valgte alternativ B:")
    Senario1_B()
input ("\nTrykk enter for å fortsette\n")


#Introduksjon til senario 2
print("Det er ikke bare Silje og Elias som bemerker seg problemer under dette prosjektet.")
print("Litt senere havner også Hamdi i kulturavdelingen og Hallgeir som er brukerrepresentant i konflikt.")
print("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform.")
print("Hallgeir ønsker et mer åpen dialogbasert system med rom for spontane innspill")

#Forklaring av senario 2 alternativer
print()
print("Hva bør Erling gjøre?")
print("A: Erling arrangerer et felles møte for å avklare uenigheter.")
print("B: Erling lar Hamdi og Hallgeir finne ut av konflikten på egen hånd.")

#logikken under senario 2
def Senario2_A():
    print("Erning arrangerer et felles møte for å avklare uenigheter.")
    print("Under møtet kommer Brukerrepresentant Jabir og politisk rådgiver Marcia med en idé med å inngå et kompromiss.")
    print("Denne ideen legger opp for en strukturert kanal med faste innspillsrunder kombinert med åpen dialogdel.")
    print("Teamet finner en løsning som ivaretar flere interesser og styrker samarbeidet")
def Senario2_B():
    print("Erling lar Hamdi og Hallgeir løse konflikten på egen hånd.")
    print("amdi og Hallgeir diskuterer flere muligheter, men sliter med å bli enige.")
    print("beslutningene blir forsinket, og at samarbeidet svekkes.")

while True:
    valg_2 = input("Velg A eller B:")
    if valg_2 in ("a", "b", "A", "B"):
        break
    print("Svaret er ikke gyldig. Velg A eller B")

if valg_2.lower() == "a":
    poeng += 1
    print("Du valgte alternativ A:")
    Senario2_A()
else:
    poeng -= 1
    print("Du valgte alternativ B:")
    Senario2_B()
input ("\nTrykk enter for å fortsette\n")


#Introduksjon til senario 3
print("Erling lurer på hvordan han skal bevare og opprettholde gruppedynamikken og motivasjonen for prosjektet.")
print("Erling stusser mellom å prioritere sosiale aktiviteter med teamet eller sette fullt fokus på fremdrift på å levere tjenesten.")

#Alternativer til senario 3
print()
print("Hva bør Erling gjøre?")
print("A: Erling setter av tid til en sosial aktivitet for teamet.")
print("B: Erling prioriterer fremdrift og leveransen fremfor sosiale aktiviteter.")

#Logikken under senario 3
def Senario3_A():
    print("Erling inviterer til en grill kveld på terrassen hjemme hos han.")
    print("Han håper at en sosial aktivitet kan styrke samholdet og bidra til at teamet kommuniserer bedre.")
    print("Relasjonene og motivasjonen øker, og samarbeidet blir bedre.")
def Senario3_B():
    print("Erling velger å prioritere prosjektarbeidet fremfor sosiale aktiviteter.")
    print("Han setter tydelige mål, fordeler arbeidsoppgavene og følger opp fremdriften gjennom faste møter.")
    print("For stort fokus på prosjektet fører til økt stress og redusert motivasjon.")

while True:
    valg_3 = input("Velg A eller B:")
    if valg_3 in ("a", "b","A","B"):
        break
    print("Svaret er ikke gyldig. Velg A eller B")

if valg_3.lower() == "a":
    poeng += 1
    print("Du valgte alternativ A:")
    Senario3_A()
else:
    poeng -= 1
    print("Du valgte alternativ B:")
    Senario3_B()
input ("\nTrykk enter for å se resultatet ditt\n")

#Slutt basert på valgene som er tatt
if poeng == 3:
    print("Teamet får lever prototypen innen fristen.")
    print("Erling retter konfliktene tidlig og legger rette for åpen kommunikasjon.")
    print("Teamet finner en balanse mellom teknologi, brukeropplevelse og sikkerhet.")
    print("Tilliten øker, gode relasjoner er bygget, motivasjonen øker og teamet beveger seg mot normingsfasen.")
elif poeng >= 0:
    print("Teamet leverer prototypen innen fristen, men teamet er fremdeles sårbart.")
    print("Erling løser noen av konfliktene, men uenigheter gjenstår.")
    print("Samarbeidet er litt bedre enn før, men de trenger fortsatt oppfølging av Erling.")
    print("Teamet gå ikke videre til normingsfasen.")
else:
    print("Prosjektet stoppes opp og utfordringene i teamet blir større.")
    print("Flere blir passive, eller trekker seg ut. Prosjektgruppen forblir i storming fasen.") 