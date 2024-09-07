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
        print()

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_head = head
        count = 0
        while current_head:
            count += 1
            current_head = current_head.next
        middle_idx = count // 2

        current_head = head
        for i in range(count):
            if i >= middle_idx:
                return current_head
            current_head = current_head.next

    def reverseList(self):
        if not self.head or not self.head.next:
            return self.head

        prev = None

        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def reorder(self):
        if not self.head or not self.head.next:
            return

        # Find the middle of the linked list using the slow and fast pointer technique
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # Reverse the second half of the linked list
        prev_node = None
        current_node = slow_ptr.next
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        slow_ptr.next = None  # Break the original list into two halves

        # Merge the two halves of the linked list
        first_half = self.head
        second_half = prev_node
        while second_half:
            next_first = first_half.next
            next_second = second_half.next
            first_half.next = second_half
            second_half.next = next_first
            first_half = next_first
            second_half = next_second


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    for i in [1, 2, 3, 4, 5]:  # 1,4,2,3
        linked_list.append(i)

    # linked_list.middle_node()
    # linked_list.reverseList()
    linked_list.reorder()

    linked_list.print_list()  # [1,4,2,3]
