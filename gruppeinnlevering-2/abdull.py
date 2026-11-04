import time
import sys

# skrive effekter
def typewrite(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
def typeInput(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    value = input()
    return value

# Pause og mellomrom mellom tekstblokker
def pause ():
    print()
    time.sleep(1)
    print()

# spørsmål loop.
def hent_valg(spørsmål):
    while True:
        svar = input(spørsmål).strip().upper()
        if svar == "A" or svar == "B":
            return svar
        print ("Ugyldig valg. Skriv A eller B.")

# Variabler
valg1 = ""
Valg2 = ""
Valg3 = ""
poeng = 0

#Intro
print("=" * 25)
print("    STORM I TEAMET   ")
print("=" * 25)
pause()
typewrite("Erling er prosjektleder i et team som skal lage en ny medborgerportal. \nProsjekt gruppen opplever noen problemer med gruppedynamikk og uenighet innad i prosjektet. \nFlere grupper med ulike arbeidserfaringer og ekspertiser begynner å kollidere. \nProsjektet med inspirerende oppstart og høy energi, merker sine første utfordringer. ")
pause()
typewrite("Det har gått 6 uker siden prosjektet startet og Erling har nettopp samlet teamet for første gang.\nEtter et møte med mye engasjement og diskusjon, har Erling fått inntrykk av at det er flere \nkonflikter i teamet som må løses for å få prosjektet på rett spor igjen.")
pause()
typewrite("Det er viktig at dette løser seg ganske fort ettersom første prototype skal være klar om tre uker. \nKommunikasjonen hakker, og stemningen er spent.")
pause()
typewrite("Prosjekt leder Erling vet at de neste valgene han tar bestemmer om de klarer å nå dette målet. \nKlarer dette teamet å levere ferdig prototype om tre uker, og klarer de å \ngå ut av stormingsfasen og inn i normingsfasen? ")
pause()
typeInput("[Trykk enter for å fortsette...]")

#Konflikt 1 #
pause()
print("=" * 27)
print("KONFLIKT #1: SILJE OG ELIAS")
print("=" * 27)
pause()
typewrite("Den første konflikten Erling må prøve å løse er mellom UX-designer Silje og IT-rådgiver Elias. \nSilje og Elias er uenig om teknologivalg. Silje har designet et forslag til IT-rådgiverne")
pause()
typewrite("Elias mener dette er alt for dyrt, usikkert og urealistisk.")
pause()
typewrite("Silje mener det Elias foreslår vil låse brukeropplevelsen og hindre innovasjon")
pause()
typewrite("Argumentene begynner å bli personlige og Silje og Elias begynner å snakke om hverandre i stedet for sak. \nDe begynner også å rekruttere andre i teamet til sin side...")
pause()
typeInput("[Trykk enter for å fortsette...]")
print()
typewrite("Prosjektleder Erling har nå 2 måter han kan prøve å løse konflikten slik at prosjektet kan gå videre:")
pause()
typewrite("[A]: Holde individuelle møter med hver av dem for å forstå deres perspektiver.")
pause()
typewrite("[B]: Ta opp konflikten direkte i plenum og be teamet om å finne en løsning sammen.")
pause()
typewrite("Hva bør Erling gjøre? (A/B)")
print()

# Valg 1
valg1 = hent_valg("Svar: ")
if valg1 == "A":
    poeng = poeng + 2
    print()
    typewrite("Erling velger å gå for individuelle samtaler med Silje og Elias i et håp for å dempe temperaturen. \nUnder samtalen har Erling stramme rammer, slik at begge parter føler at de blir tatt på alvor. \nErling ber dem å forklare hva de trenger for å løse dette og ikke hva de er imot.")
    pause()
    typewrite("Han anerkjenner begges behov, men er stram på at personangrep og rekrutering av andre er ikke greit,\nettersom dette fører til en splitting i teamet.")
    pause()
    typewrite("Han anerkjenner at Silje har et poeng når det gjelder fleksibilitet og god brukeropplevelse,\nmen at Elias har et poeng når det gjelder kostnader og risiko.")
    pause()
    typewrite("Erling ber dem å komme med forslag til en løsning som ivaretar begge parters behov.")
    pause()
    typewrite("[UTFALL]:Konflikten blir løst men det tar litt tid.")
else:
    print()
    typewrite("Erling velger å ta opp konflikten i plenum ...")
    pause()
    typewrite("Alle kommer med ideer og drøfter fordeler og ulemper med begge ideene.\nSilje og Elias får senen for å forklare hva de tenker og mener er lurest.")
    pause()
    typewrite("De føler at de må forsvare seg selv foran kollegaene sine.")
    pause()
    typewrite("Erling mener dette bør avgjøres på flertallsvedtak. \nDette fører til at konflikten eskalerer og teamet blir delt i to leire...")
    pause()
    typewrite("[UTFALL]:konflikten forsterkes og kommunikasjonen svekkes.")

pause()
typeInput("[Trykk enter for å fortsette...]")

#Konflikt 2 #
pause()
print("=" * 30)
print("KONFLIKT #2: HAMDI OG HALLGEIR")
print("=" * 30)
pause()
typewrite("Det er ikke bare Silje og Elias som bemerker seg problemer under dette prosjektet. \nTre uker senere havner også Hamdi i kulturavdelingen og Hallgeir som er brukerrepresentant i konflikt.")
pause()
typewrite("Hamdi ønsker en mer restriktiv og kontrollert løsning for innbyggernes innspill, \nmens Hallgeir ønsker en mer åpen og dialogstyrt løsning med rom for spontane innspill")
pause()
typewrite("Hamdi sin løsning er billigere, men vil gi mindre innsikt og legitimitet blant innbyggerne.\nHallgeir sin er dyrere, men vil gi mer innsikt og medvirkning blant innbyggerne.")
pause()
typeInput("[Trykk enter for å fortsette...]")
pause
typewrite("Prosjektleder Erling har igjen 2 måter han kan prøve å løse denne konflikten slik at prosjektet kan gå videre:")
pause()
typewrite("[A]: Holde et felles møte med hele teamet for å avklare uenigheter.")
pause()
typewrite("[B]: La Hamdi og Hallgeir jobbe sammen for å finne en løsning på egen hånd.")
pause()
typewrite("Hva bør Erling gjøre? (A/B)")
print()

# Valg 2
valg2 = hent_valg("Svar: ")
if valg2 == "A":
    poeng = poeng + 2
    print()
    typewrite("Erling samler teamet for et fagmøte for å ta opp problemet og prøve å komme på en måte slik at alle blir fornøyde")
    pause()
    typewrite("Under møtet får alle en mulighet til å uttrykke sine synspunkter og forstå hverandres perspektiver.")
    pause()
    typewrite("Brukerrepresentant Jabir og politisk rådgiver Marcia kom med en idé med å inngå et kompromiss.")
    pause()
    typewrite("Jabir og Marcia vurderte et kompromiss som legger opp for en strukturert kanal med faste \ninnspillsrunder kombinert med åpen dialogdel.")
    pause()
    typewrite("[UTFALL]:Teamet finner en løsning som ivaretar flere interesser og styrker samarbeidet,\nmen løsningen krever mer planlegging og kan føre til at prototypen blir forsinket")
else:
    poeng = poeng + 1
    print()
    typewrite("Erling velger å la Hamdi og Hallgeir finne en løsning på egen hånd. Han håper at de klarer å \nsamarbeide og inngå et kompromiss uten hans hjelp.")
    pause()
    typewrite("Hamdi og Hallgeir har en lang diskusjon og prøver å forstå hverandres perspektiver. \nDe innser at de begge har gode poeng, men sliter med å nå en enighet.")
    pause()
    typewrite("[UTFALL]:beslutningene blir forsinket. Samarbeidet svekkes men det er bedre kommunikasjon i teamet")
pause()
typeInput("[Trykk enter for å fortsette...]")
    # Konflikt 3 #
pause()
print("=" * 40)
print("KONFLIKT #3: MOTIVASJON ELLER FREMDRIFT")
print("=" * 40)
pause()
typewrite("Det er nå 1 uke igjen til prototypen må leveres.\nTeamet er slitne og kommunikasjonen begynner å bli kjølig.\nFolk sender e-post fremfor å snakke med hverandre, og det er tydelig at motivasjonen er lav.")
pause()
typeInput("[Trykk enter for å fortsette...]")
pause()
typewrite("Erling må igjen ta en avgjørelse:")
pause()
typewrite("[A]: Fokusere på å motivere teamet og skape en positiv stemning.")
pause()
typewrite("[B]: Fokusere på å få fremdrift og sikre at prototypen blir levert i tide.")
pause()
typewrite("Hva bør Erling gjøre? (A/B)")
print()


# Valg 3
valg3 = hent_valg("Svar: ")
if valg3 == "A":
    poeng = poeng + 2
    print()
    typewrite("Erling velger å fokusere på motivasjon og skape en positiv stemning i teamet.\nHan arrangerer en grill-kveld hos han og gir ros for det arbeidet som er gjort så langt.")
    pause()
    typewrite("Dette fører til at teamet føler seg verdsatt og motivert til å jobbe hardt for å levere prototypen i tide.")
    pause()
    typewrite("[UTFALL]:Teamet blir mer motivert og samarbeidet styrkes, Prototypen blir levert i tide.")
else:
    poeng = poeng + 1
    print()
    typewrite("Erling velger å fokusere på fremdrift og sikre at prototypen blir levert i tide.\nHan setter stramme tidsfrister og følger opp teamet tett for å sikre at arbeidet blir gjort.")
    pause()
    typewrite("Dette fører til at teamet føler seg presset og stresset, men prototypen blir levert i tide.")
    pause()
    typewrite("[UTFALL]:Prototypen blir levert i tide, men samarbeidet og motivasjonen svekkes.")

pause()
typeInput("[Trykk enter for å fortsette...]")    

# Avslutning
pause()
print("=" * 25)
print("        AVSLUTNING        ")
print("=" * 25)

# utfall basert på poengsum
if poeng >= 5:
    pause()
    typewrite("Erling har tatt gode valg som har styrket samarbeidet og motivasjonen i teamet.\nPrototypen ble levert i tide, og teamet har gått over i normingsfasen og blitt et velfungerende team.\nGratulerer!!!")
    print()
elif poeng >= 3:
    pause()
    typewrite("Erling har tatt noen gode valg som har gjort at\nprototypen ble levert i tide, men samarbeidet, kommunikasjonen og motivasjonen trenger forbedring.\nTeamet blir igjen i stormingsfasen!")
    pause()
else:
    pause()
    typewrite("Erling har tatt noen valg som har svekket samarbeidet og motivasjonen i teamet.\nPrototypen deres var skuffende, teamet ble løst opp noen måneder senere :(")
    pause()

# Oppsumering av poeng
pause()
typewrite("Dine valg har gitt deg en poengsum som reflekterer hvordan du håndterte konfliktene i teamet.")
pause()
typewrite(f"Du fikk: {poeng} poeng av 6 mulige.")
pause()
typewrite("Takk for at du spilte!")
pause()
typeInput("[Trykk enter for å avslutte...]")