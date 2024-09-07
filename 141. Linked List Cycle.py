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

    def list_cycle(self, pos):

        # To make it  cycle linked list
        next_ptr = self.head
        pre_ptr = self.head
        while next_ptr.next:
            next_ptr = next_ptr.next

        c = 0
        while pre_ptr.next:
            if pos == c:
                next_ptr.next = pre_ptr
                break
            c = c + 1
        # list_cycle

        if not self.head or not self.head.next:
            return False

        slow = self.head
        fast = self.head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    for i in [3, 2, 0, -4]:
        linked_list.append(i)

    print(linked_list.list_cycle(1))
    # linked_list.print_list()
