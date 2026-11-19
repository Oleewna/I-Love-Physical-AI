import impianto

class ImpiantoSolare:
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str):
        self.codice = codice
        self.modello = modello
        self.localita = localita
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        self.pannelli = [PannelloFotovoltaico]
    
    def aggiungi_pannello(pannello: PannelloFotovoltaico):
        self.pannelli.append(pannello)
        
    del potenza_pannelli():
        somma = 0
        for pannello in self.pannelli:
            somma += pannello.potenza_massima_kw
        return somma
    
    def cerca_pannello(codice: str):
        for pannello in self.pannelli:
            if pannello.codice == codice:
                return pannello.codice
            else:
                return None
            
    #def rimuovi_pannello
            
    #pannelli_sotto_potenza
            
        