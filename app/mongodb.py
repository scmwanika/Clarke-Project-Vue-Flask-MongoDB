from pymongo import MongoClient
# Create Connection
client = MongoClient('localhost', 27017)
print(f"Existing Databases")
print(client.list_database_names())
# Create a New Database - dictionary style
database_foods = client['foods']
# Alternative method for simple strings #
# database = client.foods
# Create a Collection - dictionary style
col_desserts = database_foods['desserts']
# Insert a Single Document
document = {'name': 'chocolate cake', 'price': 20, 'ingredients':['chocolate', 'flour', 'eggs']}
col_desserts.insert_one(document)
print(f"\nVerify the New Database")
print(client.list_database_names())
print(f"\nCollections in the Database foods")
print(database_foods.list_collection_names())
print(f"\nDocuments in the desserts Collection")
dessert = col_desserts.find()
# Print each Document
for des in dessert:
    print(des)