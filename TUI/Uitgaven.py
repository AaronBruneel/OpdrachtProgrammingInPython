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
          4. geef uitgave in
          5. verlaat programma""")
          
    keuze = int(input("Maak je keuze: \n"))
    if keuze == 1:
        print("deze functie werkt nog niet")
        #functie invoegen
    elif keuze == 2:
        print("deze functie werkt nog niet")
        #functie invoegen
    elif keuze == 3:
        persoontoevoegen()
        #functie invoegen
    elif keuze == 4:
        print("deze functie werkt nog niet")
        #functie invoegen
    elif keuze == 5:
        sys.exit(0)
    else:
        print('geef een nummer van 1 tot 5')

def persoontoevoegen():
    """Vraagt de gebruiker om gegevens en voegt een persoon toe aan de database."""
    naam = input("Voer de naam van de persoon in: ")
    bankrekeningnr = input("Voer het bankrekeningnummer in: ")
    functie = input("Voer de functie van de persoon in: ")
    
    persoon = Model.Persoon.Persoon(naam, bankrekeningnr, functie)
    DB.dbinteractie.persoontoevoegendb(persoon)
    
    print(f"Persoon {naam} toegevoegd aan de database!")