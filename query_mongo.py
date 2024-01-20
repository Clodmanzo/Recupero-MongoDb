from pymongo import MongoClient

# Connessione al server MongoDB
def mongo_con(stringa_conn, nome_db, nome_collection):
    client = MongoClient(stringa_conn)
    db = client[nome_db]
    collection = db[nome_collection]
    return collection



# Tutti i ristoranti
def query1(collection):
    result = collection.find()
    return result

#nome e città ristoranti      
def query2(collection):
    result = collection.find({}, {"nome": 1, "città": 1, "_id": 0})
    return result

#ristoranti min 2 stelle
def query3(collection):
    result= collection.find({"stelle": {"$gte": 2}})
    return result

#ristoranti con cucina italiana
def query4(collection):
    result= collection.find({"cucina": "italiana"})
    return result

#prezzo <250eur
def query5(collection):
    result= collection.find({"prezzo": {"$lt": 250}})
    return result

#con cucina sperimentale o innovativa
def query6(collection):
    result= collection.find({"cucina": {"$in": ["sperimentale", "innovativa"]}})
    return result

#con cucina italiana a Roma o Firenze
def query7(collection):
    result=  collection.find({"cucina": "italiana", "$or": [{"città": "Roma"}, {"città": "Firenze"}]})
    return result

#con tre stelle e prezzo < 250 euro
def query8(collection):
    result= collection.find({"stelle": 3, "prezzo": {"$gt": 250}})
    return result

#con cucina alpina o mare in città che iniziano con S
def query9(collection):
    result= collection.find({"$and": [{"$or": [{"cucina": "alpina"}, {"cucina": "mare"}]}, {"città": {"$regex": "^S"}}]})
    return result

# Numero di ristoranti per ogni città in ordine decrescente
def query10(collection):
    result= collection.aggregate([
    {"$group": {"_id": "$città", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
    ])
    return result
