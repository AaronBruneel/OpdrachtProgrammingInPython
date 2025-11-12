# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 18:16:27 2025

@author: Aaron.Bruneel
"""
import sys
import Model.Persoon
import DB.dbinteractie

def hoofdmenu():
    print("""maak een keuze uit één van onderstaande en mogelijkheden en geef het nummer in:
          1. Print lijst van alle uitgaven
          2. Print lijst van de uitgaven van een specifiek persoon
          3. Maak nieuwe persoon aan
          4. Geef een nieuwe uitgave in
          5. verlaat programma""")
          
    keuze = int(input("Maak je keuze: \n"))
    if keuze == 1:
        print("deze functie werkt nog niet")
        #functie invoegen
    elif keuze == 2:
        print("deze functie werkt nog niet")
        #functie invoegen
    elif keuze == 3:
        persoonToevoegen()
    elif keuze == 4:
        uitgaveToevoegen()
    elif keuze == 5:
        sys.exit(0)
    else:
        print('geef een nummer van 1 tot 5')

def persoonToevoegen():
    
    naam = input("Voer de naam van de persoon in: ")
    bankrekeningnr = input("Voer het bankrekeningnummer in: ")
    functie = input("Voer de functie van de persoon in: ")
    if DB.dbinteractie.persoonAanwezigInDb(naam):
        print('deze persoon bestaat reeds')
    else:
        persoon = Model.Persoon.Persoon(naam, bankrekeningnr, functie)
        DB.dbinteractie.persoontoevoegendb(persoon)
        print(f"Persoon {naam} toegevoegd aan de database!")
    
def uitgaveToevoegen():
    
    naam = input("Voer de naam van de persoon in: ")
    if  DB.dbinteractie.persoonAanwezigInDb(naam):
        print('Deze persoon bestaat nog niet in de database, gelieve deze eerst toe te voegen (keuze 3)')
    else:
        print('ok')
        
        