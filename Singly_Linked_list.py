class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def create(head,data):
    new_node = Node(data)
    if head == None :
        head = new_node
        new_node = head
    else:
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
    return head

def traverse (head):
    temp = head
    while temp != None:
        print(str(temp.data) + "-->",end = '')
        temp = temp.next
    print('None')

'''------------Deletion starts here------------------'''

def deletion_start(head):
    head = head.next
    while head != None:
        print(str(head.data) + "-->",end = '')
        head = head.next
    print('None')

def deletion_end(head):
    temp = head
    while temp.next != None:
        print(str(temp.data) + "-->",end = '')
        temp1 = temp
        temp = temp.next
    temp1.next = None
    print("None")
    
'''-------------End of deletion---------------------'''

'''--------------insertion starts here-------------'''
def insertion_start(head):
    temp = new_node
    new_node= Node(data)
    head = temp
    while head.next != None:
        print(str(head.data) + "-->",end = '')
    temp1 = head
    head = head.next
    print(str(head.next.data))


def insertion_end(head):
    temp = head
    new_node = Node(data)
    while temp.next != None:
        print(str(temp.data) + "-->",end = '')
        temp = temp.next
    temp.next = new_node
    print(str(temp.next.data))

    
head = None
choice = 1
while choice == 1:
    data = int(input('enter data'))
    head = create(head,data)
    #print(head)
    choice = int(input('enter 1 for adding more nodes and 0 for no'))

traverse(head)
deletion_start(head)
deletion_end(head)

insertion_end(head)
insertion_start(head)
