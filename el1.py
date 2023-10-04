import pymongo

client = pymongo.MongoClient("mongodb://localhost:27107")
db = client.test
collection = db.music_collection

def create():
  """Creates a new record."""
  name = input("Enter the name of the song: ")
  artist = input("Enter the name of the artist: ")
  genre = input("Enter the genre of the song: ")

  document = {"name": name, "artist": artist, "genre": genre}

  collection.insert_one(document)

def read():
  """Reads a record."""
  name = input("Enter the name of the song: ")

  document = collection.find_one({"name": name})

  if document is not None:
    print(document)
  else:
    print("No record found")

def update():
  """Updates a record."""
  name = input("Enter the name of the song: ")

  document = collection.find_one({"name": name})

  if document is not None:
    new_name = input("Enter the new name of the song: ")
    new_artist = input("Enter the new name of the artist: ")
    new_genre = input("Enter the new genre of the song: ")

    document["name"] = new_name
    document["artist"] = new_artist
    document["genre"] = new_genre
                    
    collection.update_one({"name": name}, {"$set": {"name": new_name, "artist": new_artist, "genre": new_genre}})
  else:
    print("No record found")

def delete():
  """Deletes a record."""
  name = input("Enter the name of the song: ")

  collection.delete_one({"name": name})

def main():
  """The main function."""
  while True:
    print("Select an option:")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      create()
    elif choice == "2":
      read()
    elif choice == "3":
      update()
    elif choice == "4":
      delete()
    elif choice == "5":
      break

if __name__ == "__main__":
  main()