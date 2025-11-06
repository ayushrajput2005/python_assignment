class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def add(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, roll):
        if not self.head:
            print("Empty list")
            return

        if self.head.roll == roll:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next.roll == roll:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Not found")

    def update(self, old_roll, new_roll, new_name, new_marks):
        if not self.head:
            print("Empty list")
            return

        temp = self.head
        while temp:
            if temp.roll == old_roll:
                temp.roll = new_roll
                temp.name = new_name
                temp.marks = new_marks
                return
            temp = temp.next

        print("Not found")

    def show(self):
        if not self.head:
            print("Empty list")
            return

        temp = self.head
        while temp:
            print(f"Roll : {temp.roll} \nName : {temp.name} \nMarks : {temp.marks}\n")
            temp = temp.next

    def sort(self):
        if not self.head or not self.head.next:
            print("Nothing to sort")
            return

        # Convert linked list to list
        nodes = []
        temp = self.head
        while temp:
            nodes.append(temp)
            temp = temp.next

        # Sort nodes by roll number
        nodes.sort(key=lambda x: x.roll)

        # Rebuild linked list
        self.head = nodes[0]
        temp = self.head
        for node in nodes[1:]:
            temp.next = node
            temp = temp.next
        temp.next = None
        print("List sorted by roll number")

# create list object
student_list = List()

# menu
while True:
    print("1. Add \n2. Delete \n3. Update \n4. Show \n5. Sort by Roll \n6. Exit")
    opt = int(input("Enter option: "))

    if opt == 1:
        roll = int(input("Enter roll no.: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        student_list.add(roll, name, marks)
    elif opt == 2:
        roll = int(input("Enter roll no. to delete: "))
        student_list.delete(roll)
    elif opt == 3:
        old_roll = int(input("Enter old roll no.: "))
        new_roll = int(input("Enter new roll no.: "))
        new_name = input("Enter new name: ")
        new_marks = int(input("Enter new marks: "))
        student_list.update(old_roll, new_roll, new_name, new_marks)
    elif opt == 4:
        student_list.show()
    elif opt == 5:
        student_list.sort()
    elif opt == 6:
        break
    else:
        print("Invalid option")
