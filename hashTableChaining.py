# Node class for linked list
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash Table class
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            new_node.next = self.table[index]
            self.table[index] = new_node
        print(f"Inserted ({key}, {value}) at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        head = self.table[index]

        if head and head.key == key:
            self.table[index] = head.next
            print(f"Deleted key {key} from index {index}")
            return True

        current = head
        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                print(f"Deleted key {key} from index {index}")
                return True
            current = current.next

        print(f"Key {key} not found")
        return False

    def display(self):
        print("\nHash Table Contents:")
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            current = self.table[i]
            while current:
                print(f"({current.key}, {current.value}) ->", end=" ")
                current = current.next
            print("None")
        print("-" * 40)


# ------------------- Simple Menu -------------------

def menu():
    ht = HashTable()
    while True:
        print("\n---- HASH TABLE MENU ----")
        print("1. Insert key-value")
        print("2. Search key")
        print("3. Delete key")
        print("4. Display table")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            key = int(input("Enter key (integer): "))
            value = input("Enter value: ")
            ht.insert(key, value)

        elif choice == '2':
            key = int(input("Enter key to search: "))
            value = ht.search(key)
            if value is not None:
                print(f"Key {key} found with value: {value}")
            else:
                print(f"Key {key} not found")

        elif choice == '3':
            key = int(input("Enter key to delete: "))
            ht.delete(key)

        elif choice == '4':
            ht.display()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please select 1-5.")


# Run the simple menu
if __name__ == "__main__":
    menu()
