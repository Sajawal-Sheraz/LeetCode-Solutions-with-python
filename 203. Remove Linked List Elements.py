def remove_item(head, val):
    current_ptr = head
    next_ptr = head.next
    while next_ptr:
        if next_ptr.val == val:
            current_ptr.next = next_ptr.next
            next_ptr = next_ptr.next
        else:
            current_ptr = next_ptr
            next_ptr = next_ptr.next
    next_ptr = head.next
    if head.val == val:
        head = next_ptr
        next_ptr = next_ptr.next if next_ptr else next_ptr
    return head
