# Hash Table implementation using Linear Probing
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = "<deleted>"

    # Hash function using division method
    def hash(self, key):
        return key % self.size

    # Insert a key using linear probing
    def insert(self, key):
        index = self.hash(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None or self.table[new_index] == self.deleted:
                self.table[new_index] = key
                print(f"Inserted {key} at index {new_index}")
                return
        print("Hash table is full! Cannot insert key.")

    # Search a key using linear probing
    def search(self, key):
        index = self.hash(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                break  # key not found
            if self.table[new_index] == key:
                print(f"Key {key} found at index {new_index}")
                return True
        print(f"Key {key} not found")
        return False

    # Delete a key (mark as deleted)
    def delete(self, key):
        index = self.hash(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                break
            if self.table[new_index] == key:
                self.table[new_index] = self.deleted
                print(f"Key {key} deleted from index {new_index}")
                return
        print(f"Key {key} not found to delete")

    # Display the hash table
    def display(self):
        print("Hash Table:")
        for i, key in enumerate(self.table):
            print(f"Index {i}: {key}")
        print()


# ----------------- Main Menu -----------------
size = int(input("Enter size of hash table: "))
hash_table = HashTable(size)

while True:
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        hash_table.insert(key)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        hash_table.search(key)
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        hash_table.delete(key)
    elif choice == 4:
        hash_table.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
