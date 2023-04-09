import pymongo
client = pymongo.MongoClient("mongodb+srv://mongo:root@cluster1.7xujqpz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "id":120,
    "name":"harshavardhan",
    "surname":"magala",
    "email":"gunasekhar@gmail.com"
}
l = [1, 2, 3, 4]
print(l)
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)