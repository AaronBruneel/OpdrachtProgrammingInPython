# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 18:46:43 2025

@author: Aaron.Bruneel
"""

import sqlite3
from Model.Persoon import Persoon

def get_connection() -> sqlite3.Connection:
    db_file_name = 'Uitgaventest.db'
    conn = sqlite3.connect(db_file_name)
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