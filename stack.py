# --------------------------------------------------ARRAY IMPLEMENTATION-----------------------------
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)  # O(1)

#     def pop(self):
#         if len(self) > 0:
#             return self.storage.pop()  # O(1)
#         else:
#             return None


# ----------------------------------------------------------LINKED LIST IMPLEMENTATION--------------------------
from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if len(self) > 0:
            self.size -= 1
            return self.storage.remove_head()  # O(1)
        else:
            return None
