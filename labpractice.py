from pymongo import MongoClient

client=MongoClient("localhost",27017)
db=client['practice']
collection=db['music']

def insertone():
    song=input("Song name :")
    artist=input("Artist name :")
    genre=input("Genre :")

    document={"song":song,"artist":artist,"genre":genre}

    collection.insert_one(document)

def insertmany():
    s1=input("Song name :")
    a1=input("Artist name :")
    g1=input("Genre :")
    s2=input("Song name :")
    a2=input("Artist name :")
    g2=input("Genre :")

    document=[{"song":s1,"artist":a1,"genre":g1},{"song":s2,"artist":a2,"genre":g2}]

    collection.insert_many(document)

def findone():
    song=input("Enter song :")

    document=collection.find_one({"song":song})

    if document is None:
        print("No document found")
    else:
        print(document)

def findmany():
    song=input("Enter song :")

    document=collection.find({"song":song})

    if document is None:
        print("No document found")
    else:
        for x in document:
            print(x)

def updateone():
    song=input("Enter song :")

    document=collection.find_one({"song":song})

    if document is None:
        print("No document found")
    else:
        new_song=input("Enter new song :")
        new_artist=input("Enter new artist :")
        new_genre=input("Enter new genre :")

        collection.update_one({"song":song},{"$set":{"song":new_song,"artist":new_artist,"genre":new_genre}})

def updatemany():
    song=input("Enter song :")

    document=collection.find_one({"song":song})

    if document is None:
        print("No document found")
    else:
        new_song=input("Enter new song :")
        new_artist=input("Enter new artist :")
        new_genre=input("Enter new genre :")

        collection.update_many({"song":song},{"$set":{"song":new_song,"artist":new_artist,"genre":new_genre}})

def deleteone():
    song=input("Enter song :")

    document=collection.find_one({"song":song})

    if document is None:
        print("No document found")
    else:
        collection.delete_one({"song":song})

def deletemany():
    song=input("Enter song :")

    document=collection.find_one({"song":song})

    if document is None:
        print("No document found")
    else:
        collection.delete_many({"song":song})    

print("1.insertone\n2.insertmany\n3.findone\n4.findmany\n5.updateone\n6.updatemany\n7.deleteone\n8.deletemany")
while(1):
    ch=int(input("Enter choice :"))
    if ch==1:
        insertone()
    elif ch==2:
        insertmany()
    elif ch==3:
        findone()
    elif ch==4:
        findmany()
    elif ch==5:
        updateone()
    elif ch==6:
        updatemany()
    elif ch==7:
        deleteone()
    elif ch==8:
        deletemany()
    else:
        break