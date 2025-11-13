# OpdrachtProgrammingInPython

## Probleemstelling

De plaatselijke jeugdbeweging doet beroep op kookouders en leiders om een kamp in goede banen leiden. 
Deze personen schieten dikwijls iets voor als ze naar de winkel gaan. 
In het verleden is het gebleken dat de terugbetaling dikwijls erg lang op zicht liet wachten.
Ook zorgde het laat binnenbrengen van bonnetjes door de leiders en de kookouders ervoor dat men geen
overzicht meer had van de totale kosten van het kamp.

## Tool

Deze tool moet er voor zorgen dat leiders en kookouders zich gemakkelijk kunnen registreren in het systeem.
Het registreren zorgt er ook voor dat hun bankrekening gekend is in het systeem.
Dit kan dus een spoedige terugbetaling mogelijk maken. 

Nadat een persoon geregistreerd is, is het mogelijk om een uitgave toe te voegen in het systeem. 
Een persoon kan al zijn uitgaven opvragen om bijvoorbeeld er zeker van te zijn dat hij alle 
kasticketjes nog heeft.
Verder is het ook mogelijk om alle uitgaven in een csv te downloaden. Dit moet er voor zorgen dat de
verantwoordelijken ten alle tijde weten hoeveel het kamp zal kosten. 


## Hoe uit te voeren

1. Clone de repository of donwnload de code

2. Plaats de meegeleverde SQLite database in de repository map

3. Mocht u de naam van de SQLite database veranderen doe dan ook in het dbinteractie script in de de DB module.

def get_connection() -> sqlite3.Connection:
    dbNaam = **'Uitgaventest.db'**
    conn = sqlite3.connect(dbNaam)
    return conn 
    
4. Maak een virtuele omgeving:
    python -m venv .venv

5. Installeer de externe bibliotheken:
    pip install -r requiements.txt

6. Voer de code uit:
    python main.py
    
    
## Op de planning 
- verwijderen van personen en uitgaven
- invoeren van try & except blokken
- verdere gegevens controle bij invoer

