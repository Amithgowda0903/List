class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    return head

def traverse(head):
    temp = head
    while temp is not None:
        print(str(temp.data) + " --> ", end='')
        temp = temp.next
    print('None')

def insert_at_start(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node 

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = new_node
    return head

def insert_after_node(head, target, data):
    temp = head
    while temp != None and temp.data != target:
        temp = temp.next
    if temp is None:
        print("Node not found.")
        return head
    new_node = Node(data)
    new_node.next = temp.next
    temp.next = new_node
    return head

def insert_before_node(head, target, data):
    if head is None:
        return None
    if head.data == target:  # If the target is the first node
        return insert_at_start(head, data)
    temp = head
    prev = None
    while temp != None and temp.data != target:
        prev = temp
        temp = temp.next
    if temp == None:
        print("Node not found.")
        return head
    new_node = Node(data)
    new_node.next = temp
    prev.next = new_node
    return head

def insert_at_position(head, position, data):
    if position == 1:
        return insert_at_start(head, data)
    temp = head
    count = 1
    while temp != None and count < position - 1:
        temp = temp.next
        count += 1
    if temp == None:
        print("Position out of range.")
        return head
    new_node = Node(data)
    new_node.next = temp.next
    temp.next = new_node
    return head

head = None
choice = 1
while choice == 1:
    data = int(input('Enter data: '))
    head = create(head, data)
    choice = int(input('Enter 1 to add more nodes, 0 to stop: '))

head = insert_at_start(head, int(input("\nEnter data to insert at start: ")))
traverse(head)
head = insert_at_end(head, int(input("\nEnter data to insert at end: ")))
traverse(head)
target = int(input("\nEnter node value after which to insert: "))
data = int(input("Enter data to insert: "))
head = insert_after_node(head, target, data)
traverse(head)
target = int(input("\nEnter node value before which to insert: "))
data = int(input("Enter data to insert: "))
head = insert_before_node(head, target, data)
traverse(head)
position = int(input("\nEnter position to insert at: "))
data = int(input("Enter data to insert: "))
head = insert_at_position(head, position, data)
traverse(head)
