from dataclasses import dataclass
from typing import Any

@dataclass
class Element:
    value: Any
    priority: int
 

class BinaryHeap:

    def __init__(self):
        self.heap = []
    
    def push(self, element):
        # naivni implementace binarni haldy
        self.proprint = element
        self.heap.append(element)
        self.push_reorder(len(self.heap) - 1)
    
    def push_reorder(self, index):
        new_elmnt_index = index
        parent_index = (new_elmnt_index - 1) // 2

        if self.heap[new_elmnt_index].priority < self.heap[parent_index].priority and parent_index >= 0:
            print(parent_index)
            print(self.proprint)
            self.heap[parent_index], self.heap[new_elmnt_index] = self.heap[new_elmnt_index], self.heap[parent_index]
            self.push_reorder(parent_index)

    def pop(self):
        # naivni implementace binarni haldy
        # najdi nejmensi prvek a vrat ho
        if not self.heap:
            raise Exception("Heap is empty")
        # Nevim jestli tomu rozumím správně, ale pokud bude halda vždy správně seřazená, tak kořen bude vždy mít "nejmenší" prioritu
        self.return_value = self.heap[0]
        self.heap.pop(0)
        self.pop_reorder()
    
    def pop_reorder(self):
        for i in self.heap:
            self.push_reorder(self.heap.index(i))

        return self.return_value

    def head(self):
        if not self.heap:
            raise Exception("Heap is empty")
        # vrati nejmensi element ve fronte (element na cele fronty)
        # protoze mame naivni implementaci, musime projit cely seznam
        return self.heap[0]

"""el1 = Element(12, 8)
el2 = Element(12, 4)
el3 = Element(12, 5)
el4 = Element(12, 1)

bh = BinaryHeap()
bh.push(el1)
bh.push(el2)
bh.push(el3)
bh.push(el4)
bh.pop()
print(bh.heap)"""
