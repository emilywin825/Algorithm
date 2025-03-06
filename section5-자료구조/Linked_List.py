class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

# 4개의 노드를 생성        
first=Node(1)
second=Node(2)
third=Node(3)
fourth=Node(4)

# 노드의 논리적 연결성을 만듦
first.next = second
second.next = third
third.next = fourth

class LinkedList(object):
	def __inint__(self): # LinkedList는 head가 있어야 함
		self.head=None
		self.tail=None
            
	def append(self,value):
            new_node = Node(value)
            if self.head is None:
                  self.head=new_node
                  self.tail=new_node
            else:
                self.tail.next=new_node
                self.tail=self.tail.next
                
	# def append(self,value):
	# 	new_node=Node(value)
    #     if self.head is None:
    #         self.head=new_node
    #     # 맨 뒤의 노드가 new_node를 가리켜야 한다.
    #     else:
	# 		current=self.head
    #         while(current.next):
    #             current=current.next
    #         current.next=new_node
        
	# def get(self,idx):
    #     current=self.head
    #     for _ in range(idx):
    #         current=current.next
    #     return current.value
    
    # def insert(self,val,idx):
    #     current=self.head
    #     for _ in range(idx):
    #         current=current.next
    #     new_node=Node(val)
    #     new_node.next=current.next
    #     current.next=new_node
    
	# def remove(self,idx):
    #     current=self.head
    #     for _ in range(idx):
    #         current=current.next
    #     nexx=current.next
    #     current.next=nexx.next        
            
