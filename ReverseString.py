from pythonds.basic.stack import Stack

#Example showing knowledge of Stack() data structure
def reverseString(aWord):
	myStack = Stack()

	for i in aWord:
		myStack.push(i)
	reversedWord = ''
	for i in aWord:
		reversedWord += (myStack.pop())
	return reversedWord

#Example showing knowledge of python syntax
def reverseSomething(something):
	return something[::-1]