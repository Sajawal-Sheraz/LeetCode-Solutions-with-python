import math


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next

    def isPalindrome(self):
        if not self.head.next:
            return True
        first_tail = self.head
        first_header = self.head
        sec_tail = self.head
        count = 0
        while sec_tail:
            sec_tail = sec_tail.next
            count += 1
        sec_tail = self.head
        half = count // 2
        for i in range(count - 1):
            if i < half - 1:
                first_tail = first_tail.next
                sec_tail = first_tail
            else:
                sec_tail = sec_tail.next
        sec_head = first_tail.next
        first_tail.next = None

        temp_p = None
        while sec_head:
            next_head = sec_head.next
            sec_head.next = temp_p
            temp_p = sec_head
            if not next_head:
                break
            sec_head = next_head

        while first_header:
            if first_header.data != sec_head.data:
                return False
            first_header = first_header.next
            sec_head = sec_head.next

        return True


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    for i in [1, 2]:
        linked_list.append(i)
    print(linked_list.isPalindrome())
    # linked_list.print_list()
