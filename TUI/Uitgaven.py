# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 18:16:27 2025

@author: Aaron.Bruneel
"""
import sys
import Model.Persoon
import DB.dbinteractie
import datetime
import Model.Uitgave

def hoofdmenu():
    print("""Maak een keuze uit één van onderstaande mogelijkheden 
          geef het nummer van je keuze in en druk op enter:
          1. Print lijst van alle uitgaven
          2. Print lijst van de uitgaven van een specifiek persoon
          3. Maak nieuwe persoon aan
          4. Geef een nieuwe uitgave in
          5. Verlaat programma""")
          
    keuze = int(input("Maak je keuze: \n"))
    if keuze == 1:
        DB.dbinteractie.alleUitgaven()
    elif keuze == 2:
        printPerPersoon()
    elif keuze == 3:
        persoonToevoegen()
    elif keuze == 4:
        uitgaveToevoegen()
    elif keuze == 5:
        sys.exit(0)
    else:
        print('geef een nummer van 1 tot 5')

def persoonToevoegen():
    
    naam = input("Voer je voornaam en acthernaam in: ").lower()
    bankrekeningnr = input("Voer je bankrekeningnummer in: ")
    functie = input("Voer je funtie in (bijvoorbeeld: leider,kok,...): ")
    if DB.dbinteractie.persoonAanwezigInDb(naam):
        print('Je bestaat reeds in het systeem')
    else:
        persoon = Model.Persoon.Persoon(naam, bankrekeningnr, functie)
        DB.dbinteractie.persoontoevoegendb(persoon)
        print(f" {naam} werd toegevoegd aan de database!")
    
def uitgaveToevoegen():
    
    naam = input("Voer je voornaam en acthernaam in: ").lower()
    if  not DB.dbinteractie.persoonAanwezigInDb(naam):
        print('Deze persoon bestaat nog niet in de database, gelieve je eerst toe te voegen (keuze 3)')
    else:
        bedrag = float(input("Voer het bedrag in: "))
        jaar = int(input("Voer het jaar in(bijvoorbeeld: 2025)"))
        maand = int(input("Voer de maand in(bijvoorbeeld: 05)"))
        dag = int(input("Voer de dag in(bijvoorbeeld: 15)"))
        datum = datetime.date(jaar,maand,dag)
        uitgave = Model.Uitgave.Uitgave(naam,bedrag,datum)
        DB.dbinteractie.uitgaveToevoegendb(uitgave)
        print("Uitgave werd toegevoegd")
        
def printPerPersoon():
    naam = (input("Voer je voornaam en acthernaam in: ")).lower()
    DB.dbinteractie.uitgavenPerPersoon(naam)
