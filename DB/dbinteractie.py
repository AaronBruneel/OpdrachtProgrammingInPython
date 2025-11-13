# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 18:46:43 2025

@author: Aaron.Bruneel
"""

import sqlite3
from Model.Persoon import Persoon
import pandas 

def get_connection():
    dbNaam = 'Uitgaventest.db'
    conn = sqlite3.connect(dbNaam)
    return conn

def persoontoevoegendb(persoon: Persoon):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            INSERT INTO Persoon
            (Naam, Bankrekeningnr, Functie)
            VALUES (?, ?, ?)
            """, (persoon.naam, persoon.bankrekeningnr, persoon.functie))
    conn.commit()
    conn.close()   


def persoonAanwezigInDb(naam):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
             "SELECT naam FROM Persoon WHERE naam = ?", (naam,))
    gevonden = cursor.fetchone()
    conn.close()   
    return gevonden is not None

def uitgaveToevoegendb(uitgave):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            INSERT INTO Uitgave
            (Naam, Bedrag, Datum)
            VALUES (?, ?, ?)
            """, (uitgave.naam, uitgave.bedrag, uitgave.datum))
    conn.commit()
    conn.close() 
    
def alleUitgaven():
    conn = get_connection()
    query = "SELECT * FROM Uitgave"
    dataframe= pandas.read_sql_query(query, conn)
    dataframe.to_csv('output.csv', index=False)
    conn.close() 
    