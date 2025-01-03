
# question 1


def insert_after_value(self, data_after, data_to_insert):
    if self.head is None:
        return

    if self.head.data == data_after:
        self.head.next = Node(data_to_insert, self.head.next)
        return

    itr = self.head
    while itr:
        if itr.data == data_after:
            itr.next = Node(data_to_insert, itr.next)
            break

        itr = itr.next





#question 2
# Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well.
# That way you can iterate in forward and backward direction. Your node class will look this this,


