import  pytest # type: ignore
from evm.stack import Stack



# def test_push():
#     with pytest.raises( IndexError, match="Stack overflow"):
       

def test_pop():
    stack = Stack()
    print(stack)
    with pytest.raises(IndexError) as exc_info:
        stack.pop()
        assert str(exc_info.value) == "Stack overflow", "Expected 'Stack overflow' error message"


def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1
    

def test_stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    stack.pop()
    assert stack.peek() == 1



def test_stack_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError) as exc_info:
        stack.pop()
        assert str(exc_info.value) == "Stack overflow", "Expected 'Stack overflow' error message"


def test_stack_peek_empty():
    stack = Stack()
    with pytest.raises(IndexError) as exc_info:
        stack.peek()
        assert str(exc_info.value) == "peek from empty stack", "Expected 'peek from empty stack' error message"

    # with pytest.raises(IndexError, match="list index out of range"):
    #     stack.peek()

