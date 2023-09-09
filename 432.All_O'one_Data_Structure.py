class ListCount:
    def __init__(self, set_string, count, prev= None, next= None):
        self.set_string = set_string
        self.count = count
        self.next = next
        self.prev = prev

class AllOne:
    def __init__(self):
        self.head = ListCount({""}, count= 0)
        self.tail = ListCount({""}, count= float('inf'), prev= self.head)
        self.head.next = self.tail
        self.dic_string = {}

    def inc(self, key: str) -> None:
        if key in self.dic_string:
            node = self.dic_string[key]
            inc_cnt = node.count+1    
            if len(node.set_string) == 1:
                if inc_cnt ==  node.next.count:
                    node.next.set_string.add(key)
                    self.dic_string[key] = node.next
                    node.next.prev, node.prev.next = node.prev, node.next 
                else:
                    node.count = inc_cnt       
            else:
                node.set_string.remove(key)
                if inc_cnt == node.next.count:
                    node.next.set_string.add(key)
                    self.dic_string[key] = node.next
                else:
                    new_node = ListCount(set_string= {key}, count= inc_cnt, prev= node, next= node.next)
                    node.next.prev = new_node
                    node.next = new_node
                    self.dic_string[key] = new_node
        else:
            if self.head.next.count == 1:
                self.head.next.set_string.add(key)
                self.dic_string[key] = self.head.next
            else:  
                node = ListCount(set_string= {key}, count= 1, prev= self.head, next= self.head.next)
                self.head.next.prev = node
                self.head.next = node
                self.dic_string[key] = node

    def dec(self, key: str) -> None:
        node = self.dic_string[key]
        if node.count == 1:    
            if len(node.set_string) == 1:  
                node.next.prev, node.prev.next = node.prev, node.next 
            else:
                node.set_string.remove(key)
            del self.dic_string[key]                        
        else:
            dec_cnt = node.count-1
            if len(node.set_string) == 1:
                if dec_cnt ==  node.prev.count:
                    node.prev.set_string.add(key)
                    self.dic_string[key] = node.prev
                    node.next.prev, node.prev.next = node.prev, node.next 
                else:
                    node.count = dec_cnt       
            else:
                node.set_string.remove(key)
                if dec_cnt == node.prev.count:
                    node.prev.set_string.add(key)
                    self.dic_string[key] = node.prev
                else:
                    new_node = ListCount(set_string= {key}, count= dec_cnt, prev= node.prev, next= node)
                    node.prev.next = new_node
                    node.prev = new_node
                    self.dic_string[key] = new_node

    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.set_string))
        
    def getMinKey(self) -> str:
        return next(iter(self.head.next.set_string))