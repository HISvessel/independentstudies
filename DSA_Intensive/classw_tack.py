#!/usr/bin/python3

class stack:
    def __init__(self, items = []):
        self.items = items if not None else []

    def is_not_empty(self, elem):
        return self.items.pop(elem) if len(self.items) > 0 else self.items


empty_stack = stack()

full_stack = stack([1, 2, 3, 4])

print(empty_stack.is_not_empty(0))

print(full_stack.is_not_empty(0))