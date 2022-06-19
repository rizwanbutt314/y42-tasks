import unittest

from .task_1 import Stack


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack()

        # dummy data in stack
        self.stack.push("test-1")
        self.stack.push("test-2")

    def test_stack_size(self):
        self.stack = Stack()

        # self.stack size with no data
        self.assertEqual(isinstance(self.stack.size(), int), True)
        self.assertEqual(self.stack.size(), 0)

        # self.stack size with data
        self.stack.push("test")

        self.assertEqual(isinstance(self.stack.size(), int), True)
        self.assertEqual(self.stack.size(), 1)

        self.stack.push("test")

        self.assertEqual(isinstance(self.stack.size(), int), True)
        self.assertEqual(self.stack.size(), 2)

    def test_stack_push(self):

        # check top element
        self.assertEqual(self.stack.peek(), "test-2")

        # push element to check it's at the top
        self.stack.push("test-3")
        self.assertEqual(self.stack.peek(), "test-3")

        # push invalid element
        with self.assertRaises(Exception) as context:
            self.stack.push(None)

        self.assertTrue("Invalid element" in str(context.exception))

    def test_stack_pop(self):

        # check top element
        self.assertEqual(self.stack.peek(), "test-2")

        # pop the top element
        poped_element = self.stack.pop()

        # validate the return poped element
        self.assertEqual(poped_element, "test-2")
        self.assertEqual(self.stack.peek(), "test-1")

        # empty the self.stack
        self.stack.pop()
        self.assertEqual(self.stack.size(), 0)

        # call pop when self.stack is empty
        with self.assertRaises(Exception) as context:
            self.stack.pop()

        self.assertTrue("Empty stack" in str(context.exception))

    def test_stack_peek(self):
        # check stack size to verify it's not empty
        self.assertEqual(self.stack.size(), 2)

        # check top element
        top_element = self.stack.peek()
        self.assertEqual(top_element, "test-2")
        self.assertEqual(self.stack.size(), 2)

        # empty the self.stack
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.size(), 0)

        # call pop when self.stack is empty
        with self.assertRaises(Exception) as context:
            self.stack.peek()

        self.assertTrue("Empty stack" in str(context.exception))

    def test_stack_empty(self):
        self.stack = Stack()

        # self.stack empty
        self.assertEqual(isinstance(self.stack.empty(), bool), True)
        self.assertEqual(self.stack.empty(), True)
        self.assertEqual(self.stack.size(), 0)

        # dummy data in self.stack
        self.stack.push("test-1")

        # self.stack with data
        self.assertEqual(isinstance(self.stack.empty(), bool), True)
        self.assertEqual(self.stack.empty(), False)
        self.assertEqual(self.stack.size(), 1)


if __name__ == '__main__':
    unittest.main()
