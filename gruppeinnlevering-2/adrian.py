import time
import sys

suksess_tall : float = 0.0


def typewrite(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def typeinput(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    value = input()
    return value

def pause(time_amount = 1.0):
    print()
    time.sleep(time_amount)
    print()

def hent_valg(spørsmål):
    while True:
        svar = input(spørsmål).strip().upper()
        if svar == "A" or svar == "B":
            return svar
        print("Beklager, ugyldig svar!")


typewrite("Kaos i teamet!")

typewrite("""
Erling er prosjektleder og skal lage et ny medborgerportal. 
Dessverre opplever teamet en del problemer med gruppedynamikken, og dette påvirker prosjektet.
Arbeidserfaringer og prioriterer begynner å kollidere og risikerer å påvirke den første prototypen.
""")

pause()

typewrite("""
Nå som det har gått seks uker siden prosjektet startet, har Erling samlet opp teamet for første gang.
Teamet virket høyengasjert på starten, men snart opplever gruppen komplikasjoner og møter sine første reele utfordringer.

Erling legger merke til at frustrasjonen øker. Det er viktig at dette løser seg fort i tide.
Valgene Erling tar kan mekke eller brekke prosjektet. Det står mye på spill, og det henger flere millioner kroner i balansen.
""")

typeinput("""
ER DU KLAR?

""")

typewrite("SPILLER INGEN ROLLE, LETS GO.")
pause(2.0)
typewrite("""
Erling kommer til kontoret en dag, der den første store konflikten gjennomgår.
UX-Designer Silje og IT-rådgiver Elias har befinnet seg selv i en stor krangel.
Silje har anlagt en forslag og fremmet det til IT-teamet, men Elias mener at dette er en altfor
dyr løsning.
Silje derimot mener at Elias sitt forslag er restriktiv for brukeropplevelsen og hindrer innovasjon.
""")
pause(2.0)
typewrite("""
Her er løsningene som Erling kommer opp med.

Alternativ A: Gjennomfør individuelle samtaler.
Alternativ B: Ta opp konflikten direkte i plenum og ber teamet avgjøre hvilket som er best.

""")

pause(1.0)
resultat = hent_valg("Hva skal Erling velge? (A / B) ")
if resultat == "A":
    typewrite("""
    Erling velger å gå for individuelle samtaler med Silje og Elias i et håp for å dempe temperaturen. 
    Under samtalen har Erling stramme rammer, slik at begge parter føler at de blir tatt på alvor. 
    Erling anerkjenner deres begges behov, men er stram på at personangrep og rekrutering av andre er ikke greit, 
    ettersom dette fører til en splitting i teamet. Erling anerkjenner at Silje har et poeng når det gjelder fleksibilitet og god bruker opplevelse, men at Elias har et godt poeng for sikkerhet og kostnad. 
    Erling ber dem å forklare hva de trenger for å løse dette og ikke hva de er imot.
    Konflikten løses, men tar litt tid.
    """)
    suksess_tall += 1
elif resultat == "B":
    typewrite("""
    Erling går for å samle teamet til et møte for å ta opp problemet i plenum. 
    Alle kommer med ideer og drøfter med fordeler og ulemper med begge ideene. 
    Silje og Elias får senen for å forklare hva de tenker og mener er lurest. Silje og Elias føler også at 
    de må forsvare seg selv foran kollegaene sine. 
    Erling mener dette bør avgjøres på flertallsvedtak, selv om det kan føre til splitting i gruppen, 
    ettersom en avgjørelse med flerstemmer fører til vinnere og tapere.
    Konflikten forsterkes og kommunikasjonen svekkes.
    """)
    suksess_tall -= 1


pause(2.0)

typewrite("""
Å nei å nei, det oppstår et nytt konflikt blant kollegaene!

Tre uker senere havner også Hamdi i kulturavdelingen og Hallgeir som er brukerrepresentant i konflikt. 
Hamdi ønsker en mer restriktiv og kontrollert løsning for innbyggernes innspill, mens Hallgeir ønsker en mer åpen og dialogstyrt løsning med rom for spontane innspill. 
Hamdi sin løsning er billigere, men vil gi mindre innsikt og legitimitet blant innbyggerne. 
Hallgeirs løsning derimot, er dyrere, men vil gi mer innsikt og medvirkning blant innbyggerne.
""")
pause(1.0)
typewrite("""
Da kommer Erling med to spennende alternativer til å løse denne problemstillingen.

Alternativ A: Arranger et felles møte for å avklare uenigheter.
Alternativ B: La Hamdi og Hallgeir finne ut av konflikten på egenhånd.
""")
pause()
resultat = hent_valg("Hva skal Erling gjøre? (A/B) ")
if resultat == "A":
    typewrite("""
    Erling samler teamet for et fagmøte for å ta opp problemet og prøve å komme på en måte slik at alle blir fornøyde. 
    Brukerrepresentant Jabir og politisk rådgiver Marcia kom med en idé med å inngå et kompromiss. 
    Erling var fornøyd med dette, han tenkte på at et kompromiss er bedre enn et flertallsvedtak. 

    Teamet finner en løsning som ivaretar flere interesser og styrker samarbeidet, men løsningen krever mer planlegging og kan føre til at prototypen blir forsinket.
    """)
    suksess_tall += 1.0
elif resultat == "B":
    typewrite("""
    Erling velger å la Hamdi og Hallgeir finne en løsning på egen hånd. Han håper at de klarer å samarbeide og inngå et kompromiss uten hans hjelp. 
    Hamdi og Hallgeir diskuterer flere muligheter, men sliter med å bli enige. 
    Hamdi ønsker fortsatt en kontrollert løsning, mens Hallgeir ønsker større åpenhet og medvirkning fra innbyggerne.

    Beslutningene blir forsinket, og at samarbeidet svekkes. Teamet risikerer å ikke bli ferdig med prototypen innen fristen. 
    Samtidig får Hamdi og Hallgeir mulighet til å ta ansvar og utvikle evnen til å løse konflikter selv.
    """)
    suksess_tall -= 1.0

pause()

typewrite("""
Nå lurer Erling på hvordan han skal bevare og opprettholde gruppedynamikken og motivasjonen for prosjektet.
Han stusser mellom å prioritere sosiale aktiviteter med teamet eller sette fullt fokus på fremdrift på å levere tjenesten.

Hva skal han gjøre?

Alternativ A: Sette av tid til en sosial aktivitet for teamet.
Alternativ B: Prioritere fremdrift og leveransen fremfor sosiale aktiviteter.
""")
pause()

resultat = hent_valg("Hva skal Erling gjøre? (A/B) ")
if resultat == "A":
    typewrite("""
    Erling inviterer til en grill kveld på terrassen hjemme hos han. 
    Han håper at teamet kan bli mer kjent med hverandre utenfor arbeidssituasjonen. 
    Han håper at en sosial aktivitet kan styrke samholdet og bidra til at teamet kommuniserer bedre. 
    Erling sørger for en inkluderende kveld, slik at ingen føler seg utenfor. Relasjonene og motivasjonen øker, og samarbeidet blir bedre. 
    Teamet blir tryggere på hverandre og det blir lettere å ta opp uenigheter på en konstruktiv måte. Noen kan også føle 
    at dette tar tid fra viktige arbeidsoppgaver, særlig når fristen nærmer seg.

    """)
    suksess_tall += 1.0
elif resultat == "B":
    typewrite("""
    Erling velger å prioritere prosjektarbeidet fremfor sosiale aktiviteter. Han setter tydelige mål, fordeler arbeidsoppgavene 
    og følger opp fremdriften gjennom faste møter. 
    Han prioriterer arbeidet for å sikre at prototypen blir ferdig innen fristen.
    Teamet får bedre tid til å jobbe med prosjektet. For stort fokus på prosjektet fører til økt stress og redusert motivasjon. 
    Ettersom teamet ikke får tid til å bygge relasjoner, kan samarbeidet bli dårligere over tid.

    """)
    suksess_tall -= 1.0

pause(2.0)

typewrite("""
Du har nå kommet til slutten. Du har behersket konflikter, løst problemer, og tjent penger.
Framtiden til Erlings bedrift fremviser seg...
""")
pause(3.0)
typewrite("nå.")
pause(2.0)

# HURRA SUKSESS
if suksess_tall >= 3.0:
    typewrite("""
    Teamet får levert prototypen innen fristen. 
    Erling retter konfliktene tidlig og legger rette for åpen kommunikasjon. 
    Teamet finner en balanse mellom teknologi, brukeropplevelse og sikkerhet. 
    De får gode innspill fra test brukere både fra åpen dialog og faste innspillsrunder. 
    Tilliten øker, gode relasjoner er bygget, motivasjonen øker og teamet beveger seg mot normingsfasen.
    
    Gratulerer.
    """)

# Å NEI IKKE SUKSESS
elif suksess_tall <= 0.0:
    typewrite("""
    Prosjektet stoppes opp og utfordringene i teamet blir større.  Flere blir passive, eller trekker seg ut. 
    De forblir i storming fasen.
    """)

else:
    typewrite("""
    Teamet leverer prototypen innen fristen, men teamet er fremdeles sårbart. Erling løser noen av konfliktene, men uenigheter gjenstår. Samarbeidet er litt bedre enn før, men de trenger fortsatt oppfølging av Erling. 
    Teamet gå ikke videre til normingsfasen.
    """)
