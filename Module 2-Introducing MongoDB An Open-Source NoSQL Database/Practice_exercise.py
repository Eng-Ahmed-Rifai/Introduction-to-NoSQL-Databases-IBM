from pymongo import MongoClient
user = 'root'
password = 'MjE5MjgtZW5nYWht'
host='localhost'
#create the connection url
connecturl = f"mongodb://{user}:{password}@{host}:27017/?authSource=admin"

# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)

# select the 'training' database

db = connection.training

# select the 'mongodb_glossary' collection

collection = db.mongodb_glossary

# create a list document

doc = [
    {"database":"a database contains collections"},
    {"collection":"a collection stores the documents"},
    {"document":"a document contains the data in the form of key value pairs."}]

# insert a list document

print("Inserting a document into collection.")
db.collection.insert_many(doc)

# query for all documents in 'training' database and 'mongodb_glossary' collection

docs = db.collection.find()

print("Printing the documents in the collection.")

for document in docs:
    print(document)

# close the server connecton
print("Closing the connection.")
connection.close()