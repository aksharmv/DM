from pymongo import MongoClient

client=MongoClient("localhost",27017)
db=client['tour']
collection=db['place']

def insert():
    name=input("enter place:")
    country=input("enter country:")
    document={"name":name,"country":country}
    collection.insert_one(document)

def read():
    name=input("enter place:")
    document=collection.find_one({"name":name})
    if  document is None:
        print("document not found")
    else:
        print(document)

def delete():
    name=input("enter place:")
    document=collection.find_one({"name":name})
    if document is None:
        print("document not found")
    else:
        collection.delete_one({"name":name})

def update():
    name=input("enter place:")
    document=collection.find_one({"name":name})
    if document is None :
        print("no collection found")
    else:
        new_name=input("enter new place:")
        new_country=input("enter new country:")
        collection.update_one({"name":name},{"$set":{"name":new_name,"country":new_country}})
        
print("1.insert\n2.read\n3.delete\n4.update\n5.exit")
while(1):
    ch=int(input("enter choice:"))
    if ch==1:
        insert()
    elif ch==2:
        read()
    elif ch==3:
        delete()
    elif ch==4:
        update()
    elif ch==5:
        break
    else:
        print("invalid input")