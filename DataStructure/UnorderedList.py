"""
Using Unordered LinkedList :
Read the Text from a file, split it into words and arrange it as Linked List.
Take a user input to search a Word in the List. If the Word is not found then add it
to the list, and if it found then remove the word from the List. In the end save the
list into a file
"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def display_all(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next_node

    def insert_at_end(self, data):
        """

        :param data: value inserted
        :return: inserted position of data
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node

    def display(self):
        current = self.head
        temp = ""
        while current:
            # print(current.data, end = ' ')
            temp = temp + current.data + " "
            current = current.get_next()
        return temp

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    # Getting the words from the File and creating a file.
    name = input("\nEnter the File Name: ")
    hand = open(name, 'r')
    FLines = hand.readlines()
    for line in FLines:
        words = line.split()
        for word in words:
            llist.insert_at_end(word)
    print("\n File contents in the List is:")
    llist.display_all()

    # Searching the word in the Linked List
    Search_word = input("\nEnter the word to be searched : ")
    if llist.search(Search_word):
        llist.delete(Search_word)
        print("Word", Search_word, " found in the Linked List and deleted")
    else:
        print("Word", Search_word, " not found in the Linked List")
    # llist.display_all()

    # Updated Linked list is stored in the file b.txt
    name = "b.txt"
    hand = open(name, 'w+')
    a = llist.display()
    # print(a)
    hand.write(a)
    hand.close()

    print("File created with filename b.txt")