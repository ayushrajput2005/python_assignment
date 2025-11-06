# ----------------- Node Definition -----------------
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# ----------------- BST Definition -----------------
class BST:
    def __init__(self):
        self.root = None

    # --------- Insertion ---------
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
        print(f"Inserted {key} into BST")

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        else:
            print(f"Key {key} already exists in BST")
        return node

    # --------- Search ---------
    def search(self, key):
        found = self._search_recursive(self.root, key)
        if found:
            print(f"Key {key} found in BST")
        else:
            print(f"Key {key} not found in BST")
        return found

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    # --------- Deletion ---------
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            print(f"Key {key} not found in BST")
            return node
        # Traverse left or right
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Node found
            print(f"Deleting {key}...")
            # Case 1: No child
            if node.left is None and node.right is None:
                return None
            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Case 3: Two children
            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.right = self._delete_recursive(node.right, successor.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # --------- Inorder Traversal ---------
    def inorder(self):
        print("Inorder Traversal of BST:", end=' ')
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.key, end=' ')
            self._inorder_recursive(node.right)


# ----------------- Main Program -----------------
bst = BST()

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display Inorder")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        bst.insert(key)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        bst.search(key)
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        bst.delete(key)
    elif choice == 4:
        bst.inorder()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
