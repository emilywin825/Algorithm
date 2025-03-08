# https://leetcode.com/problems/design-browser-history/description/

class ListNode(object):
    def __init__(self,val=0,prev=None,next=None):
        self.val=val
        self.next=next
        self.prev=prev

class BrowserHistory(object):

    def __init__(self, homepage):
        self.head=self.current=ListNode(val=homepage)

    def visit(self, url):
        self.current.next=ListNode(val=url, prev=self.current)
        self.current=self.current.next
        return None

    def back(self, steps):
        for _ in range(steps):
            if self.current.prev is None:
                break
            else:
                self.current=self.current.prev
        return self.current.val
        

    def forward(self, steps):
        for _ in range(steps):
            if self.current.next is None:
                break
            else:
                self.current=self.current.next
        return self.current.val