import pymongo

client = pymongo.MongoClient("mongodb+srv://gireesh22:mitravinda22@cluster0.su6prrl.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"gireesh",
    "email" : "hari.giree2014@gmail.com",
    "surname" : "pattem"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

