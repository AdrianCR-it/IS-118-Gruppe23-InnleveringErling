import time

def hent_valg(spørsmål):
    while True:
        svar = input(spørsmål).strip().upper()
        if svar =="A" or svar =="B":
            return svar
        print("Ugyldig valg. Vennligst velg A eller B.")
        pause()
valg1 = ""
valg2 = ""
valg3 = ""
poeng = 0

def pause():
    print()
    time.sleep(1)
    print()

pause()

print("========================================================================================================================")

print("Erling er prosjektleder og leder et team som skal lage en ny medborgerportal. Prosjekt gruppen opplever noen problemer med gruppedynamikk og uenighet innad i prosjektet. Flere grupper med ulike arbeidserfaringer og ekspertiser begynner å kollidere.") 

pause()

print("Det har gått seks uker siden prosjektet startet. Prosjektleder Erling har nettopp samlet prosjekt teamet for første gang. Etter et møte med mye engasjement og høy energi, begynner teamet å møte på sine første reelle utfordringer. Uenigheten er enda lavmeld men Erling legger merke til å frustrasjonen øker. Det er viktig at dette løser seg ganske fort ettersom første prototype skal være klar om tre uker. Kommunikasjonen hakker, og stemningen er spent. Prosjekt leder Erling vet at de neste valgene han tar bestemmer om de klarer å nå dette målet. Klarer dette teamet å levere ferdig prototype om tre uker, og klarer de å gå ut av stormingsfasen og inn i normingsfasen? ") 

pause()

print("========================================================================================================================")



input("Trykk ENTER for å fortsette til den første konflikten ===>")

print("========================================================================================================================")

pause()

print("KONFLIKT #1")

pause()

print("Konflikten mellom Silje og Elias")

pause()

print("Den første konflikten Erling må prøve å løse er mellom UX-designer Silje og IT-rådgiver Elias. Silje og Elias er uenig om teknologivalg. Silje har designet et forslag til IT-rådgiverne, men Elias mener dette er alt for dyrt, usikkert og urealistisk. Silje mener det Elias foreslår vil låse brukeropplevelsen og hindre innovasjon ")

pause()

print("Alternativ A: Erling gjennomfører individuelle samtaler")

pause()

print("Alternativ B: Erling tar konflikten opp direkte i plenum og ber teamet avgjøre hvilken løsning som er best.")

pause()

valg1 = hent_valg("SVAR: ")
if valg1 == "A":
    poeng += 1
    print("Erling velger å gå for individuelle samtaler med Silje og Elias i et håp for å dempe temperaturen. Under samtalen har Erling stramme rammer, slik at begge parter føler at de blir tatt på alvor. Erling anerkjenner deres begges behov, men er stram på at personangrep og rekrutering av andre er ikke greit, ettersom dette fører til en splitting i teamet. Erling anerkjenner at Silje har et poeng når det gjelder fleksibilitet og god bruker opplevelse, men at Elias har et godt poeng for sikkerhet og kostnad. Erling ber dem å forklare hva de trenger for å løse dette og ikke hva de er imot.")
    pause()
    print("Konflikten løses, men tar litt tid.")
else:
    print("Erling går for å samle teamet til et møte for å ta opp problemet i plenum. Alle kommer med ideer og drøfter med fordeler og ulemper med begge ideene. Silje og Elias får senen for å forklare hva de tenker og mener er lurest. Silje og Elias føler også at de må forsvare seg selv foran kollegaene sine. Erling mener dette bør avgjøres på flertallsvedtak, selv om det kan føre til splitting i gruppen, ettersom en avgjørelse med flerstemmer fører til vinnere og tapere.")
    pause()
    print("konflikten forsterkes og kommunikasjonen svekkes.")

pause()

print("========================================================================================================================")

input("Trykk ENTER for å gå videre til neste konflikt ===>")

print("========================================================================================================================")

pause()

print("KONFLIKT #2")

pause()

print("Konflikten mellom Hamdi og Hallgeir")

pause()

print("Det er ikke bare Silje og Elias som bemerker seg problemer under dette prosjektet. Tre uker senere havner også Hamdi i kulturavdelingen og Hallgeir som er brukerrepresentant i konflikt. Hamdi ønsker en mer restriktiv og kontrollert løsning for innbyggernes innspill, mens Hallgeir ønsker en mer åpen og dialogstyrt løsning med rom for spontane innspill. Hamdi sin løsning er billigere, men vil gi mindre innsikt og legitimitet blant innbyggerne. Hallgeirs løsning derimot, er dyrere, men vil gi mer innsikt og medvirkning blant innbyggerne.")

pause()

