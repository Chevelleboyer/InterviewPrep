import unittest
from pythonds.basic.stack import Stack

class InterviewTests(unittest.TestCase):

	#ReverseString
	def testReverseString(self):
		myStack = Stack()
		for i in 'chevelle':
			myStack.push(i)
		reversedWord = ''
		for i in 'chevelle':
			reversedWord += (myStack.pop())
		self.assertEqual('ellevehc', reversedWord)

	#ReverseString
	def testReverseSomething(self):
		reversedWord = 'chevelle'
		self.assertEqual('ellevehc', reversedWord[::-1])

	#FizzBuzz
	def testFizzBuzz(self):
		pass

if __name__ == '__main__':
    unittest.main()