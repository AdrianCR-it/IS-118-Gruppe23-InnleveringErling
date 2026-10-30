
# Interaktiv historie - Erling
# IS-118 Gruppeoppgave 2

print("-----------------------------------")
print("       PROSJEKTET TIL ERLING")
print("-----------------------------------")

print("Erling er prosjektleder for et team som skal utvikle en digital løsning.")
print("Det har oppstått flere konflikter i teamet, og prototypen må leveres om tre uker.")
print("Nå må Erling ta noen viktige valg.")

# Beslutningspunkt 1
print("BESLUTNING 1: Silje og Elias er uenige.")
print("1. Snakke med Silje og Elias hver for seg.")
print("2. La hele teamet diskutere konflikten sammen.")

valg1 = input("Hva velger Erling? (1 eller 2): ")

if valg1 == "1":
    print("Erling snakker med begge hver for seg.")
    print("De forstår hverandres synspunkter bedre og blir enige om et kompromiss.")
elif valg1 == "2":
    print("Erling tar konflikten opp i et felles møte.")
    print("Diskusjonen blir mer anspent, og konflikten blir større.")
else:
    print("Ugyldig valg. Erling velger å snakke med dem hver for seg.")
    valg1 = "1"


# Beslutningspunkt 2
print("BESLUTNING 2: Hamdi og Hallgeir er uenige om brukermedvirkning.")
print("1. Arrangere et møte der de prøver å finne et kompromiss.")
print("2. La dem løse uenigheten på egen hånd.")

valg2 = input("Hva velger Erling? (1 eller 2): ")

if valg2 == "1":
    print("Erling arrangerer et møte.")
    print("De finner en løsning som kombinerer faste innspill og åpen dialog.")
elif valg2 == "2":
    print("Erling lar dem finne ut av problemet selv.")
    print("Uenigheten fortsetter, og prosjektet mister noe fremdrift.")
else:
    print("Ugyldig valg. Erling arrangerer et felles møte.")
    valg2 = "1"


# Beslutningspunkt 3
print("BESLUTNING 3: Teamet begynner å miste motivasjonen.")
print("1. Arrangere en sosial aktivitet for å styrke samholdet.")
print("2. Prioritere arbeidet og sette tydelige mål.")

valg3 = input("Hva velger Erling? (1 eller 2): ")

if valg3 == "1":
    print("Erling arrangerer en sosial aktivitet.")
    print("Teamet blir bedre kjent og får mer motivasjon.")
elif valg3 == "2":
    print("Erling prioriterer arbeidet.")
    print("Teamet får mer tid til oppgavene, men motivasjonen kan bli dårligere.")
else:
    print("Ugyldig valg. Erling arrangerer en sosial aktivitet.")
    valg3 = "1"


# Avslutning - vurderer valgene
print("-----------------------------------")
print("             SLUTTEN")
print("-----------------------------------")

# Alle tre gode valg
if valg1 == "1" and valg2 == "1" and valg3 == "1":
    print("TEAMET LYKKES!")
    print("Erling klarer å håndtere konfliktene og styrke samholdet.")
    print("Teamet samarbeider godt og leverer prototypen innen fristen.")

# Alle tre dårlige valg
elif valg1 == "2" and valg2 == "2" and valg3 == "2":
    print("PROSJEKTET MISTER FREMDRIFT!")
    print("Konfliktene fortsetter, og motivasjonen blir dårligere.")
    print("Teamet sliter med samarbeidet, og prosjektet blir forsinket.")

# Alle andre kombinasjoner
else:
    print("DELVIS SUKSESS!")
    print("Erling klarer å løse noen av utfordringene.")
    print("Teamet gjør fremskritt, men har fortsatt utfordringer.")
    print("Prototypen blir levert, men samarbeidet trenger mer arbeid.")

print("Takk for at du spilte!")
