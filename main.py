from query_mongo import *
from prettytable import PrettyTable


stringa_conn = 'mongodb+srv://Clodmanzo:Killermanzo98@cluster0.xmk9ncr.mongodb.net/'
nome_db = 'Recupero'
nome_collection = 'Recupero_collection'

documenti_ristoranti= mongo_con(stringa_conn, nome_db, nome_collection)



# Menù iniziale
def main_menu(documenti_ristoranti):
    while True:
        print("\n-- Guida Ristoranti --\n")
        print("- 1. Info Tutti i Ristoranti")
        print("- 2. Nomi e Città Ristoranti")
        print("- 3. Min 2 Stelle")
        print("- 4. Con Cucina Italiana")
        print("- 5. Con Prezzo < eur250")
        print("- 6. Con Cucina Sperimentale o Innovativa")
        print("- 7. Con Cucina Italiana a Roma o Firenze")
        print("- 8. Con 3 stelle e Prezzo < eur250")
        print("- 9. Con cucina alpina o mare in città che iniziano con S")
        print("- 10. Numero di ristoranti per ogni città in ordine decrescente")
        
        print("----------\n- 4. Esci\n----------")

        scelta = input("\nSeleziona un'opzione:\n-  ")

        if scelta == "1":
            risultato = query1(documenti_ristoranti)
            tabella = PrettyTable()
            tabella.title = 'RISTORANTI'
            tabella.field_names = ["Nome", "Città", "Stelle", "Cucina", "Prezzo"]

            for doc in risultato:
                prezzo_formattato = f"€{doc.get('prezzo')},00"
                tabella.add_row([doc.get("nome"), doc.get("città"), doc.get("stelle"), doc.get("cucina"), prezzo_formattato])

            print(tabella)
              
        elif scelta == "2":
            risultato = query2(documenti_ristoranti)
            tabella = PrettyTable()
            tabella.title = 'RISTORANTI'
            tabella.field_names = ["Nome", "Città"]

            for doc in risultato:
                tabella.add_row([doc.get("nome"), doc.get("città")])

            print(tabella)       

     
        elif scelta == "3":
            risultato = query3(documenti_ristoranti)
            tabella = PrettyTable()
            tabella.title = 'RISTORANTI MIN 2 *'
            tabella.field_names = ["Nome", "Città", "Stelle", "Cucina", "Prezzo"]

            for doc in risultato:
                prezzo_formattato = f"€{doc.get('prezzo')},00"
                tabella.add_row([doc.get("nome"), doc.get("città"), doc.get("stelle"), doc.get("cucina"), prezzo_formattato])

            print(tabella)


        elif scelta == "4":
            risultato = query4(documenti_ristoranti)
            tabella = PrettyTable()
            tabella.title = 'RISTORANTI CON CUCINA ITALIANA'
            tabella.field_names = ["Nome", "Città", "Stelle", "Cucina", "Prezzo"]

            for doc in risultato:
                prezzo_formattato = f"€{doc.get('prezzo')},00"
                tabella.add_row([doc.get("nome"), doc.get("città"), doc.get("stelle"), doc.get("cucina"), prezzo_formattato])

            print(tabella)


        elif scelta == "5":
            risultato = query5(documenti_ristoranti)
            tabella = PrettyTable()
            tabella.title = 'RISTORANTI CON PREZZO < EUR 250'
            tabella.field_names = ["Nome", "Città", "Stelle", "Cucina", "Prezzo"]

            for doc in risultato:
                prezzo_formattato = f"€{doc.get('prezzo')},00"
                tabella.add_row([doc.get("nome"), doc.get("città"), doc.get("stelle"), doc.get("cucina"), prezzo_formattato])

            print(tabella)


        elif scelta == "6":
            risultato = query6(documenti_ristoranti)
            tabella = PrettyTable()
            tabella.title = 'RISTORANTI SPERIMENTALI O INNOVATIVI'
            tabella.field_names = ["Nome", "Città", "Stelle", "Cucina", "Prezzo"]

            for doc in risultato:
                prezzo_formattato = f"€{doc.get('prezzo')},00"
                tabella.add_row([doc.get("nome"), doc.get("città"), doc.get("stelle"), doc.get("cucina"), prezzo_formattato])

            print(tabella)

        elif scelta == "7":
            risultato = query7(documenti_ristoranti)
            tabella = PrettyTable()
            tabella.title = 'RISTORANTI ITAIANI A ROMA O FIRENZE'
            tabella.field_names = ["Nome", "Città", "Stelle", "Cucina", "Prezzo"]

            for doc in risultato:
                prezzo_formattato = f"€{doc.get('prezzo')},00"
                tabella.add_row([doc.get("nome"), doc.get("città"), doc.get("stelle"), doc.get("cucina"), prezzo_formattato])

            print(tabella)

        elif scelta == "8":
            risultato = query8(documenti_ristoranti)
            tabella = PrettyTable()
            tabella.title = 'RISTORANTI CON 3* PREZZO < EUR 250'
            tabella.field_names = ["Nome", "Città", "Stelle", "Cucina", "Prezzo"]

            for doc in risultato:
                prezzo_formattato = f"€{doc.get('prezzo')},00"
                tabella.add_row([doc.get("nome"), doc.get("città"), doc.get("stelle"), doc.get("cucina"), prezzo_formattato])

            print(tabella)

        elif scelta == "9":
            risultato = query9(documenti_ristoranti)
            tabella = PrettyTable()
            tabella.title = 'RISTORANTI CON CUCINA ALPINA O MARE IN CITTÀ S...'
            tabella.field_names = ["Nome", "Città", "Stelle", "Cucina", "Prezzo"]

            for doc in risultato:
                prezzo_formattato = f"€{doc.get('prezzo')},00"
                tabella.add_row([doc.get("nome"), doc.get("città"), doc.get("stelle"), doc.get("cucina"), prezzo_formattato])

            print(tabella)


        elif scelta == "10":
            risultato = query10(documenti_ristoranti)
            tabella = PrettyTable()
            tabella.title = 'RISTORANTI PER CITTÀ'
            tabella.field_names = ["Città", 'Count']

            for doc in risultato:
                tabella.add_row([doc["_id"], doc["count"]])

            print(tabella)



        


        elif scelta == "4":
            break
        else:
            print("\n--Scelta non valida.--\n")
        

if __name__=='__main__':
    main_menu(documenti_ristoranti)