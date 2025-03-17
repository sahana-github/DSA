# Define a class for a single node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data (value) of the node
        self.next = None  # Pointer to the next node (initially None since it's a new node)

# Define the linked list class
class LinkedList:
    def __init__(self):
        self.head = None  # Head (first node) of the linked list, initially empty

    # Method to insert a new node at the end of the linked list
    def insert(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # Check if the list is empty
            self.head = new_node  # If empty, set the new node as the head (first node)
            return  # Exit the function

        # If the list is not empty, traverse to the last node
        temp = self.head  # Start from the head
        while temp.next:  # Move to the next node until reaching the last node
            temp = temp.next  

        temp.next = new_node  # Attach the new node at the end of the list

    # Method to display all elements of the linked list
    def display(self):
        temp = self.head  # Start from the head node
        while temp:  # Loop until we reach the end (None)
            print(temp.data, end=" -> ")  # Print the current node's data
            temp = temp.next  # Move to the next node
        print("None")  # Print "None" to indicate the end of the list


ll = LinkedList()  # Create an empty linked list
ll.insert(10)  # Insert 10
ll.insert(20)  # Insert 20
ll.insert(30)  # Insert 30
ll.display()   # Display the linked list: Output -> 10 -> 20 -> 30 -> None
