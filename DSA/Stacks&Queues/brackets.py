class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def is_balanced(parentheses):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    brackets_map = {")": "(", "]": "[", "}": "{"}

    for bracket in parentheses:
        if bracket in opening_brackets:
            stack.push(bracket)
        elif bracket in closing_brackets:
            if stack.is_empty() or brackets_map[bracket] != stack.pop():
                return False

    return stack.is_empty()


if __name__ == "__main__":
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}", "{{{{}}", "}}"]
    for test_case in test_cases:
        if is_balanced(test_case):
            print(f"{test_case} is balanced")
        else:
            print(f"{test_case} is not balanced")
