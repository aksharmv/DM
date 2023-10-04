from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client['Music']
collection = db['Song']

def createCollection():
  name = input("Song Name: ")
  artist = input("Artist: ")
  genre = input("Genre: ")

  document = {"Song Name": name, "Artist": artist, "Genre": genre}

  collection.insert_one(document)

def readCollection():
  name = input("Song name: ")

  document = collection.find_one({"Song Name": name})

  if document is not None:
    print(document)
  else:
    print("No collection found")

def updateCollection():
  name = input("Song Name: ")

  document = collection.find_one({"Song Name": name})

  if document is not None:
    new_name = input("Song Name: ")
    new_artist = input("Artist: ")
    new_genre = input("Genre: ")

    document["Song Name"] = new_name
    document["Artist"] = new_artist
    document["Genre"] = new_genre
                    
    collection.update_one({"Song Name": name}, {"$set": {"Song Name": new_name, "Artist": new_artist, "Genre": new_genre}})
  else:
    print("No collection found")

def deleteCollection():
  name = input("Song name: ")

  collection.delete_one({"Song Name": name})

def query():
   genre=input("Genre: ")
   document = collection.find_one({"Genre":"rock"})
   if document is not None:
    print(document)
   else:
     print("no song in the specified genre")

while 1:
  print("Enter a choice:")
  print("1. Create")
  print("2. Read")
  print("3. Update")
  print("4. Delete")
  print("5. Exit")
  print("6. Query")
  print("=======================")
  ch = input("Choice: ")
  print("=======================")

  if ch == "1":
    createCollection()
  elif ch == "2":
    readCollection()
  elif ch == "3":
    updateCollection()
  elif ch == "4":
    deleteCollection()
  elif ch == "5":
    break
  elif ch == "6":
    query()
  else:
    print("invalid choice")