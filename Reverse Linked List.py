import unittest
import NodeSolution

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class unitest(unittest.TestCase):
    def testNone(self):
        Input = None
        Output = None
        self.assertEqual(Solution().reverseList(Input),Output)
    def testSample(self):
        row = [1,2,3]
        node = NodeSolution.NodeSolution()
        Input = node.AddNode(row)
        Ans = [3,2,1]
        Output = node.ShowNode(Solution().reverseList(Input))
        self.assertEqual(Ans,Output)

class Solution():
    def reverseList(self, head):
        prev = None
        while(head):
            Next = head.next
            head.next = prev
            prev = head
            head = Next
        return prev

if __name__ == '__main__':
    unittest.main()