print("Alternativ A: Erling arrangerer et felles møte for å avklare uenigheter.")

pause()

print("Alternativ B: Erling lar Hamdi og Hallgeir finne ut av konflikten på egen hånd.")

pause()

valg2 = hent_valg("SVAR: ")
if valg2 == "A":
    poeng += 1
    pause()
    print("Erling samler teamet for et fagmøte for å ta opp problemet og prøve å komme på en måte slik at alle blir fornøyde. Brukerrepresentant Jabir og politisk rådgiver Marcia kom med en idé med å inngå et kompromiss. Erling var fornøyd med dette, han tenkte på at et kompromiss er bedre enn et flertallsvedtak. Jabir og Marcia vurderte et kompromiss som legger opp for strukturert kanal med faste innspillsrunder kombinert med åpen dialog")
    pause()
    print("Teamet finner en løsning som ivaretar flere interesser og styrker samarbeidet, men løsningen krever mer planlegging og kan føre til at prototypen blir forsinket.")
else:
    pause()
    print("Erling velger å la Hamdi og Hallgeir finne en løsning på egen hånd. Han håper at de klarer å samarbeide og inngå et kompromiss uten hans hjelp. Hamdi og Hallgeir diskuterer flere muligheter, men sliter med å bli enige. Hamdi ønsker fortsatt en kontrollert løsning, mens Hallgeir ønsker større åpenhet og medvirkning fra innbyggerne.")
    pause()
    print("beslutningene blir forsinket, og at samarbeidet svekkes. Teamet risikerer å ikke bli ferdig med prototypen innen fristen. Samtidig får Hamdi og Hallgeir mulighet til å ta ansvar og utvikle evnen til å løse konflikter selv.")

pause()

print("========================================================================================================================")

input("Trykk ENTER for å gå videre til neste konflikt ===>")

print("========================================================================================================================")

pause()

print("KONFLIKT #3")

pause()

print("Motivasjon eller fremdrift?")

pause()

print("Erling lurer på hvordan han skal bevare og opprettholde gruppedynamikken og motivasjonen for prosjektet. Erling stusser mellom å prioritere sosiale aktiviteter med teamet eller sette fullt fokus på fremdrift på å levere tjenesten.")

pause()

print("Alternativ A: Erling setter av tid til en sosial aktivitet for teamet.")

pause()

print("Alternativ B: Erling prioriterer fremdrift og leveransen fremfor sosiale aktiviteter.")

pause()

valg3 = hent_valg("SVAR: ")
if valg3 == "A":
    poeng += 1
    pause()
    print("Erling inviterer til en grill kveld på terrassen hjemme hos han. Han håper at teamet kan bli mer kjent med hverandre utenfor arbeidssituasjonen. Han håper at en sosial aktivitet kan styrke samholdet og bidra til at teamet kommuniserer bedre. Erling sørger for en inkluderende kveld, slik at ingen føler seg utenfor. ")
    pause()
    print("Relasjonene og motivasjonen øker, og samarbeidet blir bedre. Teamet blir tryggere på hverandre og det blir lettere å ta opp uenigheter på en konstruktiv måte. Noen kan også føle at dette tar tid fra viktige arbeidsoppgaver, særlig når fristen nærmer seg.")
else:
    pause()
    print("Erling velger å prioritere prosjektarbeidet fremfor sosiale aktiviteter. Han setter tydelige mål, fordeler arbeidsoppgavene og følger opp fremdriften gjennom faste møter. Han prioriterer arbeidet for å sikre at prototypen blir ferdig innen fristen.")
    pause()
    print("Teamet får bedre tid til å jobbe med prosjektet. For stort fokus på prosjektet fører til økt stress og redusert motivasjon. Ettersom teamet ikke får tid til å bygge relasjoner, kan samarbeidet bli dårligere over tid.")

if poeng >= 3:
    pause()
    print("Du har oppnådd stor sukksess! Teamet takker Erling for hans gode beslutningsevne.")

elif poeng == 2:
    pause()
    print("Du har oppnådd delvis suksess poeng og er herved middelmådig. Teamet leverer prototypen innen fristen, men teamet er fremdeles sårbart. Teamet går ikke videre til normingsfasen.")

else:
    pause()
    print("Erling har mislykket som leder. Teamet er så misfornøyde med hans lederskap til Erling at de velger å drepe han med øks. Erling dør og teamet leverte ikke prototypen i tide.")

pause()
print(f"Valgene du har gjort har gitt deg {poeng} poeng av 3 mulige.")

pause()

print("TAKK FOR AT DU SPILTE DETTE VIDUNDERLIGE SPILLET!!!")
