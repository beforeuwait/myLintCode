# coding=utf-8

"""
数据流中第一个独特的数 II

描述:我们需要实现一个叫 DataStream 的数据结构。并且这里有 两 个方法需要实现：

1.void add(number) // 加一个新的数
2.int firstUnique() // 返回第一个独特的数

思路:
没搞明白
"""

class DataStream:
    
    def __init__(self):
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.num_to_prev = {}
        self.duplicates = set()
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        if num in self.duplicates:
            return
        
        if num not in self.num_to_prev:
            self.push_back(num)            
            return
        
        # find duplicate, remove it from hash & linked list
        self.duplicates.add(num)
        self.remove(num)
    
    def remove(self, num):
        prev = self.num_to_prev.get(num)
        del self.num_to_prev[num]
        prev.next = prev.next.next
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            # if we removed the tail node, prev will be the new tail
            self.tail = prev

    def push_back(self, num):
        # new num add to the tail
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        if not self.dummy.next:
            return None
        return self.dummy.next.val