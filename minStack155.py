"""
155. Min Stack: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

"""

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        pushes the element val onto the stack.
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
      """
      void pop() removes the element on the top of the stack.
      """
        if len(self.stack) > 0:
            item = self.stack.pop()
            if len(self.min_stack)>0 and item==self.min_stack[-1]:
                self.min_stack.pop()
            return item

    def top(self):
        """
        :rtype: int
        gets the top element of the stack.
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None        
    def getMin(self):
        """
        :rtype: int
        retrieves the minimum element in the stack
        """
        return self.min_stack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
